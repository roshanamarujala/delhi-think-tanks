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
Locate the relevant category section (e.g., `section-geo`) and paste a new card block. Note the inclusion of the `.tt-social` block:
```html
<div class="tt-card [category]-card">
    <div class="tt-social">
        <a href="LINKEDIN_URL" target="_blank" class="social-btn btn-lkn" title="LinkedIn">
            <svg><use href="#icon-lkn"></use></svg>
        </a>
        <a href="TWITTER_URL" target="_blank" class="social-btn btn-twt" title="Twitter/X">
            <svg><use href="#icon-twt"></use></svg>
        </a>
    </div>
    <div class="tt-header">
        <a href="HOME_URL" class="tt-name">Institution Name</a>
        <span class="tt-focus">Brief description of policy focus.</span>
    </div>
    <div class="tt-meta">📍 Location</div>
    <div class="tt-links">
        <a href="HOME_URL" class="tt-link primary">Home</a>
        <a href="EVENTS_URL" class="tt-link">Events</a>
        <a href="CAREERS_URL" class="tt-link">Join</a>
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

### 4. Social Media Verification Standard
All new entries must have verified LinkedIn and Twitter (X) profiles.
- **LinkedIn**: Use the official company page URL.
- **Twitter (X)**: Use the official institutional handle.
- **Icons**: Ensure the SVG `<use>` pattern is used (`#icon-lkn` and `#icon-twt`) to maintain performance.

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

---

## 📊 Project Census & Coverage (Verified)

| Thematic Domain | Count | Govt/Semi Status |
| :--- | :--- | :--- |
| **GEO** | 32 | 2 Govt, 2 Semi, 28 Private |
| **DEF** | 23 | 2 Govt, 10 Semi, 11 Private |
| **POL** | 36 | 3 Govt, 8 Semi, 25 Private |
| **ECO** | 20 | 3 Govt, 8 Semi, 9 Private |
| **TEC** | 17 | 2 Govt, 4 Semi, 11 Private |
| **ENV** | 15 | 4 Govt, 0 Semi, 11 Private |
| **SOC** | 19 | 4 Govt, 0 Semi, 15 Private |
| **LAW** | 12 | 2 Govt, 4 Semi, 6 Private |
| **ART** | 12 | 3 Govt, 5 Semi, 4 Private |
| **TOTAL** | **186** | **25 Govt, 41 Semi, 120 Private** |

### Verification Standard
- **Direct Links**: Every card contains verified Home, Events, and Careers/Jobs/Join links.
- **Social Integration**: 100% coverage for LinkedIn and Twitter (X) official profiles.
- **UI Logic**: All counts are synchronized between the Strategic Navigator and sectoral badges.

---

## 📜 Project History & Changelog

**March 2026 - The "Ultimate Edition" Refactoring**
- **Data Enrichment**: Scaled the directory from 140+ to **186 verified institutions**, expanding across 9 distinct policy domains including the new 'Arts & Culture' sector.
- **Master Research Suite UI**: Overhauled the header and directory guide to create a professional, premium introductory frame designed for maximum conversion and credibility.
- **Brand Synthesization**: Integrated `@roshanamarujala` into the sticky navigation and header as a strategic CTA, directly linking to professional social architectures (Instagram, LinkedIn, X).
- **Link Integrity Audit**: Executed exhaustive bash-level checks across all `tt-card` objects. All institutional anchors, event logs, and career portals are functional and accurately mapped as of the final spot check.
- **Structural Alignment**: Synchronized the frontend badge counts (GEO, DEF, POL, etc.) perfectly with the backend DOM counts. Fixed legacy structural fragment errors (`</div>v>`).
- **Leadership Data Integrity Audit**: Eliminated generic leadership placeholders for 10 entries across the document (e.g. replaced "Strategic Thinkers Group" and "Board of Directors" with accurate manual verification endpoints) to ensure zero data pollution in the metadata blocks.
