# GitHub App Registration Guide

**Purpose:** Automate deployments and CI/CD workflows for Contruil portfolio and projects  
**Organization:** Contruil LLC  
**Date:** December 2024

---

## Form Field Recommendations

### Basic Information

**GitHub App name:**
```
Contruil Portfolio Deployer
```
*Or:*
```
Contruil CI/CD Automation
```

**Homepage URL:**
```
https://contruil.com
```
*Or your portfolio URL:*
```
https://timothywheels.com
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
- ✅ **Request user authorization (OAuth) during installation** - Check this if you need user identity
- ⚠️ **Enable Device Flow** - Only if you need device-based auth (usually not needed for CI/CD)

---

### Post Installation

**Setup URL (optional):**
```
https://contruil.com/github/setup
```
*Or leave blank if not needed*

**Redirect on update:**
- ✅ **Check this** - Redirect users after installations are updated (useful for managing access)

---

### Webhook Configuration

**Important:** There are TWO different webhook concepts here:

1. **GitHub App Webhook** (this section) - Receives events FROM GitHub
2. **Vercel Deploy Hook** (separate) - Triggers deployments TO Vercel

**Active:**
- ✅ **Check "Active"** - Enable webhooks (if you need to receive GitHub events)
- ⚠️ **OR leave unchecked** - If you only need to trigger Vercel deployments (not receive GitHub events)

**Webhook URL Options:**

**Option A: Use Vercel's GitHub Integration (Recommended)**
If Vercel is connected to your GitHub repo, you may not need a custom webhook. Vercel automatically deploys on push.

**Option B: Custom Webhook Endpoint**
If you need to process GitHub events yourself:
```
https://api.contruil.com/github/webhook
```
*For development:*
```
http://localhost:8080/github/webhook
```
*Or use a webhook service like:*
```
https://hooks.zapier.com/hooks/catch/YOUR_WEBHOOK_ID
```

**Option C: Vercel Webhook (If Vercel Provided One)**
If Vercel gave you a webhook URL to receive deployment events:
- Use that URL here
- This receives events FROM Vercel (deployment status, etc.)
- Different from the deploy hook that triggers deployments

**Secret:**
- Generate a strong random secret (32+ characters)
- Store in environment variable: `GITHUB_WEBHOOK_SECRET`
- Example generation:
  ```bash
  openssl rand -hex 32
  ```
- **If using Vercel's webhook:** Use the secret Vercel provided

**SSL verification:**
- ✅ **Enable SSL verification** (recommended for production)
- Only disable if using self-signed certificates in development

---

### Permissions

Based on your CI/CD and deployment needs:

#### Repository Permissions

**Required for Vercel deployments:**
- ✅ **Contents:** Read-only (to access repository code)
- ✅ **Metadata:** Read-only (always required)
- ✅ **Pull requests:** Read-only (to monitor PRs)
- ✅ **Issues:** Read-only (optional, for issue tracking)

**For GitHub Actions automation:**
- ✅ **Actions:** Read & write (to trigger workflows)
- ✅ **Deployments:** Write (to create deployment statuses)

**For repository management:**
- ⚠️ **Administration:** Read-only (if you need to manage settings)
- ⚠️ **Pull requests:** Write (if you want to create/update PRs)

#### Organization Permissions

**If using organization-level features:**
- ⚠️ **Members:** Read-only (if you need to check team membership)
- ⚠️ **Plan:** Read-only (if you need to check billing/plan)

#### Account Permissions

**For user identity (if OAuth enabled):**
- ⚠️ **Email addresses:** Read-only (if you need user email)
- ⚠️ **Profile:** Read-only (if you need user profile info)

---

### Subscribe to Events

**Recommended events for CI/CD:**

**Repository Events:**
- ✅ **Push** - Trigger on code pushes
- ✅ **Pull request** - Monitor PRs
- ✅ **Release** - Track releases
- ✅ **Create** - Track branch/tag creation
- ✅ **Delete** - Track branch/tag deletion

**Workflow Events:**
- ✅ **Workflow run** - Monitor GitHub Actions runs
- ✅ **Workflow job** - Track individual job status

**Deployment Events:**
- ✅ **Deployment** - Track deployment status
- ✅ **Deployment status** - Monitor deployment results

**Optional Events:**
- ⚠️ **Installation** - Track app installations
- ⚠️ **Installation repositories** - Track repository access changes
- ⚠️ **Meta** - Track app deletion/removal

---

### Installation Target

**Where can this GitHub App be installed?**

**For Contruil LLC only:**
- ✅ **Only on this account** - Select "Only on this account"
- Choose: `@Contruil-LLC`

**For broader use:**
- ⚠️ **Any account** - Only if you want others to install it

**Recommendation:** Start with "Only on this account" for security. You can change this later.

---

## Complete Configuration Summary

### Minimal CI/CD Setup (Recommended)

```
GitHub App name: Contruil Portfolio Deployer
Homepage URL: https://contruil.com
Callback URL: https://api.contruil.com/github/callback

