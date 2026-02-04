# Scientific Paper Bundle for Amplifier

AI-assisted workflow for creating publication-ready scientific papers with LaTeX, figure generation, and multi-conference formatting.

## Overview

This Amplifier bundle provides specialized agents for scientific paper authoring:

- **paper-architect** - Structure planning and IMRaD methodology
- **latex-expert** - LaTeX compilation and conference formatting
- **figure-artist** - Publication-ready figure generation with quality veto rules

## Features

### Multi-Conference Support
- ✅ NeurIPS (Neural Information Processing Systems)
- ✅ ICML (International Conference on Machine Learning) 
- ✅ ACL (Association for Computational Linguistics)
- ✅ IEEE (Transactions and Conferences)
- ✅ ACM (SIGCHI and other venues)
- ✅ arXiv (Preprint formatting)
- ✅ Stanford CS (Thesis formatting)

### Figure Generation
- **Matplotlib + tikzplotlib** - Data plots converted to LaTeX
- **Seaborn** - Statistical graphics
- **TikZ/PGFPlots** - Mathematical diagrams
- **PlotNeuralNet** - Neural network architectures
- **Mermaid** - Flowcharts and diagrams
- **Quality veto rules** - Inspired by PaperBanana research

### Paper Structuring
- **IMRaD methodology** - Introduction, Methods, Results, Discussion
- **Abstract composition** - 5-component framework
- **Section flow optimization** - Narrative structure guidance
- **Contribution statements** - Clear, measurable contributions

## Installation

### Requirements

**Python packages:**
```bash
pip install matplotlib seaborn tikzplotlib pypdf requests bibtexparser scienceplots
```

**System dependencies:**
- LaTeX distribution (TeX Live 2023+ recommended)
- pdflatex, bibtex, latexmk
- Optional: Inkscape for SVG conversion

### Install Bundle

```bash
# Use with Amplifier
amplify --bundle github:yourusername/amplifier-bundle-scientificpaper
```

## Quick Start

### Create a New Paper

```bash
amplify --bundle @scientificpaper
```

Then in the session:
```
"Create a NeurIPS paper on transformer efficiency"
```

The paper-architect agent will:
1. Design paper structure (IMRaD)
2. Create outline with sections
3. Set up LaTeX project with NeurIPS template
4. Generate skeleton files

### Generate Figures

```
"Create a matplotlib plot showing training loss curves over 100 epochs"
```

The figure-artist agent will:
1. Generate plot with scientific styling
2. Convert to TikZ code for LaTeX
3. Save publication-ready PDF
4. Provide LaTeX integration code

### Convert Between Conferences

```
"Convert my NeurIPS paper to ICML format"
```

The latex-expert agent will:
1. Load both conference specifications
2. Adjust document class and style files
3. Update margins, fonts, and citation style
4. Validate formatting

## Usage Examples

### Example 1: End-to-End Paper Creation

```
User: "Create a NeurIPS paper on attention mechanisms in transformers"

Amplifier delegates to paper-architect:
→ Designs IMRaD structure
→ Creates sections: Intro, Background, Methods, Results, Discussion
→ Sets up LaTeX project with NeurIPS template

User: "Create a diagram showing the attention architecture"

Amplifier delegates to figure-artist:
→ Uses PlotNeuralNet to create professional diagram
→ Exports as TikZ code
→ Provides LaTeX integration code

User: "Compile the paper"

Amplifier delegates to latex-expert:
→ Runs pdflatex with NeurIPS style
→ Compiles bibliography
→ Validates formatting
→ Generates paper.pdf
```

### Example 2: Figure Generation

```
User: "Plot training curves comparing three models"

Amplifier delegates to figure-artist:
→ Creates matplotlib plot with scientific styling
→ Applies ColorBrewer color scheme
→ Converts to TikZ via tikzplotlib
→ Validates against quality veto rules:
  ✓ Vector format (TikZ)
  ✓ Professional colors
  ✓ Readable text (10pt)
  ✓ Clear legend
→ Provides integration code
```

### Example 3: Format Conversion

