# Creating a Vercel Deploy Hook - Step by Step

## The Issue
You entered the API endpoint URL in the "Branch" field. The Branch field needs a **Git branch name**, not a URL.

## Correct Steps

### Step 1: Fill in the Form Correctly

In the Vercel Dashboard Deploy Hooks page:

1. **Name field:** 
   - Enter: `Production Deploy` (or any name you want)
   - ✅ This is correct

2. **Branch field:**
   - ❌ **DON'T enter:** `https://api.vercel.com/v1/integrations/deploy/`
   - ✅ **DO enter:** `main` (or `master`, or whatever your production branch is)
   - This should be a Git branch name from your repository

3. **Click "Create Hook"**

### Step 2: Get Your Deploy Hook URL

After clicking "Create Hook", Vercel will:
- Create the hook
- Display the **complete deploy hook URL** (this is what you need!)
- The URL will look like: `https://api.vercel.com/v1/integrations/deploy/prj_XXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX`

### Step 3: Copy and Use the URL

Once you see the complete URL, copy it and use it like this:

```bash
curl -X POST "https://api.vercel.com/v1/integrations/deploy/prj_XXXXXXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX"
```

## Quick Fix

1. Clear the Branch field
2. Enter `main` (or your production branch name)
3. Click "Create Hook"
4. Copy the generated URL
5. Use that URL in your curl command

## What Each Field Does

- **Name:** Just a label for your reference (e.g., "Production Deploy")
- **Branch:** The Git branch that will be deployed when the hook is triggered (e.g., `main`, `master`, `production`)
- **Generated URL:** The webhook endpoint you'll use to trigger deployments (you get this AFTER creating the hook)

---

**The deploy hook URL is the RESULT of creating the hook, not something you enter!**

