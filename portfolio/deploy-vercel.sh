#!/usr/bin/env bash
set -euo pipefail

# 1) Put your Deploy Hook URL here (or export it in your shell)
: "${VERCEL_DEPLOY_HOOK_URL:?Set VERCEL_DEPLOY_HOOK_URL}"

echo "Triggering Vercel deploy hook..."
curl -sS -X POST "$VERCEL_DEPLOY_HOOK_URL" >/dev/null
echo "OK: Deploy triggered."

