---
meta:
  name: conference-styling
  description: Multi-conference formatting and style application
agents:
  - agents/latex-expert.md
  - agents/citation-manager.md
context:
  - context/conference-formats/neurips.md
  - context/conference-formats/icml.md
  - context/conference-formats/acl.md
  - context/conference-formats/ieee.md
  - context/conference-formats/acm.md
  - context/conference-formats/arxiv.md
---

# Conference Styling Behavior

Applies correct formatting for major scientific conferences.

## Supported Conferences
- NeurIPS - 8 pages, Times 10pt
- ICML - 8 pages, two-column
- ACL - A4 only, natbib
- IEEE - Letter/A4, numbered citations
- ACM - Single-column review
- arXiv - TeX recommended

## Agent Delegation
- Format application → @latex-expert
- Citation styling → @citation-manager
