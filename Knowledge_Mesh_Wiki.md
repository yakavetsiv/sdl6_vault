## 🧠 AI Software Knowledge Mesh: CodeWiki Concept Draft

**Status:** Prototype Knowledge Base (Requires Linkgrounding)
**Goal:** Transform raw, distributed source code and ephemeral documentation (social media) into a persistent, interconnected, and queryable knowledge graph.
**Inspiration:** CodeWiki (Google/GitHub Concept)
**Core Principle:** The living software artifact is the ultimate source of truth; documentation must be derived *from* it, not *about* it.

---

## 🔗 Overview: The Knowledge Mesh (The "Skyline" View)

The primary failure point in software knowledge is the gap between **`Code`** (the source of truth) and **`Documentation`** (the interpretation). A Knowledge Mesh aims to close this gap using AI to create a continuous loop:

`Code` $\xrightarrow{\text{Diff/Analyze}}$ `Knowledge Embeddings` $\xrightarrow{\text{Query/Refine}}$ `Documentation`

### 🛠️ Core Tool Flow (API Layer Documentation)
This section documents the procedural steps needed to interact with a local Obsidian vault using the REST API. This process acts as a *how-to* guide for system interaction.

*   **Vault Root Listing:** Requires a valid API Key (`Authorization: Bearer <key>`).
    *   *Endpoint:* `GET https://127.0.0.1:27124/vault/`
    *   *Libraries:* Used basic HTTP requests (`curl`).
*   **Targeted Reading/Writing:** APIs allow granular control, avoiding the "rewrite whole file" problem.
    *   *Action:* PATCH/PUT/POST
    *   *Target:* Heading (`/heading/My%20Section`), Frontmatter (`/frontmatter/status`), Block.
    *   *Benefit:* High atomic precision for updates (e.g., simply appending a line to a specific heading).

---

## 🚀 Primary Knowledge Domain: CodeWiki Deep Dive

CodeWiki is not merely a documentation site; it is an **active computational layer** over the codebase.

### Key Features & Concepts

1.  **Interactive Guide Generation:**
    *   The system ingests the entire repo structure and dependencies.
    *   It automatically generates an *onboarding path* that simulates traversing the code, perfect for new hires or complex feature explorations.
2.  **Automated Visualization:**
    *   Goes beyond simple file trees. It automatically generates visual diagrams:
        *   **Sequence Diagrams:** To show function call order (`A` calls `B` which triggers `C`).
        *   **Architecture Diagrams:** To define component boundaries and communication protocols.
        *   **Data Flow Diagrams:** Tracing data from input to output across various services.
3.  **Contextual Chatbot (The "Know-It-All"):**
    *   This is the most advanced feature. The LLM is given the entire codebase context *and* the documentation context.
    *   **Example Query:** "Why does the user get a 403 error on the payment API endpoint when the local test data shows 200?"
    *   **System Response:** *[Reads relevant code block]*, *[References a specific design doc in the vault]*, *[Highlights the missing permission step]*.

### 📘 The Karpathy Synthesis (Bridging Disciplines)

As an architectural concept, CodeWiki requires the convergence of three disciplines:

| Discipline | Function | Required Tech | Linked Obsidian Concept |
| :--- | :--- | :--- | :--- |
| **Static Code Analysis** | Understanding structure (AST, dependency graph). | Tree-sitter, Python `ast` | [[Codebase Inspection]] |
| **Knowledge Graphing** | Connecting *concepts* (e.g., 'Authentication' $\rightarrow$ 'OAuth' $\rightarrow$ 'Token Flow'). | Neo4j, Semantic Search | [[Structured Notes]] |
| **Intent/Pillar Extraction** | Figuring out *why* the code is written (the business need). | LLM (Zero-Shot Classification) | [[Project Scope & Goals]] |

---

## 🔬 Future Connection & Next Steps (Actionable Tasks)

To bring this wiki draft to life, we need to perform the following tasks, which should be added to the `TODO` list:

1.  **Grounding:** Populate the Knowledge Mesh with the READMEs and high-level summaries of the files found in the vault (`input.md` and `Welcome.md`).
    *   *Action:* Read contents of `/Users/iyakavets/Documents/obsidian/viprorok/Welcome.md` and synthesize its purpose.
2.  **Source Integration:** Identify related open-source projects/GitHub repos that implement components similar to CodeWiki.
    *   *Action:* Targeted search on GitHub using `github-search` skills or targeted web research.
3.  **Testing:** Create a proof-of-concept workflow to trace a simple, known bug in a local example project, documenting every analysis step using the structured wiki format.

***
**💡 Wiki Status:** The framework is complete, defining the 'what' and the 'how'. The next phase is the heavy lifting of data ingestion and linking to ground the theory in your actual work.
"

---

## 🤖 AI Tools & Agents Layer

Saved resources, tools, and agent patterns collected in May 2026 — structured as a queryable knowledge graph.

Start here: [[Map - AI Tools and Agents (May 2026)]]

Key nodes:
- [[Agent Architecture]] · [[Agent Memory]] · [[Agent From Scratch]]
- [[Deep Research Tools]] · [[Open AI Scientists]]
- [[Claude Code Memory Systems]] · [[Obsidian AI Integration]]

---

## 📚 Literature Wiki Layer

The research-paper graph seed lives at [[Literature Wiki Home]]. It indexes the sorted research PDFs into paper notes, concept pages, map-of-content pages, and graph export files for later knowledge-graph tooling.

Start here: [[Literature Wiki Home]]

Key maps:
- [[Map - Self-Driving Lab Stack]]
- [[Map - Biofabrication and Cell Systems]]
- [[Map - AI for Bioimage Analysis]]
- [[Map - Materials and Therapeutics]]

