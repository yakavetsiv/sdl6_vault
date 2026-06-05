---
tags:
  - ai
  - type/skill
  - visualization
  - acceleration-consortium
name: ac-presentation
description: "Use this skill for creating or improving presentations for the Acceleration Consortium (AC) — research talks, conference presentations, lab meetings, grant briefings, seminar slides, or any deck representing AC/University of Toronto. Triggers on: 'AC presentation', 'AC slides', 'make slides', 'conference talk', 'research deck', 'thesis defense', 'grant briefing', 'seminar presentation', or any request to build/edit a .pptx in this project. Also triggers when the user shares research content (ML results, bioimaging data, materials science findings) and asks to present it. Governs AC brand compliance + academic content structure. For technical .pptx file creation/editing, also use the pptx skill."
tags:
  - ai
  - type/skill
  - sdl6
---

# Acceleration Consortium Presentation Skill

## Overview

Two-layer system:
1. **This file** — AC brand identity + academic content standards. Read fully before planning any slide.
2. **PPTX skill** — technical .pptx implementation (pptxgenjs, editing, QA).

Always read both before writing code or creating files.

---

## AC Brand Identity (Official — March 2026 Guide)

### Colour Palette

AC uses an intentionally minimal, three-colour palette. Do not introduce additional colours.

```javascript
const AC_COLORS = {
  black:    "000000",   // Primary body text, sub-headings, dark slide backgrounds
  orange:   "FF3D00",   // Slide titles on white slides, section labels, key annotations, eyebrow dots
  gray:     "D4D4D4",   // Dividers, muted elements
  white:    "FFFFFF",   // Content slide backgrounds, body text on dark slides
  // Extended grays (use sparingly):
  grayDark: "515151",   // Captions, citations
  grayMid:  "919191",   // Muted text, footer text
  grayLight:"EAEAEA",   // Subtle backgrounds
};
```

**Rules — confirmed from visual frames + ML.pptx slide 15:**
- **White background slides:** slide title = ORANGE; sub-headings within slide = BLACK; body = BLACK.
- **Black background slides (title, section dividers, closing):** slide title = ORANGE or WHITE depending on emphasis; body = WHITE.
- Orange (`FF3D00`) for: slide titles on white BG, section/page labels, the orange dot (●) marker before section names, key finding annotations, active section indicators.
- Never use orange for large body-text blocks or decorative fills.
- Gray variants for dividers, citations, footer.
- Do not add colours from outside this palette (no navy, no blue, no gradients).

**Extended palette — DATA GRAPHS ONLY** (from ML.pptx slide 15 — do NOT use for text or design elements):

```javascript
const AC_GRAPH_COLORS = [
  "FF3D00",   // Primary orange (also main brand)
  "FF7136",   // Light orange
  "F7B833",   // Amber / yellow-orange
  "9395DE",   // Lavender / periwinkle
  "B0E1DC",   // Teal / mint
  "655FE8",   // Purple / violet
  "F5EA81",   // Light yellow
  "E8E8E8",   // Light gray
];
// Use these as series colors in bar charts, line charts, scatter plots.
// Never use for slide backgrounds, text, borders, or decorative elements.
```

### Typography

**Preferred (brand fonts — use if available on target machine):**

| Role | Font | Weight |
|------|------|--------|
| Eyebrow / label text | IBM Plex Mono | Regular |
| Headings / action titles | Obviously | Semibold (default), Medium if Semibold feels heavy |
| Body text | IBM Plex Sans | Regular |

**Universal fallback (always safe — use in .pptx files):**

| Role | Font | Weight |
|------|------|--------|
| Eyebrow / label text | Courier New | Regular |
| Headings / action titles | Arial | Black (default), Bold if Black feels heavy |
| Body text | Arial | Regular |

