# CLAUDE.md — Emilie Mazurek Portfolio

## Project Overview
Personal portfolio site for Emilie Mazurek — Senior Product Designer. Multi-page static site.

**Pages:** `index.html` · `about.html` · `community.html` · `links.html` · `veerum.html` · `barstool.html` · `proposify.html` · `max-retail.html`
**Shared:** `styles.css` · `nav.js`

## Local Server
- **No Node.js on this machine.** Use Python instead.
- Start server: `cd "/Users/emiliemazurek/Documents/Cursor/Website design" && /usr/bin/python3 -m http.server 3000 &>/tmp/portfolio-server.log &`
- Site available at: `http://localhost:3000`
- Check if already running before starting a new instance: `lsof -i :3000`

## Screenshots
- No Puppeteer/Node available. Ask the user to share a browser screenshot, or use whatever screenshot tool is available.
- Always serve from localhost, never from `file:///`.

## Brand Assets
All assets live in `brand_assets/`:
- `Emilie rainbow@3x.png` — rainbow wordmark (use in nav)
- `Emilie Black@3x.png` — black wordmark (use in footer, inverted to white)
- `Rainbow Favicon Bold@3x.png` — favicon
- `images/DSC03735.jpg` — hero headshot (full-body swing photo)
- `images/DSC03711.jpg` — alternate headshot (closer crop, golden hour)

## Design System
**Colors (exact hex — never use Tailwind defaults):**
- `--coral: #E8584A`
- `--pink: #F07DB5`
- `--periwinkle: #6B77C8`
- `--purple: #6347E8`
- `--mint: #7DD4B0`
- `--dark: #1A1A1A`
- `--white: #FFFFFF`
- `--off-white: #F8F7F5`

**Typography:**
- Font: ITC Avant Garde Gothic (self-hosted from `brand_assets/Typography/`)
- Headings: `'ITC Avant Garde'`, weight 800 (Bold), `letter-spacing: -0.03em`
- Subheadings/UI: weight 700 (Demi)
- Body: weight 400/300 (Book), `line-height: 1.75`
- Medium weight: 500 (Medium)
- No Google Fonts — do not re-add the @import

**Work card colors:**
- Max Retail → `card-purple`
- VEERUM → `card-periwinkle`
- Barstool Sports Store → `card-coral`
- Proposify → `card-mint`

## Output Rules
- Multi-page site — each page is its own `.html` file
- Shared styles go in `styles.css`; page-specific styles in a `<style>` tag per file
- No Tailwind CDN (not used in this project — custom CSS only)
- No `transition-all` — only animate `transform` and `opacity`
- Every interactive element needs hover, focus-visible, and active states
- WCAG 2.0 AA minimum (contrast, semantic HTML, skip nav, focus indicators)

## Nav Structure
`[rainbow logo] → Work · About · Community` — no CTA button
`/links` page is footer-only (not in primary nav)

## Git & Version Control
- This repo is tracked in git and pushed to GitHub — commit and push regularly so no work is ever lost.
- **After every meaningful change** (new page, significant edit, bug fix), commit and push before moving on.
- Commit messages must be clean and descriptive — describe what changed and why, not just "update files".
  - Good: `add community page with resource grid and mentoring services`
  - Good: `fix nav toggle aria state on mobile`
  - Bad: `update index.html`, `changes`, `wip`
- Stage specific files by name — never `git add .` or `git add -A` (risks committing unintended files).
- Always `git push` after committing so GitHub stays in sync.
- Check `git status` before committing to confirm only intended files are staged.

## Hard Rules
- Never invent brand colors — use the hex values above
- Never use default Tailwind palette
- No "coming soon" pages — build everything fully
- Do not add sections or features not asked for
- Do not use `transition-all`
