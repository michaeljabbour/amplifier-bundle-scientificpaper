---
meta:
  name: figure-generation
  description: Scientific figure and diagram creation capabilities
agents:
  - agents/figure-artist.md
context:
  - context/imaging/matplotlib-scientific.md
  - context/imaging/tikz-patterns.md
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
All figure requests → @figure-artist
