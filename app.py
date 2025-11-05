import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import hashlib

# Page configuration
st.set_page_config(
    page_title="Demo App - Registration & Login",
    page_icon="🔐",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    .success-box {
        padding: 1rem;
        border-radius: 8px;
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        margin-bottom: 1rem;
    }
    .error-box {
        padding: 1rem;
        border-radius: 8px;
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Google Sheets configuration
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

SPREADSHEET_ID = '1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I'
USERS_SHEET = 'users'

# Initialize session state
if 'user' not in st.session_state:
    st.session_state.user = None
if 'page' not in st.session_state:
    st.session_state.page = 'login'

def get_google_sheet():
    """Initialize and return Google Sheet client"""
    try:
        creds = None
        # Try to get credentials from Streamlit secrets (for Streamlit Cloud)
        try:
            if hasattr(st, 'secrets') and 'credentials' in st.secrets:
                creds_dict = dict(st.secrets.credentials)
                
                # Fix private key format - ensure newlines are preserved
                if 'private_key' in creds_dict:
                    private_key = str(creds_dict['private_key'])
                    
                    # Remove any leading/trailing whitespace
                    private_key = private_key.strip()
                    
                    # Diagnostic: Check key length
                    original_length = len(private_key)
                    
                    # Handle different formats of newline representation
                    # TOML might store \n as actual newlines or as literal \n
                    if '\\n' in private_key and '\n' not in private_key:
                        # Replace literal \n with actual newlines
                        private_key = private_key.replace('\\n', '\n')
                    elif '\r\n' in private_key:
                        # Handle Windows line endings
                        private_key = private_key.replace('\r\n', '\n')
                    elif not '\n' in private_key and 'BEGIN PRIVATE KEY' in private_key:
                        # If no newlines at all but has BEGIN marker, try to add them
                        # This handles the case where \n was interpreted as actual newlines
                        # but we need to add newlines after each line
                        lines = private_key.split('-----BEGIN PRIVATE KEY-----')
                        if len(lines) > 1:
                            key_part = lines[1].split('-----END PRIVATE KEY-----')[0]
                            # Try to reconstruct with proper newlines
                            private_key = '-----BEGIN PRIVATE KEY-----\n' + key_part.replace(' ', '\n') + '\n-----END PRIVATE KEY-----'
                    
                    # Ensure private key has proper format
                    if not private_key.startswith('-----BEGIN'):
                        st.error("❌ Private key format is incorrect in secrets!")
                        st.info("💡 Make sure the private_key includes the full key with BEGIN/END markers")
                        st.info(f"💡 Private key starts with: {private_key[:50]}...")
                        st.info(f"💡 Private key length: {original_length} characters")
                        st.stop()
                    
                    # Ensure it ends properly
                    if not private_key.endswith('-----END PRIVATE KEY-----'):
                        # Try to fix if it ends with \n or other characters
                        if private_key.endswith('-----END PRIVATE KEY-----\\n'):
                            private_key = private_key.replace('-----END PRIVATE KEY-----\\n', '-----END PRIVATE KEY-----\n')
                        elif not private_key.endswith('\n'):
                            private_key = private_key.rstrip() + '\n'
                    
                    # Validate the key structure
                    if '-----BEGIN PRIVATE KEY-----' not in private_key or '-----END PRIVATE KEY-----' not in private_key:
                        st.error("❌ Private key is missing BEGIN or END markers!")
                        st.info(f"💡 Key length: {len(private_key)} characters")
                        st.info(f"💡 First 100 chars: {private_key[:100]}")
                        st.info(f"💡 Last 100 chars: {private_key[-100:]}")
                        st.stop()
                    
                    creds_dict['private_key'] = private_key
                
                creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)
        except Exception as secrets_error:
            error_str = str(secrets_error)
            st.error(f"❌ Error parsing credentials from secrets: {error_str}")
            
            # Provide specific guidance based on error type
            if "Incorrect padding" in error_str or "padding" in error_str.lower():
                st.warning("⚠️ 'Incorrect padding' error detected!")
                st.error("This usually means the private_key is corrupted or incomplete.")
                
                # Try to get diagnostic info
                try:
                    if hasattr(st, 'secrets') and 'credentials' in st.secrets:
                        creds_dict = dict(st.secrets.credentials)
                        if 'private_key' in creds_dict:
                            pk = str(creds_dict['private_key'])
                            st.info(f"📏 Private key length: {len(pk)} characters")
                            st.info(f"📝 First 80 chars: `{pk[:80]}`")
                            st.info(f"📝 Last 80 chars: `{pk[-80:]}`")
                            if 'BEGIN' not in pk:
                                st.error("❌ Missing 'BEGIN' marker - key is corrupted!")
                            if 'END' not in pk:
                                st.error("❌ Missing 'END' marker - key is truncated!")
                except:
                    pass
                
                st.info("💡 **SOLUTION:**")
                st.info("1. Go to Streamlit Cloud → Settings → Secrets → Edit secrets")
                st.info("2. **DELETE everything** in the editor")
                st.info("3. Open `SECRETS_TO_PASTE.txt` in your project folder")
                st.info("4. Copy the **ENTIRE** file (Ctrl+A, Ctrl+C)")
                st.info("5. Paste into Streamlit secrets editor (Ctrl+V)")
                st.info("6. **VERIFY** the `private_key` line is all on ONE line (very long!)")
                st.info("7. Make sure it starts with `-----BEGIN PRIVATE KEY-----\n`")
                st.info("8. Make sure it ends with `-----END PRIVATE KEY-----\n\"`")
                st.info("9. Click Save")
            elif "Invalid JWT Signature" in error_str or "invalid_grant" in error_str:
                st.warning("⚠️ This usually means the private_key in secrets is not formatted correctly.")
                st.info("💡 Make sure the private_key includes `\\n` characters for newlines")
            else:
                st.info("💡 Check that all fields in secrets are correct, especially the private_key")
            
            st.info("📋 **Quick fix:** Delete all secrets, then copy-paste the entire content from `SECRETS_TO_PASTE.txt`")
            st.stop()
        
        # Fallback to credentials.json file (for local development)
        if creds is None:
            import os
            creds_file = 'credentials.json'
            if not os.path.exists(creds_file):
                st.error("❌ Credentials not found! Please set up Streamlit Secrets in Settings or add credentials.json file.")
                st.info("💡 Go to Streamlit Cloud → Settings → Secrets → Edit secrets")
                st.stop()
            creds = Credentials.from_service_account_file(creds_file, scopes=SCOPE)
        
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(SPREADSHEET_ID)
        return spreadsheet
    except Exception as e:
        error_msg = str(e)
        st.error(f"❌ Error connecting to Google Sheets: {error_msg}")
        
        if "Invalid JWT Signature" in error_msg or "invalid_grant" in error_msg:
            st.warning("⚠️ This usually means the private_key in secrets is not formatted correctly.")
            st.info("💡 Make sure the private_key includes `\\n` characters for newlines")
            st.info("💡 Example: `private_key = \"-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n\"`")
        else:
            st.info("💡 Make sure you've added secrets in Streamlit Cloud Settings")
        st.stop()

@st.cache_resource
def init_sheet():
    """Initialize the users sheet with headers if it doesn't exist"""
    try:
        spreadsheet = get_google_sheet()
        try:
            worksheet = spreadsheet.worksheet(USERS_SHEET)
            # Check if headers exist, if not add them
            if not worksheet.get('A1'):
                worksheet.append_row(['Email', 'Password', 'Name', 'Created At'])
        except gspread.exceptions.WorksheetNotFound:
            # Create the sheet if it doesn't exist
            worksheet = spreadsheet.add_worksheet(title=USERS_SHEET, rows=1000, cols=10)
            # Add headers
            worksheet.append_row(['Email', 'Password', 'Name', 'Created At'])
        
        return worksheet
    except Exception as e:
        st.error(f"Error initializing sheet: {e}")
        return None

def hash_password(password):
    """Hash password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def get_user_by_email(email):
    """Get user from Google Sheet by email"""
    try:
        worksheet = init_sheet()
        if not worksheet:
            return None
        
        records = worksheet.get_all_records()
        for record in records:
            if record.get('Email', '').lower() == email.lower():
                return record
        return None
    except Exception as e:
        st.error(f"Error getting user: {e}")
        return None

def create_user(email, password, name):
    """Create a new user in Google Sheet"""
    try:
        worksheet = init_sheet()
        if not worksheet:
            return False
        
        # Check if user already exists
        if get_user_by_email(email):
            return False
        
        # Add new user
        hashed_password = hash_password(password)
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        worksheet.append_row([email, hashed_password, name, created_at])
        return True
    except Exception as e:
        st.error(f"Error creating user: {e}")
        return False

def show_login():
    """Display login page"""
    st.title("🔐 Login")
    
    with st.form("login_form"):
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if not email or not password:
                st.error("Please enter both email and password!")
            else:
                user = get_user_by_email(email)
                
                if user and user.get('Password') == hash_password(password):
                    # Login successful
                    st.session_state.user = {
                        'email': user.get('Email'),
                        'name': user.get('Name', 'User')
                    }
                    st.session_state.page = 'dashboard'
                    st.rerun()
                else:
                    st.error("Invalid email or password!")
    
    st.markdown("---")
    st.markdown("Don't have an account?")
    if st.button("Register here"):
        st.session_state.page = 'register'
        st.rerun()

def show_register():
    """Display registration page"""
    st.title("📝 Create Account")
    
    with st.form("register_form"):
        name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password (min 6 characters)")
        submit = st.form_submit_button("Register")
        
        if submit:
            # Validation
            if not email or not password or not name:
                st.error("All fields are required!")
            elif '@' not in email:
                st.error("Please enter a valid email address!")
            elif len(password) < 6:
                st.error("Password must be at least 6 characters long!")
            else:
                if create_user(email, password, name):
                    st.success("Registration successful! Please login.")
                    st.session_state.page = 'login'
                    st.rerun()
                else:
                    st.error("Email already exists! Please login or use a different email.")
    
    st.markdown("---")
    st.markdown("Already have an account?")
    if st.button("Login here"):
        st.session_state.page = 'login'
        st.rerun()

def show_dashboard():
    """Display dashboard page"""
    if not st.session_state.user:
        st.session_state.page = 'login'
        st.rerun()
        return
    
    user = st.session_state.user
    
    st.title(f"Welcome, {user['name']}! 👋")
    st.markdown("You're successfully logged in to your dashboard")
    
    st.markdown("---")
    
    # User Information
    st.subheader("Account Information")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info(f"**Name:** {user['name']}")
    
    with col2:
        st.info(f"**Email:** {user['email']}")
    
    st.success("**Status:** ● Active")
    
    st.markdown("---")
    
    # Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Dashboard", "📊")
    with col2:
        st.metric("Authenticated", "✅")
    with col3:
        st.metric("Secure", "🔒")
    
    st.markdown("---")
    
    if st.button("Logout", type="primary"):
        st.session_state.user = None
        st.session_state.page = 'login'
        st.rerun()

# Initialize sheet on first run (only if not already initialized)
if 'sheet_initialized' not in st.session_state:
    try:
        # Check if secrets are available
        if hasattr(st, 'secrets') and 'credentials' in st.secrets:
            init_sheet()
            st.session_state.sheet_initialized = True
        else:
            # Secrets not set yet - show message but don't crash
            st.session_state.sheet_initialized = False
    except Exception as e:
        # Show error if secrets are set but connection fails
        if hasattr(st, 'secrets') and 'credentials' in st.secrets:
            st.error(f"❌ Error connecting to Google Sheets: {e}")
            st.info("💡 Check that your Google Sheet is shared with the service account email")
        st.session_state.sheet_initialized = False

# Show setup message if secrets not configured
if hasattr(st, 'secrets') and 'credentials' not in st.secrets:
    st.warning("⚠️ Streamlit Secrets not configured. Please add credentials in Settings → Secrets")
    st.info("See HOW_TO_ADD_SECRETS.md for instructions")
    st.stop()

# Main app logic
if st.session_state.user:
    show_dashboard()
elif st.session_state.page == 'register':
    show_register()
else:
    show_login()
