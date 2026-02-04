# Scientific Paper Bundle Architecture

## Overview

A thin, composable Amplifier bundle for creating publication-ready scientific papers with sophisticated styling and AI-assisted figure generation.

**Philosophy:** Following Amplifier's "mechanism, not policy" approach—provide composable tools without dictating specific workflows.

## Bundle Structure

```
amplifier-bundle-scientificpaper/
├── bundle.md                    # Root bundle (thin inheritance from foundation)
├── ARCHITECTURE.md              # This document
│
├── behaviors/                   # Reusable capability modules
│   ├── latex-authoring.md       # LaTeX document creation
│   ├── figure-generation.md     # Scientific imaging capabilities
│   └── conference-styling.md    # Multi-conference format support
│
├── agents/                      # Specialized context-sink agents
│   ├── paper-architect.md       # Structure and outline planning
│   ├── figure-artist.md         # AI-assisted scientific figures
│   ├── latex-expert.md          # LaTeX compilation and debugging
│   └── citation-manager.md      # Reference and bibliography handling
│
├── context/                     # Shared knowledge base
│   ├── instructions.md          # Core operating instructions
│   ├── conference-formats/      # Conference-specific guidelines
│   │   ├── neurips.md
│   │   ├── icml.md
│   │   ├── acl.md
│   │   ├── ieee.md
│   │   ├── acm.md
│   │   └── arxiv.md
│   └── imaging/                 # Figure generation guidance
│       ├── gemini-api.md
│       ├── tikz-patterns.md
│       └── matplotlib-scientific.md
│
├── templates/                   # LaTeX templates (assets)
│   ├── neurips/
│   ├── icml/
│   ├── ieee/
│   └── generic/
│
├── scripts/                     # Utility scripts
│   ├── compile_latex.py
│   ├── validate_format.py
│   └── generate_figure.py
│
├── skills/                      # Claude skills for Cowork integration
│   └── amplifier-expert/        # Amplifier philosophy/patterns skill
│
└── bundles/                     # Pre-composed variants
    ├── with-gemini.md           # Includes Gemini API for figures
    └── latex-only.md            # Pure LaTeX without AI imaging
```

## Core Design Decisions

### 1. Thin Bundle Pattern

The root `bundle.md` inherits from foundation and adds only scientific paper capabilities:

```yaml
---
bundle:
  name: scientificpaper
  version: 1.0.0
includes:
  - github:microsoft/amplifier-foundation/bundle.md
behaviors:
  - behaviors/latex-authoring.md
  - behaviors/figure-generation.md
  - behaviors/conference-styling.md
---
```

**Rationale:** Avoids duplicating foundation tools (bash, filesystem) while adding domain-specific agents.

### 2. Context Sink Architecture

Heavy documentation lives in agents, not behaviors:

| Component | Token Budget | Content |
|-----------|--------------|---------|
| Behavior files | ~50 lines | Awareness pointers only |
| Agent files | Unlimited | Full @mention references to context/ |
| Context files | Loaded on demand | Conference guides, API docs |

**Example:** The `figure-artist` agent loads imaging context only when spawned for figure generation tasks.

### 3. Conference Format Abstraction

Conference-specific formatting is externalized to `context/conference-formats/`:

```
User: "Format this paper for NeurIPS"
→ latex-expert agent loads context/conference-formats/neurips.md
→ Applies correct margins, fonts, citation style
```

