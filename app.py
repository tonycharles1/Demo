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
        # Try to get credentials from Streamlit secrets (for Streamlit Cloud)
        if 'credentials' in st.secrets:
            creds_dict = dict(st.secrets.credentials)
            creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPE)
        else:
            # Fallback to credentials.json file (for local development)
            import os
            creds_file = 'credentials.json'
            if not os.path.exists(creds_file):
                st.error("❌ Credentials not found! Please set up Streamlit Secrets or add credentials.json file.")
                st.stop()
            creds = Credentials.from_service_account_file(creds_file, scopes=SCOPE)
        
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(SPREADSHEET_ID)
        return spreadsheet
    except Exception as e:
        st.error(f"Error connecting to Google Sheets: {e}")
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

# Initialize sheet on first run
try:
    init_sheet()
except Exception as e:
    st.warning(f"Could not initialize Google Sheet: {e}")

# Main app logic
if st.session_state.user:
    show_dashboard()
elif st.session_state.page == 'register':
    show_register()
else:
    show_login()
