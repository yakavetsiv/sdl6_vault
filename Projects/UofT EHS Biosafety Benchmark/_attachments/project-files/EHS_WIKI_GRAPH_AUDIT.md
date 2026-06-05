# EHS Wiki Graph Audit

Date: 2026-05-10

## Verdict

The Obsidian EHS Wiki is connected enough for the current biosafety QA dataset builder, because the builder reads source text directly from `Pages/` and `PDF Notes/`.

It is not yet connected enough to be a strong semantic knowledge graph. The current graph is mostly hub-and-spoke: topic/index notes link outward to many files, while scraped EHS pages are mostly leaf notes with little or no outgoing semantic linkage.

## Snapshot

Initial audit, before the first semantic-link rebuild:

- Markdown notes: 378
- Root/index notes: 3
- `Pages/`: 137
- `PDF Notes/`: 228
- `Topics/`: 10
- Wikilinks found: 3,482
- Broken wikilinks: 1
  - `EHS Wiki Home.md` links to missing `[[Resources]]`
- Fully isolated notes: 0
- Notes with no incoming links: 1
  - `EHS Knowledge Graph Index.md`
- Low-degree notes: 134

After the first biosafety semantic-link pass:

- Curated notes updated: 28
- Missing mapped notes: 0
- Missing link targets: 0
- Script idempotency check: clean, 0 pending changes after write
- `Pages/` average outgoing links: 1.12
- `Pages/` average incoming links: 2.53
- `PDF Notes/` average outgoing links: 4.65
- `PDF Notes/` average incoming links: 5.39
- Core node degree examples:
  - `Biosafety Manual`: 19 outgoing, 27 incoming
  - `Biological Spills`: 10 outgoing, 18 incoming
  - `Biological Waste Disposal`: 9 outgoing, 15 incoming
  - `Decontamination`: 6 outgoing, 20 incoming
  - `Biosafety Cabinets`: 6 outgoing, 12 incoming
  - `Biosafety Permits`: 8 outgoing, 15 incoming

After the second recursive layer:

- Curated notes with `## Semantic Links`: 39
- Missing mapped notes: 0
- Missing link targets: 0
- Script idempotency check: clean, 0 pending changes after write
- `Pages/` average outgoing links: 1.67
- `Pages/` average incoming links: 3.07
- `PDF Notes/` average outgoing links: 4.65
- `PDF Notes/` average incoming links: 5.40
- Additional core node degree examples:
  - `Biosafety Manual`: 19 outgoing, 34 incoming
  - `Biological Spills`: 10 outgoing, 22 incoming
  - `Biological Waste Disposal`: 9 outgoing, 21 incoming
  - `Emergency Procedures`: 10 outgoing, 7 incoming
  - `Laboratory Waste Management`: 11 outgoing, 5 incoming
  - `Institutional Biosafety Biosecurity Committee`: 7 outgoing, 7 incoming

After duplicate cleanup:

- Markdown notes: 362
- `Pages/`: 121
- `PDF Notes/`: 228
- Remaining duplicate page-title groups: 0
- Broken wikilinks: 0
- Suffixed duplicate wikilinks: 0
- Curated notes with `## Semantic Links`: 39
- `Pages/` average outgoing links: 1.89
- `Pages/` average incoming links: 3.35

Whole-folder check after cleanup:

- Root notes: 3
- `Pages/`: 121 Markdown notes
- `PDF Notes/`: 228 Markdown notes
- `PDFs/`: 228 source files
- `Topics/`: 10 Markdown notes
- `_data/`: 9 provenance/intermediate files
- Duplicate basenames across remaining folders: 0
- `PDF Notes` with missing `source_pdf`: 0
- Duplicate `source_file` keys in `PDF Notes`: 0
- Broken wikilinks by folder: 0
- Exact normalized duplicate `PDF Notes`: 0

After root-index cleanup:

- `EHS Wiki Home.md` regenerated as a curated landing page
- `PDF Notes Index.md` regenerated from the actual `PDF Notes/` folder
- `PDF Notes Index.md` coverage: 228 of 228 PDF notes
- Broken wikilinks: 0
- Home page outgoing links: 41 total, 40 unique
- The only repeated home-page target is intentional: `Biosafety Manual` appears in both `Start Here` and `Biosafety Entry Points`

