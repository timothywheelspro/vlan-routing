# GitHub App Backend Route Diagnostic

**Purpose:** Identify the correct callback URL path for your GitHub App  
**Issue:** 404 error at `https://api.contruil.com/github/callback`

---

## Step 1: Determine If You Have a Backend

### Check 1: Is `api.contruil.com` Actually Deployed?

**Test the domain:**
```bash
# Test if the domain responds
curl -I https://api.contruil.com
curl -I https://api.contruil.com/health
curl -I https://api.contruil.com/api/health
```

**What to look for:**
- ✅ **200 OK** = Backend is running
- ❌ **404 Not Found** = Backend not deployed or wrong path
- ❌ **502 Bad Gateway** = Backend exists but not responding
- ❌ **Connection refused** = Domain not configured

---

### Check 2: What Framework/Platform Are You Using?

**Options:**
1. **Vercel Serverless Functions** (Next.js/API routes)
2. **FastAPI** (Python backend)
3. **Django** (Python backend)
4. **Express/Node.js** (JavaScript backend)
5. **Laravel** (PHP backend)
6. **No backend** (just using Vercel GitHub integration)

**If you're using Vercel:**
- You might not need a callback URL at all
- Vercel's GitHub integration handles OAuth automatically
- Uncheck "Request user authorization (OAuth) during installation"

---

## Step 2: Test Different Route Paths

**Run these tests to find which path exists:**

```bash
# Test common callback paths
echo "Testing callback routes..."
curl -I https://api.contruil.com/github/callback
curl -I https://api.contruil.com/api/github/callback
curl -I https://api.contruil.com/v1/github/callback
curl -I https://api.contruil.com/webhook/github/callback
curl -I https://api.contruil.com/auth/github/callback
```

**The one that returns 200 OK (not 404) is your correct path.**

---

## Step 3: Check Your Codebase for Route Definitions

### If Using Vercel (Next.js API Routes)

**Look for files like:**
- `pages/api/github/callback.js` or `.ts`
- `app/api/github/callback/route.js` or `.ts`
- `api/github/callback.js`

**Route would look like:**
```javascript
// pages/api/github/callback.js
export default async function handler(req, res) {
  // Handle callback
}
```

**Callback URL would be:**
```
https://api.contruil.com/api/github/callback
```

---

### If Using FastAPI

**Look for files like:**
- `main.py`
- `app.py`
- `api/routes/github.py`

**Route would look like:**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/github/callback")
async def github_callback(code: str, installation_id: str):
    # Handle callback
    pass
```

**Callback URL would be:**
```
https://api.contruil.com/api/github/callback
```

---

### If Using Express/Node.js

**Look for files like:**
- `server.js`
- `app.js`
- `routes/github.js`

**Route would look like:**
```javascript
app.get('/api/github/callback', (req, res) => {
  // Handle callback
});
```

**Callback URL would be:**
```
https://api.contruil.com/api/github/callback
```

---

## Step 4: Check NGINX/OpenResty Configuration

**If you're using a reverse proxy, check routing:**

**Common NGINX patterns:**
```nginx
# Pattern 1: Direct routing
location /github/callback {
    proxy_pass http://backend:8000/github/callback;
}

# Pattern 2: With /api prefix
location /api/github/callback {
    proxy_pass http://backend:8000/api/github/callback;
}

# Pattern 3: Rewrite
location /github/callback {
    rewrite ^/github/callback /api/github/callback break;
    proxy_pass http://backend:8000;
}
```

**Your NGINX config location:**
- `/etc/nginx/sites-available/api.contruil.com`
- `/etc/nginx/conf.d/api.conf`
- Vercel dashboard (if using Vercel)

---

## Step 5: Quick Fix Options

### Option A: If You Don't Have a Backend (Vercel Only)

**Solution:** Disable OAuth callback

1. Go to GitHub App settings
2. **Uncheck:** "Request user authorization (OAuth) during installation"
3. **Leave Callback URL blank** or set to: `https://contruil.com`
4. Use Vercel's GitHub integration instead

**This is the simplest solution if you're just deploying to Vercel.**

---

### Option B: If Backend Uses `/api/github/callback`

**Solution:** Update GitHub App callback URL

1. Go to GitHub App settings
2. Change **Callback URL** to: `https://api.contruil.com/api/github/callback`
3. Save

---

### Option C: If Backend Uses `/github/callback` (No `/api`)

**Solution:** Verify backend route exists

1. Test: `curl https://api.contruil.com/github/callback`
2. If 404, the backend route isn't implemented
3. Either:
   - Implement the route in your backend
   - Or update GitHub to use the route that exists

---

### Option D: Create a Simple Backend Route (If Needed)

**If you need OAuth but don't have a backend yet:**

**FastAPI Example:**
```python
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/api/github/callback")
async def github_callback(code: str, installation_id: str):
    # Exchange code for token
    # Store installation_id
    # Redirect to success page
    return RedirectResponse(url="https://contruil.com/github/success")
```

**Deploy this to:**
- Vercel (as serverless function)
- Your existing `api.contruil.com` server
- Or create a new service

---

## Step 6: Verification Checklist

**After fixing, verify:**

- [ ] Callback URL in GitHub App matches backend route
- [ ] Backend route is implemented and deployed
- [ ] Route is accessible (not 404)
- [ ] NGINX/OpenResty routes correctly (if using reverse proxy)
- [ ] OAuth flow completes successfully

---

## Recommended Configuration (Based on Common Patterns)

### For Vercel Deployments (Most Common)

**GitHub App Settings:**
- ❌ **Uncheck:** "Request user authorization (OAuth) during installation"
- **Callback URL:** Leave blank or `https://contruil.com`
- **Webhook:** Not needed (Vercel handles deployments)

**Why:** Vercel's GitHub integration handles everything automatically.

---

### For Custom Backend (If You Need OAuth)

**GitHub App Settings:**
- ✅ **Check:** "Request user authorization (OAuth) during installation"
- **Callback URL:** `https://api.contruil.com/api/github/callback` (most common)
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

## Next Steps

**To get precise help, run these commands and share results:**

```bash
# 1. Test if api.contruil.com responds
curl -I https://api.contruil.com

# 2. Test different callback paths
curl -I https://api.contruil.com/github/callback
curl -I https://api.contruil.com/api/github/callback

# 3. Check what framework you're using
# (Look in your codebase for main.py, app.js, etc.)
```

**Then tell me:**
1. What framework/platform are you using?
2. What does `curl -I https://api.contruil.com/api/github/callback` return?
3. Do you actually need OAuth, or can you use Vercel's GitHub integration?

---

**Most Likely Solution:** If you're using Vercel, you probably don't need the OAuth callback at all. Just uncheck "Request user authorization" and use Vercel's built-in GitHub integration.

