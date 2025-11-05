# Quick Setup Guide - Google Sheets API

## 🚀 Fast Setup (5 minutes)

### Step 1: Create Project & Enable APIs
**Direct Links:**
- [Google Cloud Console](https://console.cloud.google.com/)
- [Create New Project](https://console.cloud.google.com/projectcreate)
- [Enable Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com)
- [Enable Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com)

**Steps:**
1. Click "Create New Project" link above
2. Name it: `demo-app-sheets` → Click "Create"
3. Wait for project creation (30 seconds)
4. Enable Google Sheets API (click link above → Select your project → Enable)
5. Enable Google Drive API (click link above → Select your project → Enable)

---

### Step 2: Create Service Account
**Direct Link:**
- [Create Service Account](https://console.cloud.google.com/apis/credentials/serviceaccountkey)

**Steps:**
1. Click the link above
2. Select your project from dropdown
3. Click "Create Service Account" at top
4. Fill in:
   - Service account name: `demo-app-sheets`
   - Service account ID: (auto-filled)
   - Click "Create and Continue"
5. Skip optional steps → Click "Done"
6. You'll see a service account listed

---

### Step 3: Create & Download Key
**Steps:**
1. Click on the service account email you just created
2. Go to "Keys" tab
3. Click "Add Key" → "Create new key"
4. Select **JSON** format
5. Click "Create" → File downloads automatically

---

### Step 4: Place Credentials File
**Steps:**
1. Find the downloaded JSON file (usually in Downloads folder)
2. Copy it to: `C:\Users\tonyc\OneDrive\Desktop\Demo App\`
3. Rename it to: `credentials.json`
4. Make sure it's in the same folder as `app.py`

---

### Step 5: Share Google Sheet
**Direct Link:**
- [Your Google Sheet](https://docs.google.com/spreadsheets/d/1S2TjqfMPAcOh8vFcaNrzysXLjKMk89jWI_lBlo-Et6I/edit)

**Steps:**
1. Open `credentials.json` in a text editor
2. Find the `"client_email"` field (looks like: `xxx@xxx.iam.gserviceaccount.com`)
3. Copy that email address
4. Open your Google Sheet (link above)
5. Click "Share" button (top right)
6. Paste the service account email
7. Set permission to **"Editor"**
8. Uncheck "Notify people"
9. Click "Share"

---

### Step 6: Verify Setup
Run this command to verify everything is set up correctly:

```bash
python verify_setup.py
```

If you see ✅ checkmarks, you're ready!

---

### Step 7: Run the App
```bash
python app.py
```

Then open: http://localhost:5000

---

## 🆘 Need Help?

**If credentials.json is missing:**
- Make sure you downloaded the JSON key from Step 3
- Check it's renamed to exactly `credentials.json`
- Verify it's in the same folder as `app.py`

**If you get permission errors:**
- Run `python verify_setup.py` to get the service account email
- Make sure you shared the Google Sheet with that email
- Give it "Editor" permissions (not just "Viewer")

**If APIs are not enabled:**
- Go back to Step 1 and enable both APIs
- Wait a few minutes for changes to propagate

