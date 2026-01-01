# Portfolio Deployment Guide

Quick guide to build, test, and deploy your portfolio website.

## Local Development

### Option 1: Python HTTP Server (Recommended)
```bash
cd /Users/timothywheels/Projects/portfolio
python3 server.py
```
Server will start on `http://localhost:8000` and automatically open your browser.

### Option 2: Simple Python Server
```bash
cd /Users/timothywheels/Projects/portfolio
python3 -m http.server 8000
```
Then open `http://localhost:8000/landing.html` in your browser.

### Option 3: Node.js (if installed)
```bash
cd /Users/timothywheels/Projects/portfolio
npx serve .
```

---

## Deployment Options

### Option 1: Netlify (Easiest - Recommended)

1. **Push to GitHub:**
   ```bash
   cd /Users/timothywheels/Projects/portfolio
   git init  # if not already a git repo
   git add .
   git commit -m "Initial portfolio deployment"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy via Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub account
   - Select your portfolio repository
   - Settings:
     - Build command: (leave empty - static site)
     - Publish directory: `.` (current directory)
   - Click "Deploy site"

3. **Custom Domain (Optional):**
   - Netlify Dashboard → Site settings → Domain management
   - Add custom domain: `timothywheels.com`
   - Configure DNS as instructed by Netlify

**Netlify will automatically:**
- Deploy on every git push
- Provide HTTPS certificate
- Handle redirects (configured in `netlify.toml`)

---

### Option 2: Vercel

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   cd /Users/timothywheels/Projects/portfolio
   vercel
   ```
   Follow the prompts. First deployment will ask for configuration.

3. **Production Deployment:**
   ```bash
   vercel --prod
   ```

4. **Git Integration (Automatic Deploys):**
   - Go to [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Vercel will auto-deploy on every push

**Vercel provides:**
- Automatic HTTPS
- Global CDN
- Preview deployments for PRs
- Custom domain support

---

### Option 3: GitHub Pages

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Deploy to GitHub Pages"
   git push
   ```

2. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` (or `master`)
   - Folder: `/` (root)
   - Click "Save"

3. **Custom Domain (Optional):**
   - In Pages settings, add custom domain
   - Add `CNAME` file to repo:
     ```bash
     echo "timothywheels.com" > CNAME
     git add CNAME
     git commit -m "Add custom domain"
     git push
     ```
   - Configure DNS: Add CNAME record pointing to `YOUR_USERNAME.github.io`

**GitHub Pages:**
- Free for public repos
- Auto-deploys on push
- HTTPS included
- URL: `https://YOUR_USERNAME.github.io/REPO_NAME`

---

### Option 4: Cloudflare Pages

1. **Push to GitHub** (same as above)

2. **Connect to Cloudflare Pages:**
   - Go to [dash.cloudflare.com](https://dash.cloudflare.com)
   - Pages → Create a project
   - Connect GitHub repository
   - Settings:
     - Framework preset: None (static)
     - Build command: (leave empty)
     - Build output directory: `.`
   - Click "Save and Deploy"

3. **Custom Domain:**
   - In Pages project → Custom domains
   - Add domain and follow DNS setup

---

## Pre-Deployment Checklist

- [ ] Test locally: `python3 server.py`
- [ ] Verify all links work (landing.html ↔ index.html)
- [ ] Check responsive design on mobile/tablet
- [ ] Verify email link works: `timothy@timothywheels.com`
- [ ] Test newsletter form (currently shows success, needs backend integration)
- [ ] Verify all external links (LinkedIn, Contruil) open correctly
- [ ] Check browser console for errors (F12 → Console)
- [ ] Validate HTML: [W3C Validator](https://validator.w3.org/)
- [ ] Test on multiple browsers (Chrome, Firefox, Safari)

---

## Post-Deployment

1. **Test live site:**
   - Visit deployed URL
   - Test all navigation links
   - Verify images/assets load
   - Check mobile responsiveness

2. **Analytics (Optional):**
   - Add Google Analytics or Plausible
   - Track page views and user behavior

3. **SEO (Optional):**
   - Submit sitemap to Google Search Console
   - Verify meta tags are correct
   - Check Open Graph previews

4. **Performance:**
   - Test with [PageSpeed Insights](https://pagespeed.web.dev/)
   - Optimize if needed (images, fonts, etc.)

---

## Quick Deploy Commands

```bash
# Netlify (after initial setup)
git add .
git commit -m "Update portfolio"
git push  # Auto-deploys on Netlify

# Vercel
vercel --prod

# Vercel Deploy Hook (trigger deployment via webhook)
curl -X POST "YOUR_DEPLOY_HOOK_URL"

# GitHub Pages (auto-deploys on push)
git push
```

---

## Vercel Deploy Hooks

Deploy hooks allow you to trigger deployments via HTTP POST requests without using the CLI.

### Creating a Deploy Hook

1. **Go to Vercel Dashboard:**
   - Visit: https://vercel.com/contruil-llc/portfolio/settings/deploy-hooks
   - Or: Project → Settings → Deploy Hooks

2. **Create New Hook:**
   - Click "Create Hook"
   - Name it (e.g., "Manual Deploy" or "Production Deploy")
   - Select branch: `main` (or your production branch)
   - Click "Create Hook"

3. **Copy the Hook URL:**
   - You'll get a URL like: `https://api.vercel.com/v1/integrations/deploy/...`
   - **Keep this URL secret** - anyone with it can trigger deployments

### Using the Deploy Hook

**Basic usage:**
```bash
curl -X POST "YOUR_DEPLOY_HOOK_URL"
```

**With response:**
```bash
curl -X POST "YOUR_DEPLOY_HOOK_URL" -v
```

**Save hook URL to file (for convenience):**
```bash
# Save your hook URL (replace with actual URL)
echo "YOUR_DEPLOY_HOOK_URL" > .vercel-deploy-hook

# Use it later
curl -X POST "$(cat .vercel-deploy-hook)"
```

**Add to .gitignore:**
```bash
echo ".vercel-deploy-hook" >> .gitignore
```

### Use Cases

- **CI/CD pipelines:** Trigger from GitHub Actions, GitLab CI, etc.
- **Automation scripts:** Deploy after content updates
- **Manual triggers:** Quick deploy without CLI
- **Webhooks:** Connect to other services (Zapier, n8n, etc.)

### Example: GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy to Vercel
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Vercel Deploy
        run: |
          curl -X POST "${{ secrets.VERCEL_DEPLOY_HOOK }}"
```

Add `VERCEL_DEPLOY_HOOK` as a GitHub secret with your hook URL.

---

## Troubleshooting

**404 on root URL:**
- Netlify: Check `netlify.toml` redirects
- Vercel: Check `vercel.json` routes
- GitHub Pages: May need `index.html` at root or adjust base path

**Styles not loading:**
- All styles are inline in `<style>` tags, so this shouldn't happen
- If using external CSS, check file paths are relative

**Links not working:**
- Use relative paths: `index.html` not `/index.html` (unless root domain)
- Check file names match exactly (case-sensitive on some servers)

---

## Support

For issues:
1. Check browser console (F12) for errors
2. Test locally first with `server.py`
3. Verify file paths and names
4. Check deployment platform logs

---

**Last Updated:** January 2025

