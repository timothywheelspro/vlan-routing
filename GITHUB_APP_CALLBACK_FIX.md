# GitHub App OAuth Callback 404 Fix

**Issue:** 404 Not Found when GitHub redirects to callback URL  
**Error:** `openresty/1.27.1.2` - Route not found  
**Status:** Configuration mismatch between GitHub App and backend

---

## Problem Analysis

**Current Situation:**
- ✅ GitHub App is installed correctly
- ✅ OAuth handshake starts correctly
- ✅ DNS + SSL working (`api.contruil.com` responds)
- ✅ NGINX/OpenResty is running
- ❌ **Callback route doesn't exist** - `/github/callback` returns 404

**Error Details:**
```
URL: https://api.contruil.com/github/callback?code=...&installation_id=...
Response: 404 Not Found (openresty/1.27.1.2)
```

---

## Root Cause

The callback URL in GitHub App settings doesn't match your actual backend route.

**Most Likely Issues:**
1. **Path mismatch:** GitHub points to `/github/callback` but backend expects `/api/github/callback`
2. **Backend not deployed:** Route exists in code but service isn't running
3. **Reverse proxy routing:** NGINX/OpenResty not forwarding to correct upstream

---

## Step-by-Step Fix

### Step 1: Check Current GitHub App Callback URL

**Go to:**
```
GitHub → Settings → Developer Settings → GitHub Apps → Contruil Portfolio Deployer
```

**Check:**
- **Callback URL:** What does it currently say?
- **Webhook URL:** What does it currently say?

**Common Configurations:**
- ❌ `https://api.contruil.com/github/callback` (missing `/api` prefix)
- ✅ `https://api.contruil.com/api/github/callback` (with `/api` prefix)
- ✅ `https://api.contruil.com/v1/github/callback` (with `/v1` prefix)

---

### Step 2: Identify Your Backend Route

**Questions to Answer:**

1. **What backend framework are you using?**
   - FastAPI
   - Django
   - Node/Express
   - Laravel
   - Other

2. **What is the actual route path in your code?**
   ```python
   # FastAPI example
   @app.get("/api/github/callback")
   # or
   @app.get("/github/callback")
   # or
   @app.get("/v1/github/callback")
   ```

3. **Is your backend service running?**
   - Check if the API service is deployed
   - Verify the route is accessible

4. **What is your NGINX/OpenResty routing config?**
   - Does it forward `/github/callback` to the backend?
   - Does it require `/api` prefix?

---

### Step 3: Fix the Mismatch

**Option A: Update GitHub App Callback URL**

If your backend route is `/api/github/callback`:
1. Go to GitHub App settings
2. Change **Callback URL** to: `https://api.contruil.com/api/github/callback`
3. Save

**Option B: Update Backend Route**

If GitHub is pointing to `/github/callback`:
1. Update your backend code to match
2. Deploy the updated backend
3. Verify the route works

**Option C: Update NGINX/OpenResty Config**

If you need to route `/github/callback` to `/api/github/callback`:
```nginx
location /github/callback {
    proxy_pass http://backend/api/github/callback;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

---

## Recommended Configuration

**For Most Cases:**

**GitHub App Settings:**
- **Callback URL:** `https://api.contruil.com/api/github/callback`
- **Webhook URL:** `https://api.contruil.com/api/github/webhook` (if needed)

**Backend Route:**
```python
# FastAPI example
@app.get("/api/github/callback")
async def github_callback(code: str, installation_id: str):
    # Handle OAuth callback
    pass
```

---

## Verification Steps

1. **Check GitHub App Settings:**
   - Verify callback URL matches backend route
   - Note the exact path (case-sensitive)

2. **Test Backend Route:**
   ```bash
   curl https://api.contruil.com/api/github/callback
   # Should return something (not 404)
   ```

3. **Check NGINX/OpenResty Logs:**
   ```bash
   # Check if requests are reaching the backend
   tail -f /var/log/nginx/access.log
   ```

4. **Re-run Install Flow:**
   - Remove app installation (if needed)
   - Start new installation
   - Should redirect to success page, not 404

---

## Quick Diagnostic Commands

**Check if route exists:**
```bash
# Test the callback URL directly
curl -I https://api.contruil.com/github/callback
curl -I https://api.contruil.com/api/github/callback
```

**Check backend service:**
```bash
# If backend is running locally
curl http://localhost:8000/api/github/callback
```

**Check NGINX config:**
```bash
# View routing configuration
cat /etc/nginx/sites-available/api.contruil.com
# or
cat /etc/nginx/conf.d/api.conf
```

---

## Next Steps

**To get precise help, provide:**

1. **Current GitHub App Callback URL:**
   ```
   (paste from GitHub settings - no secrets)
   ```

2. **Backend Framework:**
   ```
   FastAPI / Django / Node / Laravel / Other
   ```

3. **Backend Route Path:**
   ```python
   # Paste your actual route definition
   @app.get("/...")
   ```

4. **Backend Deployment Status:**
   ```
   Is the API service running? Where is it deployed?
   ```

5. **NGINX/OpenResty Config:**
   ```
   (if you have access to routing config)
   ```

---

## Common Solutions

### Solution 1: Add `/api` Prefix

**GitHub App:**
- Change callback URL to: `https://api.contruil.com/api/github/callback`

**Backend:**
- Ensure route is: `/api/github/callback`

### Solution 2: Remove `/api` Prefix

**GitHub App:**
- Change callback URL to: `https://api.contruil.com/github/callback`

**Backend:**
- Change route to: `/github/callback`

### Solution 3: Deploy Backend

**If backend isn't deployed:**
- Deploy the API service
- Ensure the callback route is implemented
- Verify the service is accessible

---

## For Vercel Deployments

**If you're using Vercel for the backend:**

1. **Check Vercel Project Settings:**
   - Verify the project is deployed
   - Check the deployment URL

2. **Update GitHub App:**
   - Use Vercel deployment URL: `https://your-project.vercel.app/api/github/callback`

3. **Or Use Custom Domain:**
   - Configure `api.contruil.com` in Vercel
   - Use: `https://api.contruil.com/api/github/callback`

---

**Status:** ✅ Backend route implementation created - Ready for deployment

---

## Implementation Created

**FastAPI callback handler created at:** `api/github_callback.py`

**Route:** `/api/github/callback`

**Features:**
- ✅ OAuth code exchange for access token
- ✅ Error handling and redirects
- ✅ Installation ID capture
- ✅ Health check endpoints
- ✅ CORS configuration

**Next Steps:**
1. Deploy the FastAPI app to `api.contruil.com`
2. Set environment variables (GITHUB_CLIENT_SECRET, etc.)
3. Update GitHub App callback URL to: `https://api.contruil.com/api/github/callback`
4. Test the OAuth flow