After adding Canada biosafety external references:

- Added 7 notes under `External References/`
- Added raw Crawl4AI JSON payloads under `_data/external/canada-biosafety/`
- Linked the external reference from:
  - `EHS Wiki Home.md`
  - `EHS Knowledge Graph Index.md`
  - `Topics/EHS Topic - Biosafety.md`
- Markdown files: 363
- External references: 7
- Broken wikilinks: 0
- Note status: `crawl4ai-converted`

The raw `urllib` and `curl` downloads from Canada.ca timed out or failed, but Crawl4AI fetched the pages successfully through its browser-backed crawler.

Imported Canada references:

- `Canadian Biosafety Standards and Guidelines`
- `Canadian Biosafety Standard Third Edition`
- `Biosecurity Addendum to the Canadian Biosafety Standard Third Edition`
- `Canadian Biosafety Handbook Second Edition`
- `Canadian Biosafety Guidelines`
- `Canadian Biosafety App`
- `Contact Canadian Biosafety Standards and Guidelines`

## Main Findings

### 1. Topic notes are over-broad

The topic notes create many links, but some are weak semantic matches. For example, `EHS Topic - Biosafety.md` includes respirator instructions, X-ray documents, chemical safety material, and other notes that are not strongly biosafety-specific.

This is useful for recall, but weak for graph navigation and benchmark generation because topic membership does not always mean conceptual relevance.

### 2. Scraped EHS pages are mostly leaves

`Pages/` average almost no outgoing links. Important biosafety pages such as `Biosafety Manual.md`, `Biological Spills.md`, `Biosafety Permits.md`, and `General Laboratory Safety Practices.md` mention other concepts in plain text but do not wikilink them.

Examples from `Biosafety Manual.md` that should be linked:

- `[[Biosafety Training]]`
- `[[Biological Spill Kit]]`
- `[[Decontamination]]`
- `[[General Laboratory Safety Practices]]`
- `[[Biosafety Cabinets]]`
- `[[Biosafety Permit Holder]]`
- `[[Laboratory Users]]`
- `[[Working with Laboratory Animals]]`
- `[[Fume Hoods]]`
- `[[Medical Surveillance and Immunoprophylaxis]]`
- `[[Using Needles and Syringes]]`

### 3. PDF notes rarely connect back to referring pages

227 of 228 PDF notes say no referring page was found. That means PDF notes are mostly attached through generated topic links, not through provenance links from the actual EHS page that referenced the PDF.

For graph quality, each important PDF note should ideally link to:

- its parent EHS page, when known
- one or more domain concepts
- required procedure pages
- forms/checklists it supports

### 4. Duplicate scraped pages need normalization

There are 16 duplicate page groups, including:

- `Biological Spills.md` and `Biological Spills (2).md`
- `Biological Waste Disposal.md` and `Biological Waste Disposal (2).md`
- `Emergency Procedures.md`, `Emergency Procedures (2).md`, and `Emergency Procedures (3).md`
- `Institutional Biosafety Biosecurity Committee.md` and `Institutional Biosafety Biosecurity Committee (2).md`
- `Training Matrix Laboratory Personnel.md` and `Training Matrix Laboratory Personnel (2).md`

These should be reviewed before adding many new links, otherwise links may point to inconsistent duplicates.

## Recommended Link Model

Add a curated semantic section to important notes:

```md
## Semantic Links

- Parent program: [[Biosafety Manual]]
- Related procedures: [[Biological Spills]], [[Decontamination]], [[Biological Waste Disposal]]
- Related equipment: [[Biosafety Cabinets]], [[Autoclaves Steam Sterilizers]]
- Roles: [[Biosafety Permit Holder]], [[Laboratory Users]]
- Training/forms: [[Biosafety Training]], [[Biosafety Permits]]
```

Use link labels only when the note title is awkward:

```md
- Related procedure: [[Importation Use and Distribution of Biological materials|Importation, use, and distribution of biological materials]]
```

## Priority Pass

Start with biosafety core notes:

