# How to Get Your Vercel Deploy Hook URL

## Quick Steps

1. **Open Vercel Dashboard:**
   - Go to: https://vercel.com/contruil-llc/portfolio/settings/deploy-hooks
   - Or navigate: Project → Settings → Deploy Hooks

2. **Create New Hook:**
   - Click the **"Create Hook"** button
   - **Name:** `Production Deploy` (or any name you prefer)
   - **Git Branch:** `main` (or your production branch)
   - Click **"Create Hook"**

3. **Copy the URL:**
   - You'll see a URL like: `https://api.vercel.com/v1/integrations/deploy/...`
   - **Copy this entire URL**

4. **Use the URL:**
   ```bash
   # Option 1: Direct curl
   curl -X POST "YOUR_COPIED_URL_HERE"
   
   # Option 2: Save and use script
   echo "YOUR_COPIED_URL_HERE" > .vercel-deploy-hook
   ./deploy-hook.sh
   
   # Option 3: One-liner with environment variable
   export VERCEL_DEPLOY_HOOK="YOUR_COPIED_URL_HERE"
   curl -X POST "$VERCEL_DEPLOY_HOOK"
   ```

## Example

Once you have your URL, it will look something like:
```
https://api.vercel.com/v1/integrations/deploy/prj_xxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Then you can run:
```bash
curl -X POST "https://api.vercel.com/v1/integrations/deploy/prj_xxxxxxxxxxxxx/xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## Security

⚠️ **Keep your deploy hook URL secret!** Anyone with this URL can trigger deployments to your site.

- Don't commit it to git (already in `.gitignore`)
- Don't share it publicly
- Consider using environment variables in CI/CD

## Test It

After creating the hook, test it:
```bash
curl -X POST "YOUR_HOOK_URL" -v
```

You should see a response like:
```json
{
  "job": {
    "id": "...",
    "state": "QUEUED"
  }
}
```

---

**Need help?** Check the Vercel docs: https://vercel.com/docs/deploy-hooks

