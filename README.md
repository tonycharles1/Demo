# Registration and Login System with Google Sheets

A Streamlit application that uses Google Sheets as a database for user registration and login functionality.

## Features

- ✅ User Registration
- ✅ User Login
- ✅ Secure Password Hashing
- ✅ Session Management
- ✅ Beautiful Dashboard
- ✅ Google Sheets Integration
- ✅ Streamlit Cloud Ready

## Quick Start

### For Streamlit Cloud Deployment

1. **Set up Streamlit Secrets** (see `STREAMLIT_SETUP.md`)
2. **Share your Google Sheet** with the service account email
3. **Deploy to Streamlit Cloud**
4. **Done!** 🎉

### For Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up credentials:
   - Option A: Create `.streamlit/secrets.toml` (see `.streamlit/secrets.toml.example`)
   - Option B: Place `credentials.json` in project root

3. Run the app:
```bash
streamlit run app.py
```

## Google Sheets API Setup

See `STREAMLIT_SETUP.md` for detailed instructions on:
- Setting up Google Cloud Project
- Creating service account
- Configuring Streamlit Secrets
- Sharing Google Sheet

## Google Sheet Configuration

- **Sheet ID**: `1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I`
- **Sheet Name**: `users` (created automatically)

## Project Structure

```
Demo App/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── credentials.json            # Google service account credentials (local only)
├── .streamlit/
│   └── secrets.toml           # Streamlit secrets (for local testing)
├── README.md                  # This file
└── STREAMLIT_SETUP.md         # Detailed setup guide
```

## Security Notes

- ⚠️ Never commit `credentials.json` or `.streamlit/secrets.toml` to GitHub
- ⚠️ Use Streamlit Secrets for production deployments
- ⚠️ Passwords are hashed using SHA256

## Troubleshooting

- **"Credentials not found"**: Check Streamlit Secrets or credentials file
- **Permission errors**: Share Google Sheet with service account email
- **Sheet not found**: The app creates the "users" sheet automatically
