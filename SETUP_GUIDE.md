# Setup Guide - Google Sheets API Credentials

## Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click on the project dropdown at the top
3. Click "New Project"
4. Name it (e.g., "Demo App Sheets")
5. Click "Create"

## Step 2: Enable APIs

1. In your project, go to **"APIs & Services"** → **"Library"**
2. Search for **"Google Sheets API"** and click **"Enable"**
3. Search for **"Google Drive API"** and click **"Enable"**

## Step 3: Create Service Account

1. Go to **"APIs & Services"** → **"Credentials"**
2. Click **"Create Credentials"** → **"Service Account"**
3. Fill in:
   - **Service account name**: `demo-app-sheets` (or any name)
   - **Service account ID**: (auto-generated)
   - Click **"Create and Continue"**
4. Skip the optional steps and click **"Done"**

## Step 4: Create and Download Key

1. In the Credentials page, find your service account (it should be listed)
2. Click on the service account email
3. Go to the **"Keys"** tab
4. Click **"Add Key"** → **"Create new key"**
5. Select **"JSON"** format
6. Click **"Create"** - this will download a JSON file

## Step 5: Place Credentials File

1. Rename the downloaded JSON file to `credentials.json`
2. Move it to your project folder: `C:\Users\tonyc\OneDrive\Desktop\Demo App\`
3. Make sure it's in the same folder as `app.py`

## Step 6: Share Google Sheet with Service Account

1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I/edit
2. Click the **"Share"** button (top right)
3. Find the email address in your `credentials.json` file (look for `"client_email"` field)
   - It will look like: `something@something.iam.gserviceaccount.com`
4. Paste this email into the "Share" dialog
5. Give it **"Editor"** permissions
6. Click **"Send"** (uncheck "Notify people" if you want)

## Step 7: Run the Application

Once `credentials.json` is in place, run:

```bash
python app.py
```

The app will:
- Create a "users" sheet automatically if it doesn't exist
- Start the server at `http://localhost:5000`

## Quick Test

1. Open browser: `http://localhost:5000`
2. You'll be redirected to login
3. Click "Register here" to create an account
4. After registration, login and access the dashboard

---

**Troubleshooting:**
- If you get "Credentials file not found": Make sure `credentials.json` is in the project root
- If you get permission errors: Make sure you shared the sheet with the service account email
- If the sheet name is different: The app will create a "users" sheet automatically

