---
tags:
  - literature
  - type/paper
  - lit/sdl
type: literature-note
source_note: "Papers/Paper - AI Agent Safety.md"
source_pdf: "/Users/iyakavets/Downloads/Sorted_2026-05-09/PDFs/Research_Papers/AI Agent Safety.pdf"
converter: "microsoft/markitdown"
---
Safety in Autonomous Self-driving Chemistry Labs

An  AI  agent  powered  by  a  large  language  model  (open-source  or  closed-source),  will
orchestrate  the  self-driving  labs  (SDLs),  where  the  experimental  chemist  can  order  the
experiment as natural language text as an actionable message on Slack/Discord. Additional
physics and chemistry knowledge are incorporated into the workflow by giving it access
to physics-based models, physics-informed data-driven models, Internet, online chemical
databases, published research articles, and chemical safety resources.

Figure 1- Proposed Intelligent Self-driving Lab Orchestrator (Tool 3 is the main focus of this study).

This proposed intelligent orchestrator will account for the safety measures within each sdl
by obtaining live information from the safety sensors and aborting the experiment in case
of  experiment  failures.  These  failures  and  safety  concerns  could  come  from  various
attributes, including the hazardous toxic building blocks and reaction intermediates or the
physical lab environment, due to equipment failure. This module also supports an on-the-
fly  human-in-the-loop  feedback  cycle,  offering  assistance  to  the  domain-expert
experimentalists  by  mitigating  potential  oversights  and  reducing  the  impact  of  human
error. One of the key advantages of this tool is eliminating the need for manual handling.
However,  for  tasks  involving  sensitive  operations,  the  workflow  can  be  hardcoded  to
ensure more reliability.

Additional References

1.  https://arxiv.org/abs/2410.03963
2.  https://doi.org/10.26434/chemrxiv-2024-2qx28
