---
meta:
  name: latex-authoring
  description: LaTeX document creation and compilation capabilities
agents:
  - agents/latex-expert.md
  - agents/paper-architect.md
tools:
  - tool-bash
  - tool-filesystem
---

# LaTeX Authoring Behavior

Enables creation and compilation of LaTeX scientific documents.

## Capabilities
- Document structure creation
- Section and subsection management
- Table and figure environments
- Mathematical typesetting
- Bibliography integration

## Agent Delegation
- Structure planning → @paper-architect
- Compilation and formatting → @latex-expert
