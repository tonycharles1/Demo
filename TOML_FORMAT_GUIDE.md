# TOML Format Guide for Streamlit Secrets

## What is TOML?

TOML (Tom's Obvious Minimal Language) is the format used by Streamlit for secrets. It's similar to INI files but more structured.

## Basic TOML Rules:

1. **Sections** use square brackets: `[section_name]`
2. **Keys** and **values** use `=` sign: `key = "value"`
3. **Strings** must be in quotes: `"value"`
4. **No spaces** around `=` is optional, but recommended
5. **Comments** use `#`

## For Your Secrets:

Your secrets need to be in this format:

```toml
[credentials]
type = "service_account"
project_id = "your-project-id"
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "your-email@project.iam.gserviceaccount.com"
```

## Important Notes:

### ✅ CORRECT:
- `key = "value"` (with quotes for strings)
- `[section]` on its own line
- `\n` in strings represents a newline character

### ❌ INCORRECT:
- `key = value` (missing quotes for strings)
- `[section] key = "value"` (section and key on same line)
- Missing quotes around values

## Common Issues:

1. **Missing quotes**: `private_key = -----BEGIN...` ❌
   - Should be: `private_key = "-----BEGIN..."` ✅

2. **Wrong section format**: `credentials.type = "value"` ❌
   - Should be:
     ```toml
     [credentials]
     type = "value"
     ```
     ✅

3. **Special characters in private_key**: The `\n` characters are literal - they represent newlines in the key

## Your Current Format is Correct!

The format in `SECRETS_TO_PASTE.txt` is valid TOML. If you're getting a TOML format error, it might be because:

1. You accidentally modified the format while copying
2. Extra spaces or characters were added
3. The private_key line got broken across multiple lines

## Quick Fix:

Always copy the **entire block** from `SECRETS_TO_PASTE.txt` as-is, without modifications.

