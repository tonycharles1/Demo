"""
Script to verify Google Sheets API setup
Run this after you've downloaded credentials.json
"""
import os
import json

def verify_setup():
    print("=" * 60)
    print("Google Sheets API Setup Verification")
    print("=" * 60)
    print()
    
    # Check if credentials.json exists
    creds_file = 'credentials.json'
    if not os.path.exists(creds_file):
        print("[X] ERROR: credentials.json not found!")
        print()
        print("Please follow these steps:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a project and enable Google Sheets API & Drive API")
        print("3. Create a service account and download JSON key")
        print("4. Save it as 'credentials.json' in this folder")
        print()
        return False
    
    print("[OK] credentials.json found!")
    print()
    
    # Check credentials.json structure
    try:
        with open(creds_file, 'r') as f:
            creds = json.load(f)
        
        # Extract service account email
        client_email = creds.get('client_email', '')
        project_id = creds.get('project_id', '')
        
        if client_email:
            print(f"[OK] Service Account Email: {client_email}")
            print()
            print("[!] IMPORTANT: Share your Google Sheet with this email!")
            print("   1. Open: https://docs.google.com/spreadsheets/d/1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I/edit")
            print("   2. Click 'Share' button")
            print(f"   3. Add this email: {client_email}")
            print("   4. Give it 'Editor' permissions")
            print()
        else:
            print("[!] WARNING: Could not find client_email in credentials.json")
            print()
        
        if project_id:
            print(f"[OK] Project ID: {project_id}")
            print()
        
        # Test Google Sheets connection
        print("Testing Google Sheets connection...")
        try:
            import gspread
            from google.oauth2.service_account import Credentials
            
            SCOPE = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/drive"
            ]
            
            SPREADSHEET_ID = '1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I'
            
            creds_obj = Credentials.from_service_account_file(creds_file, scopes=SCOPE)
            client = gspread.authorize(creds_obj)
            
            try:
                spreadsheet = client.open_by_key(SPREADSHEET_ID)
                print(f"[OK] Successfully connected to Google Sheet: {spreadsheet.title}")
                print()
                
                # Check if users sheet exists
                try:
                    worksheet = spreadsheet.worksheet('users')
                    print("[OK] 'users' sheet exists")
                except:
                    print("[!] 'users' sheet not found - will be created automatically")
                
                print()
                print("=" * 60)
                print("[OK] Setup is complete! You can now run: python app.py")
                print("=" * 60)
                return True
                
            except Exception as e:
                print(f"[X] ERROR: Could not access Google Sheet")
                print(f"   Error: {str(e)}")
                print()
                print("This usually means:")
                print("1. The sheet hasn't been shared with the service account email")
                print(f"2. Share the sheet with: {client_email}")
                print("3. Give it 'Editor' permissions")
                return False
                
        except ImportError:
            print("[X] ERROR: Required packages not installed")
            print("   Run: python -m pip install -r requirements.txt")
            return False
        except Exception as e:
            print(f"[X] ERROR: {str(e)}")
            return False
            
    except json.JSONDecodeError:
        print("[X] ERROR: credentials.json is not valid JSON")
        print("   Please check that you downloaded the correct file")
        return False
    except Exception as e:
        print(f"[X] ERROR: {str(e)}")
        return False

if __name__ == '__main__':
    verify_setup()