**Supported Conferences:**
- NeurIPS (8 pages, Times 10pt, 5.5"×9" text area)
- ICML (8 pages, two-column, Type-1 fonts)
- ACL (A4 only, natbib citations)
- IEEE (letter/A4, numbered citations)
- ACM/SIGCHI (single-column review, accessibility)
- arXiv (TeX recommended, .bbl pre-compiled)
- Stanford CS (1.5" binding edge, 10-12pt)

### 4. Figure Generation Strategy

Multiple approaches based on figure type:

| Figure Type | Primary Tool | Fallback |
|-------------|--------------|----------|
| Mathematical plots | Matplotlib → tikzplotlib | TikZ direct |
| Architecture diagrams | Mermaid/Graphviz | Gemini API |
| Neural network diagrams | Custom SVG | Gemini 3 Pro |
| Flowcharts | Mermaid | Claude SVG |
| Statistical graphics | Matplotlib | PGFPlots |
| Photorealistic scientific | Gemini API | N/A |

**MCP Integration:** Optional MCP servers for Gemini API and chart generation can be composed in.

## Agent Specifications

### paper-architect

**Purpose:** Structure and outline scientific papers

**Triggers:** "outline paper", "structure abstract", "plan sections", "methodology organization"

**Capabilities:**
- IMRaD structure guidance (Introduction, Methods, Results, Discussion)
- Abstract composition (background, gap, approach, results, implications)
- Section flow optimization
- Contribution statement crafting

### figure-artist

**Purpose:** Generate publication-ready scientific figures

**Triggers:** "create figure", "generate diagram", "plot results", "visualize architecture"

**Capabilities:**
- Matplotlib/TikZ code generation
- Gemini API orchestration for complex figures
- SVG creation for vector diagrams
- PaperBanana-inspired quality control (veto rules for artifacts, colors, backgrounds)

**Quality Veto Rules:**
- No low-quality artifacts (blurry, distorted)
- Professional color schemes (no neon/jarring)
- No black backgrounds
- Legible text at publication scale

### latex-expert

**Purpose:** LaTeX compilation, debugging, and formatting

**Triggers:** "compile latex", "fix latex error", "format for conference", "add bibliography"

**Capabilities:**
- Multi-conference template application
- Compilation error diagnosis
- BibTeX/natbib management
- Page limit optimization
- Font embedding verification

### citation-manager

**Purpose:** Reference and bibliography handling

**Triggers:** "add citation", "format references", "check bibliography", "citation style"

**Capabilities:**
- BibTeX entry creation from DOIs/URLs
- Citation style conversion (author-year ↔ numeric)
- Reference list formatting
- Cross-reference validation

## Tool Integrations

### Required Tools (from foundation)
- `tool-bash` - LaTeX compilation, git operations
- `tool-filesystem` - File read/write operations

### Optional Tools (composed in bundles/)
- `tool-web-search` - Reference lookup
- `tool-mcp-gemini` - Gemini API for figure generation
- `tool-mcp-charts` - AntV chart generation

## Workflow Examples

### Example 1: Create NeurIPS Paper

```
User: "Create a new NeurIPS paper on transformer efficiency"

1. paper-architect spawns → outlines structure
2. Creates LaTeX project from templates/neurips/
3. Generates abstract and section skeletons
4. User iterates on content
```

### Example 2: Generate Figure

```
User: "Create an architecture diagram for my attention mechanism"

1. figure-artist spawns → analyzes requirements
2. Determines best approach (Mermaid for flowchart aspect)
3. Generates code or calls Gemini API
4. Applies veto rules for quality
5. Exports publication-ready PNG/PDF
```

### Example 3: Conference Conversion

```
User: "Convert my paper from NeurIPS to ICML format"

1. latex-expert spawns
2. Loads both conference format contexts
3. Adjusts margins, fonts, style file
4. Validates page count and formatting
5. Verifies font embedding
```

## Configuration Dimensions

Following Amplifier's four configurable layers:

| Dimension | Options |
|-----------|---------|
| Provider | anthropic (default), openai, azure, gemini |
| Bundle | scientificpaper (base), with-gemini, latex-only |
| Modules | Core + optional MCP tools |
| Source | github (default), local file:// |

## Testing Strategy

### Unit Tests (60%)
- Template parsing and validation
- Conference format detection
- Figure code generation

### Integration Tests (30%)
- LaTeX compilation pipeline
- Agent spawning and context loading
- MCP tool integration

### E2E Tests (10%)
- Full paper creation workflow
- Conference format conversion
- Figure generation quality

## Development Roadmap

### Phase 1: Core (MVP)
- [ ] Root bundle.md with foundation inheritance
- [ ] latex-expert agent with conference formats
- [ ] paper-architect agent for structure
- [ ] NeurIPS, ICML, IEEE templates

### Phase 2: Figure Generation
- [ ] figure-artist agent
- [ ] Matplotlib/TikZ code generation
- [ ] Mermaid/Graphviz integration
- [ ] Optional Gemini MCP

### Phase 3: Advanced
- [ ] citation-manager agent
- [ ] All conference formats
- [ ] Quality veto system (PaperBanana-inspired)
- [ ] Automated format validation

## Dependencies

### Python Packages
- `pypdf` - PDF manipulation
- `matplotlib` - Plotting
- `tikzplotlib` - Matplotlib → TikZ conversion

### System Requirements
- LaTeX distribution (TeX Live recommended)
- pdflatex, bibtex, latexmk
- Optional: Inkscape (SVG conversion)

### API Keys (Optional)
- `GOOGLE_API_KEY` - Gemini image generation
- Configured via provider settings

## Anti-Patterns to Avoid

1. **Fat bundle with all contexts loaded** - Use context sink pattern
2. **Hardcoded conference formats in bundle.md** - Externalize to context/
3. **Single monolithic agent** - Split by concern (structure, figures, latex, citations)
4. **Duplicating foundation tools** - Inherit, don't redeclare
5. **Inline figure generation code** - Use scripts/ for deterministic operations
