"""
Helper script to convert credentials.json to Streamlit Secrets format
This will help you copy-paste the secrets into Streamlit Cloud
"""
import json
import os

def convert_to_streamlit_secrets():
    """Convert credentials.json to Streamlit Secrets TOML format"""
    creds_file = 'credentials.json'
    
    if not os.path.exists(creds_file):
        print("[X] ERROR: credentials.json not found!")
        print("Please make sure credentials.json is in the current directory.")
        return
    
    try:
        with open(creds_file, 'r') as f:
            creds = json.load(f)
        
        print("=" * 60)
        print("Streamlit Secrets Configuration")
        print("=" * 60)
        print()
        print("Copy the following and paste it into Streamlit Cloud Secrets:")
        print()
        print("-" * 60)
        print()
        
        # Format as TOML
        toml_output = f"""[credentials]
type = "{creds.get('type', 'service_account')}"
project_id = "{creds.get('project_id', '')}"
private_key_id = "{creds.get('private_key_id', '')}"
private_key = "{creds.get('private_key', '').replace(chr(10), '\\n')}"
client_email = "{creds.get('client_email', '')}"
client_id = "{creds.get('client_id', '')}"
auth_uri = "{creds.get('auth_uri', '')}"
token_uri = "{creds.get('token_uri', '')}"
auth_provider_x509_cert_url = "{creds.get('auth_provider_x509_cert_url', '')}"
client_x509_cert_url = "{creds.get('client_x509_cert_url', '')}"
"""
        
        print(toml_output)
        print("-" * 60)
        print()
        print("[*] Instructions:")
        print("1. Copy the entire output above (from [credentials] to the end)")
        print("2. Go to your Streamlit Cloud app -> Settings -> Secrets")
        print("3. Click 'Edit secrets'")
        print("4. Paste the copied content")
        print("5. Click 'Save'")
        print()
        print("[OK] Service Account Email:", creds.get('client_email', ''))
        print("   Make sure your Google Sheet is shared with this email!")
        print()
        
        # Also save to a file for reference
        output_file = 'streamlit_secrets.txt'
        with open(output_file, 'w') as f:
            f.write(toml_output)
        
        print(f"[*] Also saved to: {output_file}")
        print("   (You can delete this file after copying to Streamlit Cloud)")
        
    except json.JSONDecodeError:
        print("[X] ERROR: credentials.json is not valid JSON")
    except Exception as e:
        print(f"[X] ERROR: {e}")

if __name__ == '__main__':
    convert_to_streamlit_secrets()

