# Portfolio Site Structure

## File Organization

```
portfolio/
├── landing.html          # Main landing page (Fly Wheels brand)
├── index.html            # Data Science Portfolio (light theme)
├── README.md             # Portfolio overview (markdown)
├── PROJECTS.md           # Detailed project descriptions
└── SITE_STRUCTURE.md     # This file
```

## Page Purposes

### landing.html
- **Purpose:** Main personal/professional landing page
- **Theme:** Dark, minimalist (Fly Wheels brand)
- **Content:**
  - Personal branding and mission
  - Newsletter signup ("Awareness in Action")
  - Links to LinkedIn and Contruil
  - Link to Data Science Portfolio
- **Audience:** General visitors, potential clients/collaborators

### index.html
- **Purpose:** Technical portfolio showcase
- **Theme:** Light, colorful, professional
- **Content:**
  - Featured projects (Budget Analyzer, Triangle Test, State Machines)
  - Technical skills breakdown
  - Project statistics
  - Detailed project descriptions
- **Audience:** Technical recruiters, data science professionals, hiring managers

### README.md
- **Purpose:** Markdown overview of portfolio
- **Format:** GitHub-friendly markdown
- **Use:** Can be used as GitHub README or converted to PDF

### PROJECTS.md
- **Purpose:** Deep-dive technical documentation
- **Content:** Detailed problem statements, solutions, implementations
- **Use:** Reference document, detailed project explanations

## Navigation Flow

```
Visitor arrives at landing.html
    ↓
Options:
    - Subscribe to newsletter
    - Visit LinkedIn
    - Visit Contruil
    - View Data Science Portfolio (index.html)
    
From index.html:
    - Back to Home (landing.html)
    - LinkedIn
    - Email contact
```

## Deployment Options

### Option 1: GitHub Pages
1. Create a GitHub repository
2. Push portfolio files
3. Enable GitHub Pages in repository settings
4. Site available at `username.github.io/repo-name`

### Option 2: Personal Domain
1. Host files on web server (AWS S3, Netlify, Vercel, etc.)
2. Point domain to hosting location
3. Update links if using custom domain

### Option 3: Netlify/Vercel
1. Connect GitHub repository
2. Automatic deployments on push
3. Custom domain support
4. SSL certificates included

## Customization Checklist

- [ ] Update email newsletter endpoint in `landing.html` (line 70)
- [ ] Verify all LinkedIn/profile links
- [ ] Update email address if different
- [ ] Add actual project screenshots/visualizations
- [ ] Connect newsletter form to email service (Mailchimp, ConvertKit, etc.)
- [ ] Test all links and navigation
- [ ] Update copyright year (auto-handled by JavaScript)
- [ ] Add Google Analytics if desired
- [ ] Test mobile responsiveness

## Email Newsletter Integration

The newsletter form in `landing.html` currently has a placeholder. To connect it:

### Option 1: Mailchimp
```javascript
// Replace the form handler with:
fetch('https://your-domain.us1.list-manage.com/subscribe/post-json?...', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({email: document.getElementById('email').value})
});
```

### Option 2: ConvertKit
```javascript
fetch('https://api.convertkit.com/v3/forms/{form_id}/subscribe', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    api_key: 'your_api_key',
    email: document.getElementById('email').value
  })
});
```

### Option 3: HighLevel
```javascript
fetch('https://services.leadconnectorhq.com/contacts/', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer your_token',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    email: document.getElementById('email').value,
    locationId: 'your_location_id'
  })
});
```

## SEO Considerations

Both pages include:
- Meta description tags
- Proper HTML structure
- Semantic HTML elements

To enhance SEO:
- Add Open Graph tags for social sharing
- Add Twitter Card metadata
- Consider adding structured data (JSON-LD)
- Ensure page titles are unique and descriptive

## Maintenance

### Regular Updates
- Update project statistics as new projects are added
- Refresh portfolio with latest work
- Update "Last Updated" dates
- Keep links current

### Analytics
Consider adding:
- Google Analytics
- Plausible Analytics (privacy-friendly)
- Simple hit counter

---

**Last Updated:** December 31, 2024

