---
bundle:
  name: figure-generation
  version: 1.0.0
  description: "AI-assisted scientific figure creation with quality veto rules. Composes figure-artist agent for publication-ready visualizations."

agents:
  include:
    - scientificpaper:figure-artist

context:
  include:
    - scientificpaper:context/figure-generation-awareness.md
---

# Figure Generation Behavior

Enables creation of publication-quality scientific figures.

## Supported Figure Types
- Mathematical plots and charts
- Architecture and flow diagrams
- Neural network visualizations
- Statistical graphics
- Schematic illustrations

## Tool Selection Matrix
| Type | Primary | Alternative |
|------|---------|-------------|
| Plots | Matplotlib | PGFPlots |
| Diagrams | Mermaid | Graphviz |
| Math | TikZ | SVG |
| Complex | Gemini API | - |

## Agent Delegation
All figure requests -> @figure-artist
