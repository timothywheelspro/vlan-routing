"""
GitHub App OAuth Callback Handler
Handles OAuth callback from GitHub App installation flow
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from typing import Optional

app = FastAPI(
    title="GitHub App OAuth Callback",
    description="Handles GitHub App OAuth callbacks for Contruil Portfolio Deployer",
    version="1.0.0"
)

# CORS middleware (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://contruil.com", "https://timothywheels.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GitHub App credentials (from environment variables)
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID", "Iv23lieioBWFPlGHdAGm")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")  # Set in environment
GITHUB_APP_ID = os.getenv("GITHUB_APP_ID", "2573684")

# Success/error redirect URLs
SUCCESS_URL = os.getenv("GITHUB_SUCCESS_URL", "https://contruil.com/github/success")
ERROR_URL = os.getenv("GITHUB_ERROR_URL", "https://contruil.com/github/error")


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": "GitHub App OAuth Callback",
        "app_id": GITHUB_APP_ID
    }


@app.get("/api/github/callback")
async def github_callback(
    code: Optional[str] = Query(None, description="OAuth authorization code"),
    installation_id: Optional[str] = Query(None, description="GitHub App installation ID"),
    state: Optional[str] = Query(None, description="OAuth state parameter"),
    error: Optional[str] = Query(None, description="Error code from GitHub"),
    error_description: Optional[str] = Query(None, description="Error description")
):
    """
    Handle GitHub App OAuth callback
    
    GitHub redirects here after user authorizes the app installation.
    We exchange the authorization code for an access token.
    """
    
    # Handle OAuth errors
    if error:
        error_msg = error_description or error
        print(f"GitHub OAuth error: {error} - {error_msg}")
        return RedirectResponse(
            url=f"{ERROR_URL}?error={error}&description={error_msg}",
            status_code=302
        )
    
    # Validate required parameters
    if not code:
        raise HTTPException(
            status_code=400,
            detail="Missing authorization code. GitHub should provide a 'code' parameter."
        )
    
    if not GITHUB_CLIENT_SECRET:
        print("WARNING: GITHUB_CLIENT_SECRET not set in environment")
        # For development, you might want to return a helpful error
        raise HTTPException(
            status_code=500,
            detail="Server configuration error: GITHUB_CLIENT_SECRET not configured"
        )
    
    try:
        # Exchange authorization code for access token
        token_response = await exchange_code_for_token(code)
        
        # Extract token information
        access_token = token_response.get("access_token")
        token_type = token_response.get("token_type", "bearer")
        scope = token_response.get("scope", "")
        
        # Log successful token exchange (don't log the actual token!)
        print(f"✅ OAuth success - Installation ID: {installation_id}, Scopes: {scope}")
        
        # Store installation_id and token (implement your storage logic here)
        # For example, save to database, Redis, or environment variable
        if installation_id:
            print(f"📦 Installation ID: {installation_id}")
            # TODO: Store installation_id and access_token securely
            # await store_installation(installation_id, access_token)
        
        # Redirect to success page
        return RedirectResponse(
            url=f"{SUCCESS_URL}?installation_id={installation_id}&scope={scope}",
            status_code=302
        )
        
    except httpx.HTTPStatusError as e:
        error_detail = f"GitHub API error: {e.response.status_code}"
        print(f"❌ {error_detail}: {e.response.text}")
        return RedirectResponse(
            url=f"{ERROR_URL}?error=token_exchange_failed&detail={error_detail}",
            status_code=302
        )
    except Exception as e:
        error_detail = f"Unexpected error: {str(e)}"
        print(f"❌ {error_detail}")
        return RedirectResponse(
            url=f"{ERROR_URL}?error=unexpected&detail={error_detail}",
            status_code=302
        )


async def exchange_code_for_token(code: str) -> dict:
    """
    Exchange GitHub OAuth authorization code for access token
    
    Reference: https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
    """
    
    token_url = "https://github.com/login/oauth/access_token"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            token_url,
            data={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code,
            },
            headers={
                "Accept": "application/json",
                "User-Agent": "Contruil-Portfolio-Deployer/1.0"
            },
            timeout=10.0
        )
        response.raise_for_status()
        return response.json()


@app.get("/api/github/install")
async def github_install_redirect():
    """
    Redirect to GitHub App installation page
    
    Use this endpoint to initiate the OAuth flow
    """
    install_url = f"https://github.com/apps/contruil-portfolio-deployer/installations/new"
    return RedirectResponse(url=install_url, status_code=302)


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "github-oauth-callback",
        "github_app_id": GITHUB_APP_ID
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

