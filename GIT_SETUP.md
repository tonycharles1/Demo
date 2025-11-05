# Git Setup Instructions

## ✅ Commit Completed!

Your files have been committed locally. Now you need to push to GitHub.

---

## Option 1: Connect to Existing GitHub Repository

If you already have a GitHub repository:

1. **Get your repository URL** from GitHub (e.g., `https://github.com/yourusername/your-repo.git`)

2. **Add the remote**:
   ```bash
   git remote add origin https://github.com/yourusername/your-repo.git
   ```

3. **Push to GitHub**:
   ```bash
   git branch -M main
   git push -u origin main
   ```

---

## Option 2: Create New GitHub Repository

1. **Go to GitHub**: https://github.com/new

2. **Create a new repository**:
   - Repository name: `demo-app` (or any name)
   - Description: "Registration and Login System with Google Sheets"
   - Set to **Public** or **Private**
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)

3. **Copy the repository URL** (e.g., `https://github.com/yourusername/demo-app.git`)

4. **Add remote and push**:
   ```bash
   git remote add origin https://github.com/yourusername/demo-app.git
   git branch -M main
   git push -u origin main
   ```

---

## Quick Commands Reference

```bash
# Check current status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push

# View remote
git remote -v
```

---

## After Pushing to GitHub

1. ✅ Go to Streamlit Cloud: https://share.streamlit.io
2. ✅ Connect your GitHub repository
3. ✅ Deploy your app
4. ✅ Add secrets (see NEXT_STEPS.md)

---

## Note

If you get authentication errors when pushing:
- Use GitHub CLI: `gh auth login`
- Or use a Personal Access Token instead of password
- Or use SSH keys for authentication

