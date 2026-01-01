# GitHub App Configuration - Contruil Portfolio Deployer

**App ID:** 2573684  
**Client ID:** Iv23lieioBWFPlGHdAGm  
**Organization:** @Contruil-LLC  
**Status:** Configuration in progress

---

## Current Status

✅ **Private Key:** Added 2 hours ago  
⚠️ **IPv6 Warning:** Need to address IP allow list  
📝 **Configuration:** Complete remaining fields

---

## Recommended Configuration

### Basic Information

**GitHub App name:**
```
Contruil Portfolio Deployer
```
✅ Already set correctly

**Homepage URL:**
```
https://timothywheels.com
```
*Or:*
```
https://contruil.com
```

---

### Identifying and Authorizing Users

**Callback URL:**
```
https://api.contruil.com/github/callback
```
*For development/testing:*
```
http://localhost:8080/github/callback
```

**Settings:**
- ✅ **Expire user authorization tokens** - Check this (provides refresh tokens)
- ⚠️ **Request user authorization (OAuth) during installation** - Only if you need user identity
- ❌ **Enable Device Flow** - Usually not needed for CI/CD

---

### Post Installation

**Setup URL (optional):**
```
https://contruil.com/github/setup
```
*Or leave blank if not needed*

**Redirect on update:**
- ✅ **Check this** - Redirect users after installations are updated

---

### Webhook Configuration

**Important:** For Vercel deployments, you may not need a GitHub App webhook.

**Option 1: No Webhook (Recommended for Vercel)**
- ❌ **Uncheck "Active"** - If Vercel is connected via GitHub integration
- Vercel automatically deploys on push to GitHub
- No custom webhook needed

**Option 2: Custom Webhook (If Needed)**
- ✅ **Check "Active"** - If you need to receive GitHub events
- **Webhook URL:** `https://api.contruil.com/github/webhook`
- **Secret:** Generate with: `openssl rand -hex 32`
- ✅ **Enable SSL verification** - Keep checked (recommended)

**Current Status:**
- ✅ Active (if you need webhooks)
- ⚠️ Secret configured (if you've lost it, you can regenerate)

---

### Display Information

**Logo:**
- Use the GitHub App logos from `portfolio/github-app-logo.png` or `github-app-logo-simple.png`
- Upload via drag & drop
- Must be 512×512 PNG, under 1 MB

**Note:** If you see "File contents don't match the file extension", ensure the file is actually a PNG, not an SVG renamed to PNG.

---

### IP Allow Lists and IPv6

**GitHub Warning:** "GitHub is gradually rolling out IPv6. To prevent possible access interruptions with your GitHub App, please ensure you have added any necessary IPv6 addresses to your IP allow list."

**Recommendation:**

**Option 1: Skip IP Allow List (Easiest)**
- IP allow lists are **optional**
- You don't have to create entries
- Webhook secrets provide sufficient security
- Recommended for most use cases

**Option 2: Add IPv4 Entry (If You Have Static IP)**
- **Allow list value:** Your current public IP (find at https://whatismyipaddress.com/)
- **Name:** `Development Machine IPv4`
- **Enabled?:** ✅ Check

**Option 3: Add IPv6 Entry (If You Have IPv6)**
- **Allow list value:** Your IPv6 address (find with `curl -6 -s ifconfig.me`)
- **Name:** `Development Machine IPv6`
- **Enabled?:** ✅ Check

**Option 4: Allow All (Development Only)**
- **IPv4:** `0.0.0.0/0` (allows all IPv4)
- **IPv6:** `::/0` (allows all IPv6)
- **Name:** `Allow All (Development)`
- **Enabled?:** ✅ Check
- ⚠️ **Warning:** Less secure, only for development

**To Check Your IPv6:**
```bash
curl -6 -s ifconfig.me
# or
curl -6 -s icanhazip.com
```

**If You Don't Have IPv6:**
- You can ignore the warning
- GitHub will still work with IPv4
- The message is informational, not a requirement

---

## Quick Action Items

1. ✅ **Private Key:** Already added
2. 📝 **Homepage URL:** Set to `https://timothywheels.com` or `https://contruil.com`
3. 📝 **Callback URL:** Set if you need OAuth (optional for Vercel deployments)
4. 📝 **Webhook:** Decide if you need it (probably not for Vercel)
5. ⚠️ **IP Allow List:** Either skip it or add entries if you have static IPs
6. 📝 **Logo:** Upload from `portfolio/github-app-logo-simple.png`

---

## Security Notes

- ✅ **Private Key:** Already configured (SHA256: wSVEWoGIB4YdfZtjVd85CC3nACPo3FCZPBEkYUWca/Q=)
- ✅ **Client Secret:** Keep secure, never commit to git
- ✅ **Webhook Secret:** Configured (regenerate if lost)
- ⚠️ **IP Allow List:** Optional security layer

---

## For Vercel Deployments

**If you're using this GitHub App for Vercel deployments:**

1. **Vercel GitHub Integration** (Recommended):
   - Connect Vercel to your GitHub repo directly
   - No GitHub App webhook needed
   - Vercel automatically deploys on push

2. **Vercel Deploy Hooks** (Alternative):
   - Use deploy hooks to trigger deployments
   - No GitHub App webhook needed
   - See `portfolio/deploy-vercel.sh` for script

**You probably don't need:**
- ❌ GitHub App webhook (unless you're processing events)
- ❌ IP allow list (unless you have specific security requirements)
- ❌ OAuth callback (unless you need user identity)

---

## Next Steps

1. Fill in **Homepage URL**
2. Decide on **Webhook** (probably skip for Vercel)
3. Address **IPv6 warning** (skip or add entries)
4. Upload **Logo** (optional but recommended)
5. Save all changes

---

**Last Updated:** January 1, 2026

