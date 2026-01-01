# GitHub IP Allow List Configuration

**Purpose:** Restrict where your GitHub App can be accessed from (security feature)

---

## Form Fields Explained

### Allow list value
**This is the IP address or CIDR range that should be allowed.**

**Options:**

**Option 1: Your Current IP (for testing)**
- Find your IP: Visit https://whatismyipaddress.com/
- Enter it as: `123.45.67.89` (your actual IP)
- **Note:** This changes if your IP is dynamic

**Option 2: Your Office/Home Network (CIDR range)**
- If you have a static IP range: `192.168.1.0/24` (example)
- Or: `10.0.0.0/8` (for private networks)
- **Note:** Only use if you have a static IP range

**Option 3: Vercel IP Ranges (if webhooks come from Vercel)**
- Vercel's IP ranges (check Vercel docs for current ranges)
- Example: `76.76.21.0/24` (example - check Vercel docs)

**Option 4: Allow All (Not Recommended)**
- `0.0.0.0/0` (allows from anywhere - less secure)
- Only use for development/testing

**Option 5: Skip IP Allow List (Recommended for Most Cases)**
- **You don't have to create an IP allow list entry**
- Leave it disabled if you don't need IP restrictions
- The form error might be because you're trying to create an entry when you don't need one

---

### Name
**A descriptive name for this IP allow list entry.**

Examples:
- `My Development Machine`
- `Vercel Webhooks`
- `Office Network`
- `Home IP`
- `Production Server`

---

### Enabled?
**Whether this entry is active.**

- ✅ **Check** - Entry will be used to restrict access
- ❌ **Uncheck** - Entry exists but won't be enforced

---

## Recommended Configuration

### For Most Users: Skip IP Allow List

**If you're just setting up the GitHub App for basic CI/CD:**
- **Don't create an IP allow list entry**
- IP allow lists are optional
- Only needed if you want to restrict where the app can be accessed from
- The error might be because the form requires a value if you're trying to create an entry

**To skip:**
- Don't fill out the IP allow list form
- Leave it disabled/empty
- Continue with the rest of the GitHub App setup

---

### If You Need IP Restrictions

**Scenario 1: Local Development**
```
Allow list value: [Your current public IP from whatismyipaddress.com]
Name: Development Machine
Enabled?: ✅ Check
```

**Scenario 2: Vercel Webhooks**
```
Allow list value: [Vercel's IP ranges - check their docs]
Name: Vercel Webhooks
Enabled?: ✅ Check
```

**Scenario 3: Specific Server**
```
Allow list value: [Your server's IP address]
Name: Production Server
Enabled?: ✅ Check
```

---

## How to Find Your IP Address

**Quick method:**
```bash
curl ifconfig.me
```

**Or visit:**
- https://whatismyipaddress.com/
- https://icanhazip.com/

**Note:** If you have a dynamic IP (most home internet), your IP changes periodically, so IP allow lists may not work well for you.

---

## Common Issues

### "Allow list value can't be blank"
- **Solution:** Either fill in a valid IP/CIDR, or skip creating an IP allow list entry entirely
- IP allow lists are optional - you don't have to create one

### IP Changes Frequently
- **Solution:** Use CIDR ranges if you have a static range, or skip IP allow list
- Dynamic IPs make IP allow lists impractical

### Not Sure What to Enter
- **Solution:** Skip the IP allow list for now
- You can always add it later if needed
- Most GitHub Apps don't require IP allow lists

---

## Security Note

**IP allow lists are an additional security layer:**
- They restrict where your GitHub App can be accessed from
- Useful if you have a fixed server/IP
- Not practical for dynamic IPs (home internet, mobile)
- Most users don't need IP allow lists
- Webhook secrets provide sufficient security for most cases

---

## IPv6 Support

**GitHub is rolling out IPv6 support.** You may need to add IPv6 addresses to your allow list.

### Finding Your IPv6 Address

**Method 1: Check if you have IPv6**
```bash
curl -6 -s ifconfig.me
# or
curl -6 -s icanhazip.com
```

**Method 2: Check system configuration**
```bash
ifconfig | grep inet6
```

**Method 3: Visit IPv6 test site**
- https://test-ipv6.com/
- https://ipv6-test.com/

### Adding IPv6 to Allow List

**If you have an IPv6 address:**
- Create a separate allow list entry for IPv6
- **Allow list value:** Your IPv6 address (e.g., `2001:0db8:85a3:0000:0000:8a2e:0370:7334`)
- **Name:** `Development Machine IPv6`
- **Enabled?:** ✅ Check

**If you don't have IPv6:**
- You may not need to add it
- GitHub will still work with IPv4
- The message is a warning, not a requirement

**If you want to allow all IPv6 (not recommended):**
- **Allow list value:** `::/0` (allows all IPv6)
- **Name:** `Allow All IPv6`
- **Enabled?:** ✅ Check

### Complete Setup (IPv4 + IPv6)

**Entry 1 (IPv4):**
- Allow list value: `45.144.114.120` (or `0.0.0.0/0` for all)
- Name: `Development Machine IPv4`
- Enabled?: ✅ Check

**Entry 2 (IPv6 - if you have one):**
- Allow list value: `[Your IPv6 address]` (or `::/0` for all)
- Name: `Development Machine IPv6`
- Enabled?: ✅ Check

---

## Recommendation

**For your use case (Vercel deployments):**
- **Skip the IP allow list** - You don't need it
- Vercel's GitHub integration handles deployments automatically
- Webhook secrets provide security
- IP allow lists are optional and may cause issues with dynamic IPs

**If the form is forcing you to create an entry:**
- Try entering: `0.0.0.0/0` (allows all IPv4 - for development)
- Name: `Allow All IPv4 (Development)`
- Enabled?: ✅ Check
- **For IPv6:** Add `::/0` (allows all IPv6)
- Name: `Allow All IPv6 (Development)`
- Enabled?: ✅ Check
- **Then disable the IP allow list feature entirely** if possible

---

**Last Updated:** December 2024

