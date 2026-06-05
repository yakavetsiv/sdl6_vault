---
title: Deslop — Writing Style Reference
date: 2026-06-04
type: skill-reference
tags:
  - ai
  - type/skill
  - sdl6
  - writing
  - deslop
  - style
  - AI-patterns
  - scientific-writing
---

# Deslop — Writing Style Reference

**Skill path:** `~/.claude/plugins/cache/deslop/deslop/a906154bef375d9d49ed2ad7da13b2db16f0d3d2/skills/deslop/`  
**Plugin:** `deslop` (stephenturner/skill-deslop)  
**Trigger:** "deslop", "de-AI", "make it sound human", "remove AI patterns"

---

## Core Rule

State Y directly. Drop the negation. Name the actor. Use simple verbs. Vary sentence length.

---

## Structures to Avoid

### Binary Contrasts — #1 AI tell
"Not X. But Y." / "It's not X — it's Y." / "stops being X and starts being Y"  
**Fix:** State Y. Drop the negation entirely.

### Negative Listing
"Not a bug. Not a feature. A design flaw."  
**Fix:** State Z. Reader needs no runway.

### Dramatic Fragmentation
"Speed. Quality. Cost. That's it. That's the tradeoff."  
**Fix:** "Speed, quality, cost: pick two." Complete sentences.

### Self-Posed Rhetorical Questions
"The result? Devastating." / "The worst part? Nobody saw it coming."  
**Fix:** Make the point. Cut the setup.

### Anaphora Abuse
"They assume... They assume... They assume..."  
**Fix:** Vary openings. Combine related points.

### Tricolon Abuse
Three-item lists everywhere. One or two items.

### False Agency
"the data tells us" / "the decision emerges" / "the culture shifts"  
**Fix:** Name the human doing the thing.

### Superficial Participle Analysis
Tacking "-ing" phrases to signal shallow significance:  
"...contributing to the region's rich cultural heritage"  
"...highlighting its enduring legacy"  
**Fix:** Make a specific claim or delete it.

### False Ranges
"From innovation to cultural transformation" — no real spectrum.  
**Fix:** If it's a list, list it.

### "Despite Its Challenges..."
Acknowledge problems only to dismiss them. Same beat every time.  
**Fix:** Analyze challenges or skip them.

### Listicle in a Trench Coat
"The first wall is... The second wall is... The third wall is..."  
**Fix:** If it's a list, format it as one.

### One-Point Dilution
Same argument restated 10 ways across 4000 words.  
**Fix:** State once, support once, move on.

### Fractal Summaries
Tell → say → summarize. At every level.  
**Fix:** Write. Don't announce what you're writing.

---

## Phrases to Remove

### Throat-Clearing Openers — Delete
- "Here's the thing:" / "Here's the deal" / "Here's the kicker"
- "The uncomfortable truth is" / "The truth is,"
- "Let me be clear" / "I'll say it again:"
- "It turns out"

### Emphasis Crutches — Delete
- "Full stop." / "Let that sink in."
- "Make no mistake" / "Here's why that matters"

### Pedagogical Hand-Holding — Delete
- "Let's break this down" / "Let's unpack this" / "Let's dive in"
- "Think of it as..." / "Imagine a world where..."

### Business Jargon → Plain Language
| Avoid | Use |
|---|---|
| Navigate challenges | Handle, address |
| Leverage (verb) | Use |
| Utilize | Use |
| Robust | Strong, solid |
| Streamline | Simplify |
| Landscape (for field/situation) | Field, situation |
| Paradigm | Model, approach |
| Ecosystem | System, field |
| Framework | Structure, approach |
| Game-changer | Important |
| Deep dive | Analysis |
| Moving forward | Next |

### AI Vocabulary Tells — Replace
- "delve" → examine, look at
- "tapestry" → mix, combination, range
- "certainly" → delete
- "nuanced" → complex, subtle, specific
- "serves as" / "stands as" / "marks" / "represents" → is

### Adverbs — Kill All -ly Words
really, just, literally, genuinely, honestly, simply, actually, deeply, truly, fundamentally, inherently, inevitably, interestingly, importantly, crucially, quietly, remarkably, arguably

Also cut: "At its core" / "In today's X" / "It's worth noting" / "Notably" / "At the end of the day"

### Meta-Commentary — Remove
- "In this section, we will..." / "As we'll see..." / "Let me walk you through..."
- "In conclusion" / "To sum up" / "In summary"
- "And so we return to where we began."

### Vague Declaratives — Replace with Specifics
- "The reasons are structural" → name the structure
- "The implications are significant" → name the implication
- "The stakes are high" → name the stake

### Vague Attributions — Name the Source or Cut
- "Experts argue that..." — name the expert
- "Industry reports suggest..." — cite the report

---

## Formatting Tells
- **Bold-first bullets** — every bullet starts bolded = AI signal
- Em-dash addiction — 2-3 max per piece; AI uses 20+
- Unicode arrows (→) — use `->` or plain text
- Smart/curly quotes — use straight quotes

---

## Before/After Examples (Key)

**Throat-clearing + binary contrast:**  
❌ "Here's the thing: forecasting is hard. Not because the models are complex. Because the data is complex. Let that sink in."  
✓ "Forecasting infectious disease is hard. The models are tractable. The data, collected under shifting surveillance definitions and reporting lags, is not."

**Superficial participle + serves-as:**  
❌ "The FluSight initiative serves as a foundational framework, contributing to public health preparedness and underscoring the importance of collaborative forecasting."  
✓ "The FluSight initiative coordinates influenza forecasting across dozens of modeling groups. Since 2013, it has standardized targets, submission formats, and evaluation metrics."

**Passive + false agency:**  
❌ "It was observed that performance degraded. The uncertainty naturally increased. Results emerged from our analysis."  
✓ "We observed performance degraded at longer horizons. Each additional week added roughly 15% to the mean WIS."

**Anaphora (grant narrative):**  
❌ "We will develop novel methods. We will apply these methods. We will validate findings. We will disseminate tools. We will train students."  
✓ "We will develop and validate statistical methods for multi-ancestry fine-mapping using UK Biobank and TOPMed cohorts, then release them as an R package with documentation and tutorials."

**One-point dilution:**  
❌ "Reproducibility matters. Reproducibility is the most underrated quality. When you make analyses reproducible, you reduce errors. Fewer errors mean more trust. [5 more sentences saying the same thing]"  
✓ "Reproducible analyses catch errors earlier. When Beaulieu-Jones and Greene re-ran 68 papers, only 40% reproduced. The ones that failed had no shared code or pinned dependency versions."

---

## Quick Checklist

Before submitting any prose:
- [ ] No "not X, but Y" constructions
- [ ] No trailing "-ing" analysis phrases
- [ ] No em-dashes (max 2 per page)
- [ ] No adverbs
- [ ] No throat-clearing openers
- [ ] All actors named (no passive voice)
- [ ] No vague declaratives — every claim has a specific fact
- [ ] Paragraph lengths vary (not all 4-5 sentences)
- [ ] No three-item lists where one or two would do

---

## Related
- [[vault-dump-skill]] — session dump
- [[claude-skills]] — all installed skills
