# How to Find Your Production Branch on GitHub

## On GitHub Website

### Method 1: Check the Default Branch
1. Go to your repository on GitHub
2. Look at the top of the file list
3. You'll see a dropdown showing the current branch (usually `main` or `master`)
4. **This is likely your production branch**

### Method 2: Check All Branches
1. On your repository page, click the branch dropdown (next to the green "Code" button)
2. Or go to: `https://github.com/YOUR_USERNAME/YOUR_REPO/branches`
3. You'll see all branches listed
4. Look for:
   - `main` (most common in new repos)
   - `master` (older repos)
   - `production` or `prod` (if explicitly named)
   - `gh-pages` (if using GitHub Pages)

### Method 3: Check Repository Settings
1. Go to: Repository → Settings → Branches
2. Look for "Default branch" - this is your production branch
3. Common defaults: `main`, `master`

## For Vercel Deploy Hook

**Most likely options:**
- ✅ `main` (most common - 90% of repos)
- ✅ `master` (older repos)
- ✅ `production` (if you explicitly created it)

## Quick Check

If you're not sure, try `main` first. Vercel will show an error if the branch doesn't exist, and you can try another branch name.

## What Vercel Expects

When you deployed earlier, Vercel linked to: `contruil-llc/portfolio`

Check that repository's default branch:
- Go to: `https://github.com/contruil-llc/portfolio`
- Look at the branch dropdown
- Use that branch name in the Vercel deploy hook form

---

**Pro Tip:** If you're unsure, just use `main` - it's the most common default branch name in modern GitHub repositories.

