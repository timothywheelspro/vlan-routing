#!/bin/bash
# Vercel Deploy Hook Script
# Usage: ./deploy-hook.sh [hook-url]

HOOK_URL="${1:-${VERCEL_DEPLOY_HOOK}}"

if [ -z "$HOOK_URL" ]; then
    if [ -f ".vercel-deploy-hook" ]; then
        HOOK_URL=$(cat .vercel-deploy-hook)
    else
        echo "Error: No deploy hook URL provided"
        echo ""
        echo "Usage:"
        echo "  ./deploy-hook.sh YOUR_HOOK_URL"
        echo ""
        echo "Or set environment variable:"
        echo "  export VERCEL_DEPLOY_HOOK='YOUR_HOOK_URL'"
        echo ""
        echo "Or create .vercel-deploy-hook file:"
        echo "  echo 'YOUR_HOOK_URL' > .vercel-deploy-hook"
        exit 1
    fi
fi

echo "🚀 Triggering Vercel deployment..."
echo "Hook URL: ${HOOK_URL:0:50}..."
echo ""

response=$(curl -s -w "\n%{http_code}" -X POST "$HOOK_URL")
http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')

if [ "$http_code" -eq 200 ] || [ "$http_code" -eq 201 ]; then
    echo "✅ Deployment triggered successfully!"
    echo "$body" | jq '.' 2>/dev/null || echo "$body"
else
    echo "❌ Deployment failed (HTTP $http_code)"
    echo "$body"
    exit 1
fi

