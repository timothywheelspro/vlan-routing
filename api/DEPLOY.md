# GitHub OAuth Callback API - Deployment Guide

## Quick Start

### 1. Set Environment Variables

**For local testing:**
```bash
export GITHUB_CLIENT_SECRET=48de0c3e222a171e2af23e6c3d5f03d0e172c0dc89900f26fc448a4c45075715
export GITHUB_CLIENT_ID=Iv23lieioBWFPlGHdAGm
export GITHUB_APP_ID=2573684
```

**For production (create .env file):**
```bash
# Create .env file (DO NOT COMMIT)
cat > .env << EOF
GITHUB_CLIENT_SECRET=48de0c3e222a171e2af23e6c3d5f03d0e172c0dc89900f26fc448a4c45075715
GITHUB_CLIENT_ID=Iv23lieioBWFPlGHdAGm
GITHUB_APP_ID=2573684
GITHUB_SUCCESS_URL=https://contruil.com/github/success
GITHUB_ERROR_URL=https://contruil.com/github/error
EOF
```

### 2. Run Locally

```bash
cd api
./run.sh
```

Or:
```bash
cd api
uvicorn github_callback:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Test

```bash
# Health check
curl http://localhost:8000/health

# Should return:
# {"status":"healthy","service":"github-oauth-callback","github_app_id":"2573684"}
```

---

## Deployment to api.contruil.com

### Option 1: Deploy to Existing Server

**If you have SSH access to api.contruil.com:**

```bash
# 1. Copy files to server
scp -r api/ user@api.contruil.com:/path/to/deployment/

# 2. SSH into server
ssh user@api.contruil.com

# 3. Set up environment
cd /path/to/deployment/api
pip install -r requirements.txt

# 4. Create .env file with secrets
nano .env  # Add your secrets

# 5. Run with process manager (systemd, supervisor, etc.)
# Or use gunicorn for production:
gunicorn github_callback:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Option 2: NGINX/OpenResty Reverse Proxy

**Configure NGINX to forward to FastAPI:**

```nginx
server {
    listen 443 ssl;
    server_name api.contruil.com;

    location /api/github/callback {
        proxy_pass http://localhost:8000/api/github/callback;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /api/ {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Option 3: Vercel Serverless

**Create `api/vercel.json`:**

```json
{
  "version": 2,
  "builds": [
    {
      "src": "github_callback.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/api/github/callback",
      "dest": "github_callback.py"
    },
    {
      "src": "/health",
      "dest": "github_callback.py"
    }
  ],
  "env": {
    "GITHUB_CLIENT_ID": "Iv23lieioBWFPlGHdAGm",
    "GITHUB_APP_ID": "2573684"
  }
}
```

**Set secrets in Vercel dashboard:**
- Go to Vercel project settings → Environment Variables
- Add: `GITHUB_CLIENT_SECRET` = `48de0c3e222a171e2af23e6c3d5f03d0e172c0dc89900f26fc448a4c45075715`

**Deploy:**
```bash
cd api
vercel deploy --prod
```

---

## Update GitHub App Settings

**After deployment:**

1. Go to: GitHub → Settings → Developer Settings → GitHub Apps → Contruil Portfolio Deployer
2. Update **Callback URL** to: `https://api.contruil.com/api/github/callback`
3. Save

---

## Security Checklist

- [x] Client secret stored in environment variables (not in code)
- [x] `.gitignore` excludes `.env` files
- [x] HTTPS enabled in production
- [ ] State parameter validation (CSRF protection) - TODO
- [ ] Rate limiting - TODO
- [ ] Request logging - TODO

---

## Testing the OAuth Flow

1. **Start the server:**
   ```bash
   cd api
   export GITHUB_CLIENT_SECRET=48de0c3e222a171e2af23e6c3d5f03d0e172c0dc89900f26fc448a4c45075715
   ./run.sh
   ```

2. **Test health endpoint:**
   ```bash
   curl http://localhost:8000/health
   ```

3. **Install GitHub App:**
   - Go to: https://github.com/apps/contruil-portfolio-deployer/installations/new
   - Authorize the app
   - Should redirect to success page (not 404)

---

**Status:** Ready for deployment

