# ⚠️ SECURITY: Remove credentials.json from GitHub

## Critical Issue

Your `credentials.json` file is visible in your GitHub repository. This is a **security risk** because anyone can see your Google service account credentials.

## Immediate Action Required

### Option 1: Remove from GitHub (Recommended)

1. **Go to your repository**: https://github.com/tonycharles1/Demo
2. **Click on `credentials.json`**
3. **Click the trash icon** (Delete this file)
4. **Commit the deletion**

### Option 2: Remove from Git History (More Secure)

If you want to completely remove it from history:

```bash
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch credentials.json" --prune-empty --tag-name-filter cat -- --all
git push origin --force --all
```

**⚠️ Warning**: This rewrites git history. Only do this if you're the only one working on the repo.

## Next Steps (CRITICAL)

Since your credentials were exposed, you should:

1. **Rotate/Delete the exposed service account**:
   - Go to Google Cloud Console
   - Delete the old service account
   - Create a new one
   - Download new credentials

2. **Update Streamlit Secrets**:
   - Use the new credentials in Streamlit Cloud
   - Remove old secrets

3. **Share Google Sheet with NEW service account**:
   - Remove old service account access
   - Add new service account email

## Prevention

✅ `credentials.json` is already in `.gitignore` (good!)
✅ Never commit credentials to GitHub
✅ Always use Streamlit Secrets for production

## Current Status

- ✅ Local: `credentials.json` is ignored (not tracked)
- ⚠️ GitHub: File still exists in repository (needs removal)
- ✅ `.gitignore`: Properly configured