```javascript
const AC_FONTS = {
  face:     "Arial",          // Universal substitute for IBM Plex Sans + Obviously
  eyebrow:  "Courier New",    // Substitute for IBM Plex Mono
  title:    28,               // Slide title (action title): 26–30 pt bold, ORANGE on white slides
  eyebrowSz:13,               // Eyebrow label (ALL CAPS, mono, above heading)
  subhead:  20,               // Within-slide sub-headings: black, bold
  body:     20,               // Body bullets: 20 pt minimum, black on white / white on black
  label:    16,               // Chart annotations, inline labels
  cite:     13,               // In-slide citations, captions
  footer:   11,               // "ACCELERATION CONSORTIUM" footer, page number
};
```

**Observed typography hierarchy (from visual frames):**

```
[● SECTION LABEL]           ← orange dot (●) + Courier New, ~13pt, ALL CAPS, orange/gray
Slide Title / Action Title  ← Arial Black or Obviously Semibold, 28–36pt, ORANGE (on white BG)
Sub-heading within slide    ← Arial Black, 18–20pt, BLACK (on white BG)
Body paragraph / bullets    ← Arial Regular, 18–20pt, BLACK (on white) or WHITE (on black)
─────────────────────────── ← thin gray or orange rule (optional)
Source / citation           ← Courier New or Arial, 11–13pt, gray
ACCELERATION CONSORTIUM  17 ← Courier New, ~10pt, gray — bottom-left footer + page number right
```

**The orange dot marker (●):** Used visually before section category labels (e.g., "● WHAT TO DO", "● PHOTOGRAPHY", "● ABSTRACT"). Implemented as a filled orange circle shape + Courier New label beside it.

### Slide Dimensions

AC template uses **13.33" × 7.50"** widescreen.
Confirm with user if presenting at a venue with different specs. Default to this size when creating from scratch.

```javascript
const pres = new PptxGenJS();
pres.layout = "LAYOUT_WIDE";  // 13.33" x 7.50"
const MARGIN = 0.5;           // Minimum margin from slide edge (inches)
```

### Logo

- **Always use the U of T + AC lockup** when officially representing AC.
- U of T logo on the LEFT, AC logo on the RIGHT, separated by a thin vertical rule.
- When space is too constrained: AC logo alone is acceptable.
- **Never:** alter logo colours, distort proportions, add effects, rotate, or place on busy backgrounds.
- Title slide: place lockup at the top or bottom of slide in a designated safe zone.

### Visual Assets

**Use:**
- Abstract imagery (sparingly) — bold colours, inspire imagination about materials science
- Real photography — stock or commissioned, showing actual research, equipment, people
- Diversity imagery — real people, inclusive representation

**Never use:**
- Cartoon / illustration / clip art style
- Clip art icons in coloured circles
- AI-generated "tech" clichés (glowing brains, neural network art, etc.)
- Clutter — not every slide needs an image

**AC asset library (SharePoint — for authorised users):**
- SDL images: AC SDL SharePoint / Photos and videos / Deck photo library
- SDL videos: AC SDL SharePoint / Photos and videos / SDL tour videos
- Accelerate photos: AC SDL SharePoint / Photos and videos / Accelerate
- PowerPoint template: AC SDL SharePoint / Templates and resources / 2026 PPT Deck Template

---

## Existing Template

**`ML.pptx`** in this directory is the current AC-branded research deck.
- 15 slides, 13.33" × 7.50"
- Theme colours: `FF3D00`, `000000`, `FFFFFF`, `EAEAEA`, `D4D4D4`

**Slide map (read via PowerPoint MCP):**

| # | Title / Topic |
|---|---------------|
| 1 | Title — "AI BioMedical Foundation" |
| 2 | Bioimaging ML – Computer vision (image-only) |
| 3 | Bioimaging ML – Computer vision (workflow: virtual staining, cell counting, denoising, DINOv2) |
| 4 | Label-Free AI Foundation Model Workflow + Heart-on-a-chip |
| 5 | iPSCs expansion — DINOv2, Semi-siamese U-Net, QC1 metrics |
| 6 | iPSCs differentiation — same model stack, QC2 |
| 7 | Video data (timelapse) — V-JEPA |
| 8 | Video data (cardiomyocytes) — V-JEPA |
| 9 | Video data (microtissues) — pilar detection, contractility analysis |
| 10 | Organ-on-chip — QC4, vasculature network/permeability, virtual staining |
| 11 | Test Example N19 |
| 12 | Models of interest — DINOv2, V-JEPA, Diffusion model |
| 13 | Datasets — 7000 pairs SOX2-GFP, 3400 pairs MYL2/ETB2-TRITC, 54 pairs, etc. |
| 14 | Thank you — ACCELERATION@UTORONTO.CA |
| 15 | (Hidden) Extended graph colour palette reference |

