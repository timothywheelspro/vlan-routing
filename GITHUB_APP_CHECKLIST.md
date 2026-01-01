# GitHub App Registration - Complete Checklist

**Use this checklist to ensure you've configured everything correctly.**

---

## ✅ Basic Information

- [ ] **GitHub App name:** `Contruil Portfolio Deployer` (or your preferred name)
- [ ] **Homepage URL:** `https://contruil.com` (or your website)

---

## ✅ Identifying and Authorizing Users

- [ ] **Callback URL:** `https://api.contruil.com/github/callback` (or your endpoint)
- [x] **Expire user authorization tokens** - ✅ CHECK THIS
- [x] **Request user authorization (OAuth) during installation** - ✅ CHECK THIS (if you need user identity)
- [ ] **Enable Device Flow** - ❌ LEAVE UNCHECKED (not needed for CI/CD)

---

## ✅ Post Installation

- [ ] **Setup URL (optional):** Leave blank OR `https://contruil.com/github/setup`
- [x] **Redirect on update** - ✅ CHECK THIS (useful for managing access)

---

## ✅ Webhook

- [x] **Active** - ✅ CHECK THIS (if you want to receive GitHub events)
  - ⚠️ **OR leave unchecked** if you only need to trigger Vercel deployments (Vercel's GitHub integration handles this automatically)

- [ ] **Webhook URL:** 
  - Option A: Leave blank if using Vercel's built-in GitHub integration
  - Option B: `https://api.contruil.com/github/webhook` (if you have your own endpoint)
  - Option C: Use Vercel's webhook URL if they provided one

- [ ] **Secret:** `48de0c3e222a171e2af23e6c3d5f03d0e172c0dc89900f26fc448a4c45075715` (paste the generated secret)

- [x] **Enable SSL verification** - ✅ CHECK THIS (recommended for production)

---

## ✅ Permissions

### Repository Permissions

**Available permissions (select from dropdowns):**

- [x] **Contents:** ✅ Select "Read-only"
- [x] **Metadata:** ✅ Select "Read-only" (always required - may be auto-selected)
- [x] **Actions:** ✅ Select "Read & write" (to trigger workflows)
- [x] **Deployments:** ✅ Select "Write" (to create deployment statuses)
- [ ] **Pull requests:** Select "Read-only" (optional, to monitor PRs)
- [ ] **Issues:** Select "Read-only" (optional, for issue tracking)
- [ ] **Administration:** Select "Read-only" (only if you need to manage settings)

**Note:** These are dropdown menus, not checkboxes. Select the permission level from the dropdown.

### Organization Permissions

- [ ] **Members:** Read-only (only if you need to check team membership)
- [ ] **Plan:** Read-only (only if you need to check billing/plan)

### Account Permissions

- [ ] **Email addresses:** Read-only (only if you need user email)
- [ ] **Profile:** Read-only (only if you need user profile info)

---

## ✅ Subscribe to Events

**Check these event checkboxes (if available in the form):**

- [x] **Push** - ✅ CHECK (if checkbox exists)
- [x] **Pull request** - ✅ CHECK (if checkbox exists)
- [x] **Workflow run** - ✅ CHECK (if checkbox exists)
- [x] **Workflow job** - ✅ CHECK (if checkbox exists)
- [x] **Deployment** - ✅ CHECK (if checkbox exists)
- [x] **Deployment status** - ✅ CHECK (if checkbox exists)
- [ ] **Release** - Optional (if checkbox exists)
- [ ] **Create** - Optional (if checkbox exists)
- [ ] **Delete** - Optional (if checkbox exists)
- [ ] **Installation** - Optional (if checkbox exists)
- [ ] **Installation repositories** - Optional (if checkbox exists)
- [ ] **Meta** - Optional (if checkbox exists)

**Note:** The events available depend on the permissions you selected. GitHub will show relevant events based on your permission choices. If you don't see a "Pull request" checkbox, it may not be available based on your current permissions, or the form structure may be different.

---

## ✅ Installation Target

- [x] **Only on this account** - ✅ SELECT THIS
  - Choose: `@Contruil-LLC`

- [ ] **Any account** - ❌ DON'T SELECT (unless you want others to install it)

---

## 📋 Summary of Checkboxes to Check

**Must Check:**
1. ✅ Expire user authorization tokens
2. ✅ Request user authorization (OAuth) during installation
3. ✅ Redirect on update
4. ✅ Webhook Active (if you want to receive GitHub events)
5. ✅ Enable SSL verification

**Must NOT Check:**
1. ❌ Enable Device Flow

**Optional (Check if needed):**
- Setup URL (leave blank if not needed)
- Additional repository permissions (only if needed)
- Organization permissions (only if needed)
- Account permissions (only if needed)
- Additional events (only if needed)

---

## 🎯 Minimal Configuration (Recommended)

If you just want to trigger Vercel deployments automatically:

**Check:**
- ✅ Expire user authorization tokens
- ✅ Request user authorization (OAuth) during installation
- ✅ Redirect on update
- ❌ Webhook Active (LEAVE UNCHECKED - Vercel handles this automatically)
- ✅ Enable SSL verification

**Permissions (minimal - select from dropdowns):**
- Contents: Select "Read-only"
- Metadata: Select "Read-only" (may be auto-selected)
- Actions: Select "Read & write"
- Deployments: Select "Write"

**Events (check available checkboxes):**
- Check any events that appear (GitHub shows relevant events based on your permissions)
- Common events: Push, Workflow run, Deployment, Deployment status
- If "Pull request" event doesn't appear, it may not be available with your current permissions

**Installation:**
- Only on this account → @Contruil-LLC

---

## ✅ After Registration

- [ ] Save App ID
- [ ] Save Client ID
- [ ] Save Client Secret (NEVER commit to git)
- [ ] Download and save Private Key securely
- [ ] Install the app on @Contruil-LLC
- [ ] Note the Installation ID
- [ ] Save webhook secret to environment variables
- [ ] Test the integration

---

**Last Updated:** December 2024

