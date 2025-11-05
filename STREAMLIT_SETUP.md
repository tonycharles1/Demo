# Streamlit Cloud Setup Guide

## Step 1: Set up Streamlit Secrets

Since you're using Streamlit Cloud, you need to add your Google Sheets credentials as Streamlit Secrets.

### Option A: Using Streamlit Cloud Dashboard

1. Go to your Streamlit Cloud app dashboard
2. Click on your app → **"⋮" (three dots)** → **"Settings"**
3. Scroll down to **"Secrets"** section
4. Click **"Edit secrets"**
5. Copy the entire contents of your `credentials.json` file and paste it in this format:

```toml
[credentials]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYour private key here\n-----END PRIVATE KEY-----\n"
client_email = "your-service-account@your-project.iam.gserviceaccount.com"
client_id = "your-client-id"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account%40your-project.iam.gserviceaccount.com"
```

6. **Important**: Make sure the `private_key` includes the `\n` characters for newlines
7. Click **"Save"**

### Option B: Using .streamlit/secrets.toml (for local testing)

1. Create a folder named `.streamlit` in your project root
2. Create a file named `secrets.toml` inside `.streamlit` folder
3. Copy the format from `.streamlit/secrets.toml.example`
4. Fill in your credentials from `credentials.json`

## Step 2: Share Google Sheet

Make sure your Google Sheet is shared with the service account email:

1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I/edit
2. Click **"Share"** button
3. Add the service account email (from `credentials.json` → `client_email`)
4. Give it **"Editor"** permissions
5. Click **"Share"**

## Step 3: Deploy to Streamlit Cloud

1. Push your code to GitHub (if not already done)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **"New app"**
5. Select your repository and branch
6. Set Main file path to: `app.py`
7. Click **"Deploy"**

## Step 4: Test the App

Once deployed:
1. Try registering a new account
2. Login with your credentials
3. Check your Google Sheet - the "users" sheet should be created automatically

## Troubleshooting

- **"Credentials not found"**: Make sure you've added secrets in Streamlit Cloud settings
- **Permission errors**: Make sure the Google Sheet is shared with the service account email
- **Sheet not found**: The app will create a "users" sheet automatically on first use

## Local Testing

To test locally before deploying:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Make sure you have `.streamlit/secrets.toml` set up for local testing, or have `credentials.json` in the project root.

