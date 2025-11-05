# 🚀 Streamlit Cloud Deployment - Step by Step

## Prerequisites Checklist
- [ ] Code is pushed to GitHub
- [ ] Google Cloud Project created
- [ ] Google Sheets API & Drive API enabled
- [ ] Service account created
- [ ] `credentials.json` downloaded
- [ ] Google Sheet shared with service account email

---

## Step 1: Convert Credentials to Streamlit Secrets Format

Run this command to generate the secrets format:

```bash
python convert_credentials.py
```

This will:
- Read your `credentials.json`
- Convert it to Streamlit Secrets TOML format
- Display it for you to copy
- Save it to `streamlit_secrets.txt` for reference

**Copy the entire output** (from `[credentials]` to the end).

---

## Step 2: Add Secrets to Streamlit Cloud

1. **Go to Streamlit Cloud**: https://share.streamlit.io
2. **Sign in** with your GitHub account
3. **If app exists**: Click on your app → **"⋮" (three dots)** → **"Settings"**
4. **If new app**: Follow Step 3 first, then come back to add secrets
5. Scroll down to **"Secrets"** section
6. Click **"Edit secrets"**
7. **Paste** the secrets you copied from Step 1
8. Click **"Save"**

⚠️ **Important**: The secrets are encrypted and secure. Never share them publicly.

---

## Step 3: Deploy Your App

### If this is a NEW app:

1. Go to https://share.streamlit.io
2. Click **"New app"**
3. **Connect repository**:
   - Select your GitHub account
   - Choose your repository
   - Select the branch (usually `main` or `master`)
4. **Configure app**:
   - **Main file path**: `app.py`
   - **App URL**: (optional, auto-generated)
5. Click **"Deploy"**
6. Wait for deployment (usually 1-2 minutes)

### If app already exists:

1. Go to your app dashboard
2. Click **"Manage app"** → **"Reboot app"** (if needed)
3. Or push new changes to GitHub - it will auto-deploy

---

## Step 4: Verify Google Sheet Access

**Before testing**, make sure your Google Sheet is shared:

1. Open your Google Sheet:
   https://docs.google.com/spreadsheets/d/1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I/edit

2. Click **"Share"** button (top right)

3. Add the service account email:
   - Find it in your `credentials.json` → `"client_email"` field
   - Or run `python convert_credentials.py` to see it

4. Set permission to **"Editor"**

5. **Uncheck** "Notify people" (optional)

6. Click **"Share"**

---

## Step 5: Test Your App

1. **Open your deployed app** (URL will be shown in Streamlit Cloud dashboard)

2. **Test Registration**:
   - Click "Register here"
   - Fill in: Name, Email, Password (min 6 chars)
   - Click "Register"
   - Should see success message

3. **Test Login**:
   - Enter your email and password
   - Click "Login"
   - Should see dashboard

4. **Verify in Google Sheet**:
   - Open your Google Sheet
   - Check if "users" sheet was created
   - Verify your user data is there

---

## Step 6: Troubleshooting

### ❌ "Credentials not found" error

**Solution**:
- Make sure you added secrets in Streamlit Cloud Settings
- Check that the secrets format is correct (should have `[credentials]` header)
- Verify `private_key` includes `\n` for newlines

### ❌ Permission denied errors

**Solution**:
- Make sure Google Sheet is shared with service account email
- Check that service account has "Editor" permissions
- Verify the email matches exactly (from `credentials.json`)

### ❌ App won't deploy

**Solution**:
- Check that `requirements.txt` is in the repository
- Verify `app.py` is in the root directory
- Check deployment logs in Streamlit Cloud for errors

### ❌ "Sheet not found" errors

**Solution**:
- The app will create the "users" sheet automatically
- Make sure service account has permission to create sheets
- Check that the spreadsheet ID is correct in `app.py`

---

## Quick Commands Reference

```bash
# Convert credentials to secrets format
python convert_credentials.py

# Test locally (optional)
streamlit run app.py

# Check if credentials exist
python verify_setup.py
```

---

## Security Best Practices

✅ **DO**:
- Use Streamlit Secrets for credentials
- Keep `credentials.json` out of GitHub (it's in `.gitignore`)
- Share Google Sheet only with service account email
- Regularly rotate service account keys

❌ **DON'T**:
- Commit `credentials.json` to GitHub
- Share secrets publicly
- Use service account keys in client-side code
- Give service account to unauthorized users

---

## Next Steps After Deployment

1. ✅ Test all functionality
2. ✅ Share app URL with users
3. ✅ Monitor usage in Google Sheet
4. ✅ Set up custom domain (optional)
5. ✅ Configure app settings (title, icon, etc.)

---

## Need Help?

- Check `STREAMLIT_SETUP.md` for detailed setup
- Review Streamlit Cloud logs for errors
- Verify Google Sheet permissions
- Test locally first with `streamlit run app.py`

