# Troubleshooting Streamlit Cloud Deployment

## Error: "Error installing requirements"

### Solution 1: Simplified Requirements (Already Applied)
The `requirements.txt` has been updated to use the latest compatible versions without strict version pins.

### Solution 2: Check Streamlit Cloud Logs
1. Go to your Streamlit Cloud app
2. Click **"Manage app"** → **"Logs"**
3. Look for specific error messages
4. Common issues:
   - Package version conflicts
   - Missing dependencies
   - Python version incompatibility

### Solution 3: Verify requirements.txt Format
Make sure `requirements.txt`:
- Has no empty lines at the end
- Uses proper package names (case-sensitive)
- One package per line

### Solution 4: Try Pin Specific Versions
If the latest versions don't work, try pinning to known working versions:

```txt
streamlit==1.28.1
gspread==5.12.0
google-auth==2.23.4
google-auth-oauthlib==1.1.0
google-auth-httplib2==0.1.1
```

### Solution 5: Check Python Version
Streamlit Cloud uses Python 3.11 by default. If needed, create `runtime.txt`:

```txt
python-3.11
```

(Already created for you)

---

## Common Errors and Fixes

### "Module not found" errors
- Check all imports in `app.py` match packages in `requirements.txt`
- Make sure package names are correct (case-sensitive)

### "Credentials not found"
- Add secrets in Streamlit Cloud Settings
- Verify secrets format matches TOML structure

### "Permission denied" errors
- Share Google Sheet with service account email
- Give "Editor" permissions

### "Worksheet not found"
- App will create "users" sheet automatically
- Make sure service account has permission to create sheets

---

## Step-by-Step Debugging

1. **Check Logs**: Streamlit Cloud → Manage app → Logs
2. **Test Locally**: Run `streamlit run app.py` locally first
3. **Verify Secrets**: Make sure secrets are added correctly
4. **Check Dependencies**: Ensure all packages are in requirements.txt
5. **Verify File Structure**: 
   - `app.py` in root directory
   - `requirements.txt` in root directory
   - No syntax errors in Python files

---

## If Still Not Working

1. **Clear Cache**: Streamlit Cloud → Manage app → Reboot app
2. **Check GitHub**: Make sure latest code is pushed to GitHub
3. **Try Minimal Version**: Start with just `streamlit` in requirements.txt, then add packages one by one
4. **Contact Support**: Streamlit Community Forum or check Streamlit Cloud status

