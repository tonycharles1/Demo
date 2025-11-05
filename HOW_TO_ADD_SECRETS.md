# 🔐 How to Add Streamlit Secrets - Step by Step

## What to Paste

Copy **EVERYTHING** from the file `SECRETS_TO_PASTE.txt` (open it in your editor) or copy this entire block:

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

---

## Step-by-Step Instructions

### Step 1: Open Streamlit Cloud
1. Go to: **https://share.streamlit.io**
2. Sign in with your GitHub account
3. Click on your app

### Step 2: Go to Settings
1. Click the **"⋮" (three dots)** menu next to your app
2. Click **"Settings"**

### Step 3: Find Secrets Section
1. Scroll down to the **"Secrets"** section
2. Click **"Edit secrets"** button

### Step 4: Paste the Secrets
1. **Copy the entire block above** (from `[credentials]` to the last line)
2. **Paste it** into the secrets editor
3. Make sure it includes:
   - The `[credentials]` header at the top
   - All the fields (type, project_id, private_key, etc.)
   - The entire private_key (it's very long - make sure you copy all of it)

### Step 5: Save
1. Click **"Save"** button
2. The app will automatically restart

---

## Important Notes

⚠️ **CRITICAL**: 
- Copy **EVERYTHING** - the entire block from `[credentials]` to the end
- Make sure the `private_key` includes all the lines (it's very long)
- Don't modify anything - paste it exactly as shown
- The `\n` characters in private_key are important - don't remove them

---

## Verify It Worked

After saving:
1. Go back to your app
2. The app should reload automatically
3. You should see the login page (not an error message)
4. Try registering a new account to test

---

## Still Having Issues?

If you see errors:
1. Check that you copied the entire block
2. Make sure `[credentials]` is at the top
3. Verify the private_key is complete (should be very long)
4. Check the logs: Manage app → Logs

