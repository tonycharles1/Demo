# 🔍 Debugging Guide - App Not Working

## Quick Checklist

### ✅ Step 1: Check Streamlit Cloud Logs
1. Go to: https://share.streamlit.io
2. Click on your app
3. Click **"Manage app"** → **"Logs"**
4. Look for error messages

### ✅ Step 2: Verify Secrets Are Added
1. Go to your app → **Settings** → **Secrets**
2. Check if secrets are present
3. If empty, add them (see `HOW_TO_ADD_SECRETS.md`)

### ✅ Step 3: Verify Google Sheet Sharing
1. Open: https://docs.google.com/spreadsheets/d/1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I/edit
2. Click **"Share"**
3. Verify this email is added: `demo-app-sheets@plasma-geode-477309-f6.iam.gserviceaccount.com`
4. Permission should be **"Editor"**

---

## Common Errors & Solutions

### Error: "Credentials not found"
**Solution**: 
- Add secrets in Streamlit Cloud Settings
- Copy from `SECRETS_TO_PASTE.txt`

### Error: "Permission denied" or "Access denied"
**Solution**:
- Share Google Sheet with service account email
- Give "Editor" permissions

### Error: "Error installing requirements"
**Solution**:
- Check logs for specific package
- Verify `requirements.txt` exists in repo
- Check `runtime.txt` specifies Python 3.11

### Error: Blank page or nothing loads
**Possible causes**:
- Secrets not configured
- App crashed on startup
- Check logs for errors

### Error: "Worksheet not found"
**Solution**:
- App will create it automatically
- Make sure service account has permission to create sheets

---

## What the App Shows Now

After the latest fix, the app will show:
- ✅ Clear message if secrets are missing
- ✅ Clear message if Google Sheet connection fails
- ✅ Helpful instructions on how to fix

---

## Test Locally First

To test if the code works:

```bash
# Install dependencies
pip install -r requirements.txt

# Create .streamlit/secrets.toml with your credentials
# OR place credentials.json in project root

# Run the app
streamlit run app.py
```

---

## Still Not Working?

1. **Check the logs** - Most important step!
2. **Share the error message** from the logs
3. **Verify all setup steps**:
   - [ ] Secrets added in Streamlit Cloud
   - [ ] Google Sheet shared with service account
   - [ ] Requirements installed successfully
   - [ ] App deployed successfully

---

## Need More Help?

Share:
1. The exact error message from Streamlit Cloud logs
2. What you see when you visit the app URL
3. Screenshot if possible

This will help identify the exact issue!

