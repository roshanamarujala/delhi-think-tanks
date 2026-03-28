# 🏛️ Maintenance & Recovery Guide

This project is a high-fidelity, high-performance directory of Delhi-based think tanks. This guide ensures that you (or any AI assistant) can maintain and restore the project even if session history is lost.

## 📍 File Locations
The project is stored in your local workspace:
- **Primary Website**: `/Users/roshanamarujala/Desktop/Antigravity/index.html`
- **Standalone Backup**: `/Users/roshanamarujala/Desktop/Antigravity/ultimate_directory_2026.html`
- **Public Repository**: `https://github.com/roshanamarujala/delhi-think-tanks`

---

## 🛠️ How to Update the Website
Any changes you make to `index.html` will be reflected online once you push to GitHub.

### 1. Adding a New Think Tank
Locate the relevant category section (e.g., `section-geo`) and paste a new card block:
```html
<div class="tt-card [category]-card">
    <div class="tt-header">
        <a href="URL" class="tt-name">Institution Name</a>
        <span class="tt-focus">Brief description of policy focus.</span>
    </div>
    <div class="tt-meta">📍 Location</div>
    <div class="tt-links">
        <a href="URL" class="tt-link primary">Home</a>
    </div>
</div>
```

### 2. Updating Category Counts
If you add or remove cards, you must update the **badge count** manually in the HTML:
- Search for `<div class="domain-badge">`
- Update the number (e.g., `30 Institutions` -> `31 Institutions`)

### 3. Deploying Changes (CLI)
Run this command in the terminal to go live:
```bash
git add . && git commit -m "Update: [Description of change]" && git push origin main
```

---

## 🏛️ Recovery: "I lost my session history!"
If you start a new conversation with an AI, you don't need the old logs. The repository **is** the history.

**Action Plan for New Sessions:**
1. Tell the AI: *"I have a repository at `https://github.com/roshanamarujala/delhi-think-tanks`. Please read the `index.html` and help me [task]."*
2. The AI will scan the existing structure and maintain the exact design style.

---

## ✍️ Branding & Attribution
**Official Handle**: @roshanamarujala
Maintain the professional footer and "Curated by" sections to preserve the publishing authority of the document.
