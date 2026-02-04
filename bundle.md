---
bundle:
  name: scientificpaper
  version: 1.0.0
  description: "AI-assisted scientific paper authoring with LaTeX, figure generation, and multi-conference formatting"

includes:
  - github:microsoft/amplifier-foundation/bundle.md

behaviors:
  include:
    - scientificpaper:behaviors/latex-authoring
    - scientificpaper:behaviors/figure-generation
    - scientificpaper:behaviors/conference-styling
---

# Scientific Paper Bundle

AI-assisted workflow for creating publication-ready scientific papers.

## Key Capabilities

- **Multi-conference LaTeX formatting** - NeurIPS, ICML, IEEE, ACL, ACM, arXiv, Stanford CS
- **AI-powered figure generation** - Matplotlib, TikZ, PlotNeuralNet, Mermaid
- **Paper structure planning** - IMRaD methodology (Introduction, Methods, Results, Discussion)
- **Citation management** - BibTeX generation, style conversion, reference validation
- **LaTeX compilation and debugging** - Automated compilation with helpful error diagnostics

## Philosophy

Following Amplifier's **"mechanism, not policy"** approach - this bundle provides composable tools without dictating specific workflows. Choose your own paper structure, conference format, and figure generation approach.

## Usage Examples

### Create a new paper
```
"Create a NeurIPS paper on transformer efficiency"
```

### Generate figures
```
"Create a matplotlib plot showing training loss curves and convert to TikZ"
```

### Convert between conferences
```
"Convert my NeurIPS paper to ICML format"
```

### Manage citations
```
"Add a BibTeX entry for this DOI: 10.1234/example"
```

## Available Agents

This bundle provides four specialized agents (context sinks):

- **paper-architect** - Paper structure and outline planning
- **figure-artist** - Publication-ready figure generation with quality veto rules
- **latex-expert** - LaTeX compilation, formatting, and conference conversion
- **citation-manager** - Bibliography management and citation style conversion

These agents are automatically available when using this bundle. Amplifier will delegate to them as needed.

## Variants

Pre-composed bundle variants are available in `bundles/`:

- **`bundles/with-gemini.md`** - Adds Gemini API for conceptual figure generation
- **`bundles/latex-only.md`** - Pure LaTeX workflow without figure generation
- **`bundles/neurips-focused.md`** - Optimized for NeurIPS papers

## Requirements

### Python Packages
```bash
pip install matplotlib seaborn tikzplotlib pypdf requests bibtexparser
```

### System Dependencies
- LaTeX distribution (TeX Live 2023+ recommended)
- pdflatex, bibtex, latexmk

### Optional
- `GOOGLE_API_KEY` environment variable (for with-gemini variant)
- Inkscape (for advanced SVG conversion)

## Design Principles

- **Thin bundle** - Inherits all tools from foundation (bash, filesystem, etc.)
- **Context sinks** - Heavy documentation loaded only when agents spawn
- **Template-based** - Official conference style files in `templates/`
- **Script-driven** - Deterministic operations via Python scripts in `scripts/`
- **Composable** - Mix and match behaviors and variants

## Getting Started

1. **Install requirements**: `pip install -r requirements.txt`
2. **Run Amplifier**: `amplify --bundle @scientificpaper`
3. **Create your first paper**: `"Create a NeurIPS paper on [your topic]"`

For detailed architecture and implementation notes, see `ARCHITECTURE.md`.