When editing or extending: open `ML.pptx` as the base. Match font and colour scheme exactly.
When creating from scratch: reproduce this theme via pptxgenjs using `AC_COLORS` above.

---

## Academic Content Standards

### Step 1 — Identify Mode

**Research / academic (default for AC lab presentations):**
Use for: conference papers, seminar talks, grant briefings, lab meetings, thesis defenses, internal progress updates.
Priority: argument structure → data → layout → aesthetics.

**Science communication / outreach:**
Use for: public engagement, industry briefings to non-specialists, recruitment events.
Visual storytelling takes priority. Still apply AC brand. Relax action-title rule.

When in doubt: default to research mode.

### Step 2 — Plan the Deck First

Produce a slide-by-slide outline before building:
- Slide number, action title, exhibit type
- Ghost deck test: read action titles in sequence — they must tell the complete argument alone

Confirm with user if deck > 10 slides or content is complex. Do not build until outline agreed.

### Step 3 — Argument Structure

Choose one narrative spine:

**Option A — Situation / Complication / Resolution (SCR)** *(default)*
- Situation: what was known
- Complication: what was missing or broken
- Resolution: what your work contributes

**Option B — Funnel + Answer**
- Broad context → specific gap → approach → key findings → implications

**Option C — Answer First** *(for grant panels, advisory boards, short talks)*
- Lead with conclusion, then support it

One argument per presentation. If you're tempted to present the whole paper: pick the claim that can be made convincingly in the time available. Everything else → appendix.

### Step 4 — Action Titles

Every content slide title = complete sentence stating the takeaway.

| Instead of (topic label) | Use (action title) |
|--------------------------|-------------------|
| Results | Treatment effect is significant across all three cohorts |
| Methods | Regression discontinuity exploits a sharp eligibility threshold |
| Bioimaging | Virtual staining achieves 94% accuracy vs. ground-truth GFP |
| Discussion | Effect persists after controlling for selection and attrition |

Title font: Arial Black, 28 pt, black. One to two lines maximum.

### Step 5 — Per-Slide Rules

**One exhibit per results slide.** If two charts are needed, it's two findings, therefore two slides.

**Annotate key finding directly on the chart** — arrow, box, highlight, or call-out label in AC orange (`FF3D00`).

**Figure placement:** Figure LEFT (~60% of slide width), interpretive bullets RIGHT (~35%).

**Body text maximum:** ~40 words per content slide. Body text is for orientation, not information transfer — the presenter carries the argument.

**Body text minimum font size:** 20 pt. If text does not fit at 20 pt, remove content.

**Citations:** Every borrowed figure, dataset, or claim cited on the slide (bottom, Arial, 13 pt, gray). Full references on the References slide.

### Required Slide Architecture

In order:

1. **Title slide** — presentation title (statement or question), author + affiliation, venue, date, AC/U of T lockup
2. **Motivation / Context** (1–2 slides) — why this problem matters; situation + complication
3. **Research Question** (1 slide) — state it explicitly, on its own slide
4. **Methods** (1–2 slides) — only what the audience needs to evaluate findings; detail → appendix
5. **Results** (one finding per slide) — one exhibit each, action title states the finding
6. **Discussion / Implications** (1–2 slides) — interpret findings, connect back to opening, address main limitation
7. **Conclusions** (1 slide) — 2–4 bullets restating key takeaways; **stays on screen during Q&A**
8. **Contact / Next Steps** — email, QR code, or URL; may be combined with Conclusions
9. **References** — complete citations for all in-deck sources
10. **Appendix** — pre-built Q&A slides, robustness checks, extra data; label each slide (e.g., "Appendix A")

