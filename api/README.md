# GitHub App OAuth Callback API

FastAPI service for handling GitHub App OAuth callbacks.

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file:

```bash
GITHUB_CLIENT_ID=Iv23lieioBWFPlGHdAGm
GITHUB_CLIENT_SECRET=your_client_secret_here
GITHUB_APP_ID=2573684
GITHUB_SUCCESS_URL=https://contruil.com/github/success
GITHUB_ERROR_URL=https://contruil.com/github/error
```

### 3. Run Locally

**Option A: Using the run script (recommended)**
```bash
# Set your client secret
export GITHUB_CLIENT_SECRET=your_secret_here

# Run
./run.sh
```

**Option B: Direct uvicorn command**
```bash
export GITHUB_CLIENT_SECRET=your_secret_here
uvicorn github_callback:app --reload --port 8000
```

**Option C: Using .env file**
```bash
# Create .env file with:
# GITHUB_CLIENT_SECRET=your_secret_here
# Then run:
./run.sh
```

### 4. Test

```bash
# Health check
curl http://localhost:8000/health

# Test callback (will fail without proper code, but tests route)
curl http://localhost:8000/api/github/callback?code=test
```

## Deployment

### Option 1: Vercel (Serverless)

1. Create `vercel.json`:
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
    }
  ]
}
```

2. Deploy to Vercel:
```bash
vercel deploy
```

### Option 2: Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY github_callback.py .

CMD ["uvicorn", "github_callback:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Option 3: Direct Server

```bash
# Install dependencies
pip install -r requirements.txt

# Run with uvicorn
uvicorn github_callback:app --host 0.0.0.0 --port 8000

# Or with gunicorn
gunicorn github_callback:app -w 4 -k uvicorn.workers.UvicornWorker
```

## GitHub App Configuration

**Callback URL:** `https://api.contruil.com/api/github/callback`

**Settings:**
- ✅ Request user authorization (OAuth) during installation
- ✅ Expire user authorization tokens

## API Endpoints

- `GET /` - Root/health check
- `GET /health` - Health check
- `GET /api/github/callback` - OAuth callback handler
- `GET /api/github/install` - Redirect to GitHub App installation

## Security Notes

- Never commit `GITHUB_CLIENT_SECRET` to git
- Use environment variables for all secrets
- Enable HTTPS in production
- Validate state parameter for CSRF protection (TODO)

