---
bundle:
  name: latex-authoring
  version: 1.0.0
  description: "LaTeX authoring, compilation, and conference formatting capabilities. Composes latex-expert and paper-architect agents for comprehensive LaTeX workflow support."

agents:
  include:
    - scientificpaper:latex-expert
    - scientificpaper:paper-architect

context:
  include:
    - scientificpaper:context/latex-awareness.md
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
- Structure planning -> @paper-architect
- Compilation and formatting -> @latex-expert