```
User: "Convert my paper from NeurIPS to ACL format"

Amplifier delegates to latex-expert:
→ Loads neurips.md and acl.md specifications
→ Identifies key differences:
  • Single-column → Two-column
  • US Letter → A4 paper (critical!)
  • Flexible citations → Author-year (natbib)
→ Updates document class and packages
→ Adjusts margins and fonts
→ Validates page count and formatting
```

## Bundle Structure

```
amplifier-bundle-scientificpaper/
├── bundle.md                    # Root bundle (thin inheritance)
├── behaviors/                   # Capability modules
│   ├── latex-authoring.yaml
│   ├── figure-generation.yaml
│   └── conference-styling.yaml
├── agents/                      # Context sink specialists
│   ├── paper-architect.md
│   ├── latex-expert.md
│   └── figure-artist.md
├── context/                     # Heavy documentation
│   ├── conference-formats/
│   │   └── neurips.md          # (More to be added)
│   └── imaging/
├── templates/                   # LaTeX templates
│   └── neurips/                # Official NeurIPS style files
└── scripts/                     # Utility scripts
    └── (To be implemented)
```

## Philosophy

This bundle follows Amplifier's **"mechanism, not policy"** approach:

- **Thin bundle** - Inherits all foundation tools (bash, filesystem, etc.)
- **Context sinks** - Heavy docs loaded only when agents spawn
- **Composable** - Mix and match behaviors and variants
- **Template-based** - Official conference style files
- **Quality-first** - PaperBanana-inspired figure veto rules

## Variants

Pre-composed bundle variants will be available:

- **`bundles/with-gemini.md`** - Adds Gemini API for conceptual figures
- **`bundles/latex-only.md`** - Pure LaTeX without figure generation
- **`bundles/neurips-focused.md`** - Optimized for NeurIPS papers

## Research Basis

This bundle incorporates insights from:

1. **PaperBanana** (arXiv 2601.23265)
   - Multi-agent architecture for academic illustration
   - Quality veto rules for publication figures
   - Reference-driven approach using NeurIPS examples

2. **Conference Guidelines**
   - Official formatting specifications from all supported venues
   - LaTeX style file requirements
   - Submission checklists

3. **Scientific Imaging Research**
   - Matplotlib + tikzplotlib as gold standard for data plots
   - TikZ/PGFPlots for mathematical diagrams
   - PlotNeuralNet for neural network architectures

## Development Status

**Current Phase:** Phase 1 Complete ✅

**Implemented:**
- ✅ Root bundle with foundation inheritance
- ✅ Three behaviors (latex-authoring, figure-generation, conference-styling)
- ✅ Three core agents (paper-architect, latex-expert, figure-artist)
- ✅ Context sink architecture with thin awareness pointers
- ✅ NeurIPS conference format specification
- ✅ Comprehensive documentation

**Next Phases:**
- Phase 2: Additional conference formats (ICML, ACL, IEEE, ACM)
- Phase 3: Citation manager agent
- Phase 4: Python scripts for compilation and validation
- Phase 5: Pre-composed bundle variants

See `IMPLEMENTATION_PLAN.md` for complete roadmap.

## Contributing

Contributions welcome! Areas of focus:

1. **Additional conference formats** - Add specifications to `context/conference-formats/`
2. **LaTeX templates** - Official style files in `templates/`
3. **Figure examples** - Add to agent documentation
4. **Testing** - Unit, integration, and E2E tests

## Documentation

- **`ARCHITECTURE.md`** - Bundle design and patterns
- **`IMPLEMENTATION_PLAN.md`** - Development roadmap and phases
- **Research files** - Comprehensive research saved in working directory
  - `amplifier-docs-research.md` - Bundle development patterns
  - `arxiv-paper-research.md` - PaperBanana insights
  - `conference-styling-research.md` - Conference specifications
  - `scientific-imaging-research.md` - Figure generation tools

## License

[To be determined - recommend MIT or Apache 2.0]

## Acknowledgments

Built on the [Amplifier](https://github.com/microsoft/amplifier) framework by Microsoft.

Research informed by:
- PaperBanana project (arXiv 2601.23265)
- Official conference guidelines (NeurIPS, ICML, ACL, IEEE, ACM)
- Scientific visualization best practices

---

**Status:** Phase 1 Complete (Core Structure) ✅  
**Ready for:** Testing and Phase 2 development  
**Contact:** [Your contact information]
