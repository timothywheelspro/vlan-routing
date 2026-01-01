#!/bin/bash
# Run GitHub OAuth Callback API

set -euo pipefail

cd "$(dirname "$0")"

# Check if .env file exists
if [ -f .env ]; then
    echo "Loading environment variables from .env..."
    export $(cat .env | grep -v '^#' | xargs)
else
    echo "⚠️  No .env file found. Using environment variables from shell."
fi

# Check required environment variables
if [ -z "${GITHUB_CLIENT_SECRET:-}" ]; then
    echo "❌ Error: GITHUB_CLIENT_SECRET not set"
    echo ""
    echo "Set it with:"
    echo "  export GITHUB_CLIENT_SECRET=your_secret_here"
    echo ""
    echo "Or create a .env file with:"
    echo "  GITHUB_CLIENT_SECRET=your_secret_here"
    exit 1
fi

# Set defaults if not provided
export GITHUB_CLIENT_ID="${GITHUB_CLIENT_ID:-Iv23lieioBWFPlGHdAGm}"
export GITHUB_APP_ID="${GITHUB_APP_ID:-2573684}"
export GITHUB_SUCCESS_URL="${GITHUB_SUCCESS_URL:-https://contruil.com/github/success}"
export GITHUB_ERROR_URL="${GITHUB_ERROR_URL:-https://contruil.com/github/error}"
export PORT="${PORT:-8000}"

echo "🚀 Starting GitHub OAuth Callback API..."
echo "   Client ID: $GITHUB_CLIENT_ID"
echo "   App ID: $GITHUB_APP_ID"
echo "   Port: $PORT"
echo ""

uvicorn github_callback:app --host 0.0.0.0 --port "$PORT" --reload