✅ Expire user authorization tokens
✅ Request user authorization (OAuth) during installation
❌ Enable Device Flow

Setup URL: (leave blank)
✅ Redirect on update

✅ Webhook Active
Webhook URL: https://api.contruil.com/github/webhook
Secret: [Generate with: openssl rand -hex 32]
✅ Enable SSL verification

Repository Permissions:
- Contents: Read-only
- Metadata: Read-only
- Actions: Read & write
- Deployments: Write

Events:
- Push
- Pull request
- Workflow run
- Deployment
- Deployment status

Installation: Only on this account (@Contruil-LLC)
```

---

## Post-Registration Steps

### 1. Save Credentials

After registration, you'll receive:
- **App ID** - Store as `GITHUB_APP_ID`
- **Client ID** - Store as `GITHUB_CLIENT_ID`
- **Client Secret** - Store as `GITHUB_CLIENT_SECRET` (NEVER commit to git)
- **Private Key** - Download and store securely as `GITHUB_APP_PRIVATE_KEY`

### 2. Generate Private Key

1. Click "Generate a private key"
2. Download the `.pem` file
3. Store in secure location: `~/Projects/CYW_Ops/secrets/github_app_private_key.pem`
4. Add to `.gitignore`

### 3. Install the App

1. Go to your GitHub App settings
2. Click "Install App"
3. Select `@Contruil-LLC` organization
4. Choose repositories (or "All repositories")
5. Click "Install"

### 4. Get Installation ID

After installation, note the Installation ID from the URL:
```
https://github.com/settings/installations/12345678
                                    ^^^^^^^^
                                    Installation ID
```

Store as: `GITHUB_INSTALLATION_ID`

---

## Environment Variables

Add these to your `.env` file (never commit):

```bash
# GitHub App Credentials
GITHUB_APP_ID=123456
GITHUB_CLIENT_ID=your_client_id_here
GITHUB_CLIENT_SECRET=your_client_secret_here
GITHUB_APP_PRIVATE_KEY_PATH=~/Projects/CYW_Ops/secrets/github_app_private_key.pem
GITHUB_INSTALLATION_ID=12345678
GITHUB_WEBHOOK_SECRET=your_webhook_secret_here

# Callback URLs
GITHUB_CALLBACK_URL=https://api.contruil.com/github/callback
GITHUB_WEBHOOK_URL=https://api.contruil.com/github/webhook
```

---

## Testing the Setup

### Test Webhook Locally

Use ngrok or similar to expose local server:

```bash
ngrok http 8080
# Use the ngrok URL as your webhook URL temporarily
```

### Test OAuth Flow

1. Visit: `https://github.com/login/oauth/authorize?client_id=YOUR_CLIENT_ID&scope=repo`
2. Authorize the app
3. Should redirect to your callback URL with code
4. Exchange code for access token