1. `Pages/Biosafety Manual.md`
2. `Pages/Biosafety.md`
3. `Pages/Biosafety Permits.md`
4. `Pages/Biosafety Permit Holder.md`
5. `Pages/Laboratory Users.md`
6. `Pages/Biosafety Training.md`
7. `Pages/Biological Spills.md`
8. `Pages/Biological Spill Kit.md`
9. `Pages/Biological Waste Disposal.md`
10. `Pages/Decontamination.md`
11. `Pages/General Laboratory Safety Practices.md`
12. `Pages/Biosafety Cabinets.md`
13. `Pages/Autoclaves Steam Sterilizers.md`
14. `Pages/Working with Laboratory Animals.md`
15. `Pages/Importation Use and Distribution of Biological materials.md`

Then add links from high-value PDF notes:

1. `PDF Notes/PDF - Guideline-Operational-Practices-Level-2-Biosafety-Permits.md`
2. `PDF Notes/PDF - Guideline-Biosafety-Manual-and-Emergency-Response-Plan-for-Level-1-Permits.md`
3. `PDF Notes/PDF - Guideline-Biosafety-Manual-and-Emergency-Response-Plan-for-Level-2-Permits-1.md`
4. `PDF Notes/PDF - Guide-for-Completing-the-Level-1-and-2-Biosafety-Permit.md`
5. `PDF Notes/PDF - In-Lab-Procedures-for-Biological-Waste-Handling_v3.3.md`
6. `PDF Notes/PDF - Safe-Work-Practices-Aerosol-Risk-Reduction-RG2-Biological-Agents.md`
7. `PDF Notes/PDF - Lentiviral_Vectors_Guideline_2019.md`
8. `PDF Notes/PDF - Lenti_Containment_Guidance.md`
9. `PDF Notes/PDF - SARS-CoV-2-Biosafety-Guideline-for-UofT-Labs_v2.0-Sept-4-2020.md`
10. `PDF Notes/PDF - UTSC-Biological-Waste-Procedures.md`

## Recommendation

Yes: review the notes and add semantic links before relying on the graph for retrieval, graph traversal, or benchmark hard-negative generation.

Do this as a focused biosafety pass first, not a whole-wiki pass. The whole wiki is broad and noisy; the benchmark only needs a high-quality biosafety subgraph.

## Work Completed

The constrained rebuild added `## Semantic Links` sections to 39 notes:

- 18 core biosafety pages
- 10 high-value PDF notes
- 11 second-layer emergency, waste, operations, training, and governance pages

The script used for this pass is:

```bash
python3 rebuild_ehs_biosafety_semantic_graph.py --write
```

It is intentionally curated rather than fully recursive. Generated topic notes are not used as recursion drivers because they include broad and sometimes weak matches.

Duplicate cleanup was performed with:

```bash
python3 dedupe_ehs_wiki_pages.py --write
```

The cleanup kept canonical unsuffixed pages, rewrote links in `EHS Wiki Home.md`, deleted 16 true duplicate suffixed pages, and renamed the distinct biosafety-manual emergency note from `Emergency Procedures (2)` to `Biosafety Manual Emergency Procedures`.

No additional cleanup was needed for `PDF Notes`, `PDFs`, or `Topics`: their counts match and links resolve. `_data` contains scrape/conversion provenance and stage outputs, so it should be treated as lineage data rather than graph content.

Root cleanup was performed with:

```bash
python3 clean_ehs_root_indexes.py --write
```

The graph now keeps three root notes with distinct roles:

- `EHS Wiki Home.md`: curated human landing page
- `EHS Knowledge Graph Index.md`: tool/indexing entry point
- `PDF Notes Index.md`: generated inventory of converted PDF notes

Canada external reference import was performed with Crawl4AI:

```bash
python3 crawl_canada_biosafety_references.py --write
```

## Next Recursive Pass

The next pass should expand only where the second layer reveals biosafety-relevant details. Recommended additions:

- Add semantic links to selected form/checklist PDFs:
  - `PDF - Level-1-and-2-Biosafety-Permit-Application`
  - `PDF - Level-1-and-2-Biosafety-Amendment-Application-Form`
  - `PDF - Decommissioning-form-for-Biological-agents`
  - `PDF - Autoclave-SOP`
  - `PDF - Safe-Work-Practices-Safe-Sharps-Use`
- Consider fixing the remaining broken link from `EHS Wiki Home.md` to missing `[[Resources]]`.