**Never follow Conclusions with a "Thank You" slide or blank slide.**

### Slide Budget

| Talk length | Content slides (excl. title + refs) |
|-------------|--------------------------------------|
| 10 min | 8–10 |
| 15 min | 12–14 |
| 20 min | 15–18 |
| 45 min seminar | 30–40 |

Target finishing 1–2 minutes under the allotted time.

---

## PptxGenJS Implementation (AC Style)

```javascript
const PptxGenJS = require("pptxgenjs");
const pres = new PptxGenJS();
pres.layout = "LAYOUT_WIDE";  // 13.33 x 7.50

const C = {
  black:    "000000",
  orange:   "FF3D00",
  gray:     "D4D4D4",
  grayDark: "515151",
  grayMid:  "919191",
  grayLight:"EAEAEA",
  white:    "FFFFFF",
};

const F = {
  face:    "Arial",
  eyebrow: "Courier New",
  title:   28,
  body:    20,
  label:   16,
  cite:    13,
};

const M = 0.5;  // margin inches
```

### Reusable Helpers

```javascript
// Footer: "ACCELERATION CONSORTIUM" bottom-left + page number bottom-right
// Call on every slide
function addACFooter(slide, pageNum) {
  slide.addText("ACCELERATION CONSORTIUM", {
    x: M, y: 7.15, w: 6.0, h: 0.25,
    fontSize: 9, fontFace: F.eyebrow, color: C.grayMid, align: "left"
  });
  slide.addText(String(pageNum), {
    x: 12.6, y: 7.15, w: 0.5, h: 0.25,
    fontSize: 9, fontFace: F.eyebrow, color: C.grayMid, align: "right"
  });
}

// Orange dot (●) section marker + label beside it
// e.g. addSectionDot(slide, "WHAT TO DO", 0.5, 1.2)
function addSectionDot(slide, label, x, y) {
  slide.addShape(pres.ShapeType.ellipse, {
    x: x, y: y + 0.02, w: 0.18, h: 0.18,
    fill: { color: C.orange }, line: { color: C.orange }
  });
  slide.addText(label, {
    x: x + 0.26, y: y, w: 4.0, h: 0.22,
    fontSize: 11, fontFace: F.eyebrow, color: C.black,
    bold: true, align: "left"
  });
}
```

---

### Title Slide Pattern (AC)

```javascript
// Black background — AC brand treatment for cover slides
slide.background = { color: C.black };

// Eyebrow label (Courier New, orange)
slide.addText("ACCELERATION CONSORTIUM  ·  UNIVERSITY OF TORONTO", {
  x: M, y: 0.4, w: 12.3, h: 0.3,
  fontSize: 11, fontFace: F.eyebrow, color: C.orange,
  align: "left"
});

// Thin orange rule
slide.addShape(pres.ShapeType.rect, {
  x: M, y: 0.75, w: 12.3, h: 0.04,
  fill: { color: C.orange }, line: { color: C.orange }
});

// Main title
slide.addText("Your Presentation Title as a Statement or Question", {
  x: M, y: 1.1, w: 10.0, h: 2.5,
  fontSize: 38, fontFace: F.face, fontWeight: "Black", color: C.white,
  bold: true, align: "left", valign: "top"
});

// Author + affiliation
slide.addText("Author Name  ·  Acceleration Consortium, University of Toronto", {
  x: M, y: 4.0, w: 10.0, h: 0.4,
  fontSize: 16, fontFace: F.face, color: C.gray, align: "left"
});

// Venue + date
slide.addText("Conference Name  ·  May 2026", {
  x: M, y: 4.45, w: 10.0, h: 0.35,
  fontSize: 14, fontFace: F.face, color: C.grayMid, align: "left"
});

// Logo placeholder — bottom right
// slide.addImage({ path: "ac_lockup.png", x: 10.5, y: 6.8, w: 2.5, h: 0.5 });
```