### Test Installation Token

```python
import jwt
import time
import requests

# Generate JWT
app_id = "YOUR_APP_ID"
private_key_path = "path/to/private-key.pem"

def generate_jwt():
    now = int(time.time())
    payload = {
        "iat": now - 60,
        "exp": now + (10 * 60),
        "iss": app_id
    }
    
    with open(private_key_path, 'r') as f:
        private_key = f.read()
    
    return jwt.encode(payload, private_key, algorithm="RS256")

# Get installation token
jwt_token = generate_jwt()
installation_id = "YOUR_INSTALLATION_ID"

response = requests.post(
    f"https://api.github.com/app/installations/{installation_id}/access_tokens",
    headers={
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github.v3+json"
    }
)

installation_token = response.json()["token"]
print(f"Installation token: {installation_token}")
```

---

## Security Checklist

- [ ] Private key stored securely (not in git)
- [ ] Client secret stored in environment variables
- [ ] Webhook secret configured and verified
- [ ] SSL verification enabled (production)
- [ ] Minimal permissions granted (principle of least privilege)
- [ ] Installation limited to Contruil-LLC account
- [ ] Callback URL whitelisted
- [ ] Webhook payloads verified with secret

---

## Integration with Vercel

### Understanding Vercel Webhooks vs Deploy Hooks

**Vercel Deploy Hook** (What we set up earlier):
- **Purpose:** Triggers deployments TO Vercel
- **URL Format:** `https://api.vercel.com/v1/integrations/deploy/prj_XXX/XXX`
- **Direction:** You → Vercel (trigger deployment)
- **Use Case:** Manual or automated deployment triggers

**Vercel Webhook** (If Vercel provided one):
- **Purpose:** Receives events FROM Vercel
- **URL Format:** Vercel provides this (usually in project settings)
- **Direction:** Vercel → You (deployment status updates)
- **Use Case:** Monitor deployment status, get notified of deployments

**GitHub App Webhook** (This form):
- **Purpose:** Receives events FROM GitHub
- **Direction:** GitHub → You (push, PR, etc. events)
- **Use Case:** Process GitHub events, trigger actions

### Option 1: Use Vercel's Built-in GitHub Integration (Simplest)

If Vercel is connected to your GitHub repo:
1. Vercel automatically deploys on push (no webhook needed)
2. You can skip the GitHub App webhook section
3. Just use the Vercel Deploy Hook for manual triggers

### Option 2: Custom Integration (If You Need It)

You can trigger Vercel deployments from GitHub webhooks:

```python
# Example webhook handler
import hmac
import hashlib
import json
import requests
import os

def verify_webhook(payload, signature, secret):
    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(f"sha256={expected}", signature)

def handle_webhook(request):
    # Verify webhook
    signature = request.headers.get("X-Hub-Signature-256")
    secret = os.getenv("GITHUB_WEBHOOK_SECRET")
    
    if not verify_webhook(request.data, signature, secret):
        return "Invalid signature", 401
    
    event = json.loads(request.data)
    
    # Trigger Vercel deploy on push to main
    if event.get("ref") == "refs/heads/main":
        vercel_hook = os.getenv("VERCEL_DEPLOY_HOOK_URL")
        requests.post(vercel_hook)
        return "Deploy triggered", 200
    
    return "OK", 200
```

### Option 3: Use Vercel's Webhook (If Provided)

If Vercel gave you a webhook URL to receive deployment events:
- Use that URL in the GitHub App webhook field (if you want GitHub to forward to Vercel)
- Or set it up separately to receive Vercel deployment status updates

---

## Next Steps

1. Fill out the GitHub App registration form using the recommendations above
2. Save all credentials securely
3. Install the app on your organization
4. Set up webhook endpoint to receive events
5. Test the integration
6. Connect to Vercel deploy hook for automated deployments

---

**Last Updated:** December 2024  
**Status:** Ready for implementation

