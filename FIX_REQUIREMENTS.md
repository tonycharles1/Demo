# Fixing Requirements Installation Error

## Issue
Streamlit Cloud is showing "Error installing requirements" error.

## Solutions Applied

### Solution 1: Updated with Version Constraints ✅
Updated `requirements.txt` with version constraints for better compatibility.

### Solution 2: Exact Versions ✅
Pinned to exact versions known to work with Streamlit Cloud:
- `streamlit==1.28.1`
- `gspread==5.12.0`
- `google-auth==2.23.4`
- `google-auth-oauthlib==1.1.0`
- `google-auth-httplib2==0.1.1`

## Next Steps

1. **Wait for auto-deploy**: Streamlit Cloud should automatically redeploy after the push
2. **Check logs**: Go to "Manage app" → "Logs" to see if installation succeeds
3. **If still failing**: Check the specific error in the logs

## Common Issues

### Issue: Package conflicts
**Solution**: The exact versions above should resolve this

### Issue: Missing dependencies
**Solution**: All required packages are listed

### Issue: Python version
**Solution**: `runtime.txt` specifies Python 3.11

## If Still Not Working

Check the logs for specific error messages:
1. Go to Streamlit Cloud dashboard
2. Click "Manage app" → "Logs"
3. Look for the specific package that's failing
4. Share the error message for further debugging

## Alternative: Minimal Requirements

If the above doesn't work, try this minimal version:

```txt
streamlit
gspread
google-auth
```

Then add other packages one by one.