### Content Slide Pattern (AC)

```javascript
// White background
slide.background = { color: C.white };

// Eyebrow (optional — use for section context)
slide.addText("RESULTS", {
  x: M, y: 0.15, w: 12.3, h: 0.25,
  fontSize: F.cite, fontFace: F.eyebrow, color: C.grayMid,
  align: "left"
});

// Action title — ORANGE on white background slides (confirmed from visual frames)
slide.addText("Virtual staining achieves 94% accuracy vs. ground-truth GFP across all cell lines", {
  x: M, y: 0.4, w: 12.3, h: 0.9,
  fontSize: F.title, fontFace: F.face, color: C.orange, bold: true, valign: "top"
});

// Thin gray divider
slide.addShape(pres.ShapeType.rect, {
  x: M, y: 1.3, w: 12.3, h: 0.025,
  fill: { color: C.gray }, line: { color: C.gray }
});

// Figure (left ~60%)
// slide.addImage({ path: "result_chart.png", x: M, y: 1.4, w: 7.5, h: 5.0 });

// Key finding annotation — AC orange
slide.addShape(pres.ShapeType.roundRect, {
  x: 0.6, y: 1.5, w: 2.2, h: 0.5,
  fill: { color: C.orange }, line: { color: C.orange }, rectRadius: 0.06
});
slide.addText("↑ 94% accuracy", {
  x: 0.6, y: 1.5, w: 2.2, h: 0.5,
  fontSize: 14, fontFace: F.face, color: C.white, bold: true,
  align: "center", valign: "middle"
});

// Sub-heading within slide — BLACK (not orange)
slide.addText("Key takeaways", {
  x: 8.5, y: 1.4, w: 4.3, h: 0.35,
  fontSize: 16, fontFace: F.face, color: C.black, bold: true
});
slide.addText([
  { text: "Outperforms prior methods by 12 pp on held-out test set", options: { breakLine: true } },
  { text: "Robust across brightfield and phase contrast inputs", options: { breakLine: true } },
  { text: "Inference time: 0.3 s per frame on A100", options: { breakLine: true } },
], {
  x: 8.5, y: 1.85, w: 4.3, h: 3.5,
  fontSize: F.body - 1, fontFace: F.face, color: C.black,
  bullet: true, paraSpaceAfter: 12
});

// Citation
slide.addText("Smith et al. (2025), Nature Methods", {
  x: M, y: 7.1, w: 12.3, h: 0.3,
  fontSize: F.cite, fontFace: F.face, color: C.grayDark
});
```

### Conclusions Slide Pattern (AC)

```javascript
// Black background — mirrors title slide (sandwich)
slide.background = { color: C.black };

// "Conclusions" eyebrow
slide.addText("CONCLUSIONS", {
  x: M, y: 0.35, w: 12.3, h: 0.3,
  fontSize: 12, fontFace: F.eyebrow, color: C.orange, align: "left"
});

// Orange rule
slide.addShape(pres.ShapeType.rect, {
  x: M, y: 0.7, w: 12.3, h: 0.04,
  fill: { color: C.orange }, line: { color: C.orange }
});

// Key takeaways — numbered, bold lead
slide.addText([
  { text: "1. Virtual staining generalises: ", options: { bold: true, breakLine: false } },
  { text: "94% accuracy across all cell lines; closes gap with immunofluorescence.", options: { breakLine: true, breakLine: true } },
  { text: "2. Diffusion models outperform U-Net baselines: ", options: { bold: true, breakLine: false } },
  { text: "12 pp gain at 10× lower acquisition cost.", options: { breakLine: true, breakLine: true } },
  { text: "3. Pipeline is deployment-ready: ", options: { bold: true, breakLine: false } },
  { text: "0.3 s/frame inference, validated on AC SDL hardware.", options: {} },
], {
  x: M, y: 0.9, w: 12.3, h: 5.0,
  fontSize: F.body + 1, fontFace: F.face, color: C.white,
  paraSpaceAfter: 22
});

// Contact
slide.addText("yourname@mail.utoronto.ca  ·  acceleration.utoronto.ca  ·  preprint: bit.ly/xxx", {
  x: M, y: 6.8, w: 10.0, h: 0.4,
  fontSize: 14, fontFace: F.face, color: C.gray, align: "left"
});
```

