# 🚀 Streamlit Cloud Deployment - Quick Guide

## Step 1: Sign in to Streamlit Cloud

1. Go to: **https://share.streamlit.io**
2. Click **"Sign in"** 
3. Authorize with your **GitHub account** (tonycharles1)

---

## Step 2: Create New App

1. Click **"New app"** button
2. **Connect your repository**:
   - Select: **tonycharles1/Demo**
   - Branch: **main**
3. **Configure app**:
   - **Main file path**: `app.py`
   - **App URL**: (optional, auto-generated)
4. Click **"Deploy"**

⚠️ **Wait**: Don't add secrets yet - let the app deploy first, then we'll add secrets.

---

## Step 3: Add Streamlit Secrets

After the app deploys (even if it shows errors):

1. Go to your app dashboard
2. Click **"⋮" (three dots)** → **"Settings"**
3. Scroll to **"Secrets"** section
4. Click **"Edit secrets"**
5. **Paste this entire block**:

```toml
[credentials]
type = "service_account"
project_id = "plasma-geode-477309-f6"
private_key_id = "6efae5f7d772e6a1fa816e74102dfeaa3bbfd6bf"
private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDarQ+UpSPqYgp7\n+ecRiN/nHp49Hvb/r2zhnbUlqyyPXpInFNgTEbE3Tyo3poqSkVgwDYOntA+YY8KN\ns3lYUiE+/wxdHDWTGjMQMR/Q9X1NwLGgpbprKY+9sV/yz1wqeXFXXhjkaj0NZVng\noIGm35Rpac/zT74mqBU3wQEs+yAYrjZWsq6CNmcuv2EOI4R4CxsfipZ9N9041Ukq\njQ/yeoWp6cSmg8QAk1V+OP86crjEjbR+e70hN1cR3h4DZKCdKCe/Gdi+NUVHgQBk\nXgSFZ/rbJeM9yDEr0bps92CZjvkU0tUL/XJa6P1Zv3+pKQu8j7hHRjjl/00rLMSA\nbNQxc3H5AgMBAAECggEAIDsMxlh2zDeKGw7Q33VApySMpy6WskXtcu2XQweRSEpk\nmU0JsfnUGHZbHxu1Zff1OxPq2T+BYvElPlR7KKjmTI40CM89GELuzs6mxVpBj0G9\nDJQQv3W/QXLQ1Q16JKqEqZ9tZNFB0WUkU6bkpS9kBQt7An445SK2CeMxJKuY5foV\nmWur44K2ZrnzvLXw8hksXxrkKUQ0HhQxAL66/bRQhGaEr37DjtKbSJ3w42/kfIKN\nkIPJGoWeSty2LZOOBNsLnMhGLnD4V/eh8sDqG5Rb0duGj6DbItrPXtzY5VrcGnJE\nZeTv5SV/CkQMA8sqHEadr7b3N1xnoGypclTzD2Qp9wKBgQD7Vwbc2QQyA7Eg9q2J\n2pNzIxSZLQsDjsvRVHEtp/E8vmLA8bWjZkibUnwipTK9jNl9WHYeeepOF5aiTb9A\n6M6vhhm7FeLBxAwGvukFp5vNJHN9rKkp4xlAvAF/AFuhoU0mulrdxEGEWm0KYab1\nqCiyxwPhN9PMURYGUgN9Mq6IzwKBgQDeuv8Kpkc2kw4UPTV0Z+cjrcSubLIDwXvB\n8FOtsuhsMGSZTHrUMafyVjcTzdM7EIGAR7XiVR/TroxqOTzOWrragusuDonAHOgQ\najbq2A+Jf7+LSfpKAvRWnFldSwZhoiFOpBM/a7khraBJywjrdyT3GfgVp3mRBdz4\nl7+Ag/N6twKBgQDD9R4MocZ7mBVJtgmnKRs88WTl6BBmPbb7BfMXvZB/44/rDoin\nVN/W+YB/In1k+6O17nppWHQtXoa7FBLA8MH0Z4E4M+APYmJeAAp9tifq0TiaCzv4\nxG6z4eDou8a1RaV5RGID9Td/kWDibzBU5z6T5EZKGdSvv6iEVP0TZ6hcUQKBgCRR\nHVDhN+9gHwWRzWuDnZ6lsNI4Cvatz74Zr6s85sTtRxnv7H848YeEI0rpXq3czSDb\nkH6tHplndqHDX3TOOnVyr2I9IJzgmb5Dc1zrie0DlXniwBrdTHXq3G9n0kyNIR0v\nh6vpprAlHWOq5XNvY+mepGLzgdDxwcwPAjy0RzkVAoGBAJjqgsR0yjH17LqamxTR\neZWmm0okN83jSuFhw8NUuREo5e2fTVVC+tk3uF883vUwRrSD/QrTSbng+I/WBI81\no+1iuLqtM1hxEtmvQDy1Wk5yR6YvQ4UBN5nc+gVbCBFXap/75Mg/hCapOrLFJD9X\ncOCOrQtgOJPOVbj3srmgnyyE\n-----END PRIVATE KEY-----\n"
client_email = "demo-app-sheets@plasma-geode-477309-f6.iam.gserviceaccount.com"
client_id = "100429931721093948549"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/demo-app-sheets%40plasma-geode-477309-f6.iam.gserviceaccount.com"
```

6. Click **"Save"**
7. The app will automatically restart with new secrets

---

## Step 4: Share Google Sheet

**IMPORTANT**: Before testing, make sure your Google Sheet is shared!

1. Open: https://docs.google.com/spreadsheets/d/1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I/edit
2. Click **"Share"** button (top right)
3. Add email: **demo-app-sheets@plasma-geode-477309-f6.iam.gserviceaccount.com**
4. Set permission: **"Editor"**
5. Uncheck "Notify people"
6. Click **"Share"**

---

## Step 5: Test Your App

1. **Open your app URL** (shown in Streamlit Cloud dashboard)
2. **Register**: Click "Register here" → Fill form → Submit
3. **Login**: Enter email/password → Click "Login"
4. **Dashboard**: Should see welcome message
5. **Verify**: Check Google Sheet - "users" sheet should be created with your data

---

## Troubleshooting

### ❌ "Credentials not found" error
- ✅ Check secrets are added in Settings
- ✅ Verify secrets format matches exactly (including `[credentials]` header)
- ✅ Make sure private_key includes `\n` for newlines

### ❌ "Permission denied" errors
- ✅ Share Google Sheet with service account email
- ✅ Give "Editor" permissions
- ✅ Verify email matches exactly

### ❌ "Error installing requirements"
- ✅ Check that `requirements.txt` is in the repository
- ✅ View logs: Manage app → Logs
- ✅ See `TROUBLESHOOTING.md` for more help

### ❌ App won't deploy
- ✅ Check `app.py` is in root directory
- ✅ Verify repository is connected
- ✅ Check logs for specific errors

---

## Quick Links

- **Streamlit Cloud**: https://share.streamlit.io
- **Your Repository**: https://github.com/tonycharles1/Demo
- **Google Sheet**: https://docs.google.com/spreadsheets/d/1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I/edit

---

## ✅ Checklist

- [ ] Signed in to Streamlit Cloud
- [ ] App deployed
- [ ] Secrets added
- [ ] Google Sheet shared with service account
- [ ] Tested registration
- [ ] Tested login
- [ ] Verified data in Google Sheet

---

## 🎉 You're Done!

Your app should now be live on Streamlit Cloud! Share the URL with users.