---

## QA Checklist

Run after every build. No release until full pass.

```
ACADEMIC CONTENT:
□ Every content slide has an action title (complete sentence, states the takeaway)
□ Ghost deck test passes (action titles alone tell the full argument)
□ One exhibit per results slide; each exhibit has a "so what" annotation
□ Every borrowed figure or data point has an in-slide citation
□ References slide exists at the end
□ Conclusions slide is the last non-appendix slide
□ Contact info and/or QR code on final slide
□ Font sizes ≥ 20 pt body text throughout
□ No slide has > ~40 words of body text
□ Appendix slides exist for anticipated Q&A

AC BRAND:
□ Colours limited to: #000000, #FF3D00, #D4D4D4, #FFFFFF, and approved grays
□ No colour outside AC palette
□ Slide titles (action titles) are ORANGE (#FF3D00) on white-background slides
□ Sub-headings within slides are BLACK on white-background slides
□ Body text BLACK on white slides, WHITE on black slides
□ Arial Black/Bold headings, Arial Regular body (universal fallback)
□ Eyebrow/footer text in Courier New (IBM Plex Mono is brand font)
□ Footer "ACCELERATION CONSORTIUM" + page number on every slide
□ Orange dot marker (●) used before ALL CAPS section labels where appropriate
□ No decorative icons, clip art, illustration-style imagery, or AI-cliché art
□ Logo (U of T left / AC right, thin rule separator) on title slide
□ Slide size is 13.33" × 7.50"
□ White background on content slides; black only on title/section dividers/closing slides
□ Abstract macro imagery (crystals, materials) on dark slides — use sparingly

TECHNICAL:
□ Content verified via markitdown extraction
□ Visual verified via slide images (pdftoppm)
□ All images load (no broken paths)
□ Font embedding enabled if distributing externally
```

---

## AC Brand Voice (for slide copy)

When writing text for AC slides:

- **Tone:** Empowering, inspiring, inclusive. Avoid jargon-heavy or inaccessible language.
- **Language:** Clear, concise, active voice, strong verbs.
- **Bullets:** Telegraphic is fine — drop articles and filler when meaning is preserved.
- **Messaging themes:** Empowerment, opportunity, impact. Connect research to real-world effect on sustainable materials, health, energy.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Topic labels as titles | Write action titles (complete sentence) |
| Whole-paper presentation | One argument; rest to appendix |
| Non-AC colours | Restrict to `000000`, `FF3D00`, `D4D4D4`, `FFFFFF` |
| Slide title is black on white | Slide titles must be ORANGE (`FF3D00`) on white-BG slides |
| Sub-heading is orange | Sub-headings within a slide must be BLACK |
| Missing footer | Add "ACCELERATION CONSORTIUM" + page number, every slide |
| Decorative icons | Delete; use data, abstract macro imagery, or real photos only |
| Logo missing | Add U of T + AC lockup to title slide |
| Font outside palette | Switch to Arial / Courier New |
| Reading slides aloud | Slides carry evidence; presenter carries argument |
| No "so what" on chart | Annotate key finding in AC orange |
| No citation on borrowed figure | Cite on slide; full ref on References slide |
| Body text < 20 pt | Remove content until it fits at 20 pt |
| Ending on "Thank You" | End on Conclusions; it stays up during Q&A |
| Wrong slide size | Use 13.33" × 7.50" (LAYOUT_WIDE in pptxgenjs) |

---

## Dependencies

```bash
pip install "markitdown[pptx]"     # text extraction and QA
npm install -g pptxgenjs            # create from scratch
brew install libreoffice            # PDF conversion
brew install poppler                # PDF to images (pdftoppm)
```
