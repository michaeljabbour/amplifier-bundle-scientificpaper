# Scientific Paper Bundle - Implementation Plan

**Status:** Ready to build  
**Date:** 2026-02-04  
**Based on:** Expert consultation + comprehensive research

---

## Research Summary

### Key Insights from Research

1. **PaperBanana Research (arXiv 2601.23265)**
   - Multi-agent architecture for academic illustration automation
   - Quality veto rules for publication figures
   - Reference-driven approach using NeurIPS 2025 examples
   - 5 specialized agents: Retriever, Planner, Stylist, Visualizer, Critic
   - **Critical takeaway:** Gemini-3-Pro works for figure *generation*, not data plotting

2. **Scientific Imaging Strategy**
   - ❌ **Gemini/Imagen NOT suitable** for data-driven plots or mathematical diagrams
   - ✅ **Gold standard:** Matplotlib/Seaborn → tikzplotlib → LaTeX
   - ✅ **For diagrams:** TikZ (mathematical), PlotNeuralNet (NN architecture), Mermaid (flowcharts)
   - MCP servers good for exploration, not final publication figures

3. **Conference Format Requirements**
   - **Critical differences:** ACL requires A4 paper (others US Letter), font sizes vary 9-11pt
   - **Citation styles:** ACL uses author-year; most others numeric
   - **Column layouts:** NeurIPS single-column; most others two-column
   - All conferences provide official LaTeX style files

4. **Amplifier Bundle Best Practices**
   - Thin bundle pattern: inherit foundation, add only domain-specific
   - Context sink architecture: heavy docs in agents, thin pointers in behaviors
   - Behaviors (~50 lines) vs Agents (unlimited with @mentions) vs Context (on-demand)
   - Templates and scripts accessible via @bundle:path syntax

---

## Architecture Validation ✅

**Current ARCHITECTURE.md is sound.** Foundation-expert confirms:
- ✅ Thin bundle pattern correctly planned
- ✅ Context sink architecture appropriate
- ✅ Agent specialization well-designed
- ✅ Template/script organization correct

**Key refinements needed:**
1. Behavior files should use `.yaml` extension (not `.md`)
2. Update figure generation strategy based on imaging research
3. Add PaperBanana-inspired quality veto system
4. Clarify Gemini API role (conceptual figures only, not plots)

---

## Implementation Phases

### Phase 1: Core Bundle Structure (Week 1)

**Goal:** Minimal viable bundle that inherits foundation and provides LaTeX authoring

#### 1.1 Root Bundle
```bash
# Create bundle.md
✓ Inherits foundation (no tool duplication)
✓ Includes 3 behaviors: latex-authoring, figure-generation, conference-styling
✓ Thin (~50 lines markdown + YAML frontmatter)
```

**Files to create:**
- `bundle.md` - Root bundle definition

#### 1.2 LaTeX Authoring Behavior
```bash
# Create behaviors/latex-authoring.yaml
✓ Composes latex-expert agent
✓ Includes thin awareness context (~40 lines)
✓ No heavy conference format docs (those go in agent)
```

**Files to create:**
- `behaviors/latex-authoring.yaml`
- `context/latex-awareness.md` (thin pointer)
- `agents/latex-expert.md` (heavy context sink)

#### 1.3 First Conference Template
```bash
# Create templates/neurips/
✓ Copy official NeurIPS 2024 style files
✓ Include example.tex and example.bib
✓ Document usage in latex-expert agent
```

**Files to create:**
- `templates/neurips/neurips_2024.sty`
- `templates/neurips/template.tex`
- `templates/neurips/example.bib`
- `context/conference-formats/neurips.md` (format specification)

#### 1.4 Paper Architect Agent
```bash
# Create agents/paper-architect.md
✓ Structure and outline specialist
✓ IMRaD methodology (Intro, Methods, Results, Discussion)
✓ Abstract composition guidance
✓ No heavy docs (references thin context only)
```

**Files to create:**
- `agents/paper-architect.md`
- `context/paper-structure-awareness.md` (thin pointer)

**Phase 1 Deliverable:** User can create a NeurIPS-formatted paper with structure guidance

---

### Phase 2: Figure Generation (Week 2)

**Goal:** AI-assisted figure generation with quality veto rules

#### 2.1 Figure Generation Behavior
```bash
# Create behaviors/figure-generation.yaml
✓ Composes figure-artist agent
✓ Thin awareness pointer
✓ Explains when to delegate
```

**Files to create:**
- `behaviors/figure-generation.yaml`
- `context/figure-generation-awareness.md` (thin pointer)

#### 2.2 Figure Artist Agent (Context Sink)
```bash
# Create agents/figure-artist.md
✓ Heavy @mentions to imaging context
✓ PaperBanana-inspired quality veto rules
✓ Multi-tool approach: matplotlib, TikZ, Mermaid
✓ Clear trigger examples in meta.description
```

**Files to create:**
- `agents/figure-artist.md`
- `context/imaging/matplotlib-scientific.md` (matplotlib best practices)
- `context/imaging/tikz-patterns.md` (TikZ examples)
- `context/imaging/quality-veto-rules.md` (PaperBanana-inspired rules)

#### 2.3 Figure Generation Scripts
```bash
# Create scripts/generate_figure.py
✓ Matplotlib → tikzplotlib pipeline
✓ Bundle-aware (uses AMPLIFIER_BUNDLE_ROOT)
✓ Quality checks (resolution, format, fonts)
```

**Files to create:**
- `scripts/generate_figure.py`
- `scripts/validate_figure.py`

**Phase 2 Deliverable:** User can generate publication-ready plots and diagrams

---

### Phase 3: Multi-Conference Support (Week 3)

**Goal:** Support all major conference formats with conversion capabilities

#### 3.1 Conference Styling Behavior
```bash
# Create behaviors/conference-styling.yaml
✓ Composes latex-expert agent (already exists)
✓ Thin awareness of supported conferences
✓ Points to conference format context
```

**Files to create:**
- `behaviors/conference-styling.yaml`
- `context/conference-styling-awareness.md`

#### 3.2 Conference Format Context Files
```bash
# Create context/conference-formats/*.md
✓ Detailed specifications for each conference
✓ Loaded on-demand by latex-expert agent
✓ Include margin specs, fonts, citation styles
```

**Files to create:**
- `context/conference-formats/icml.md`
- `context/conference-formats/acl.md`
- `context/conference-formats/ieee.md`
- `context/conference-formats/acm.md`
- `context/conference-formats/arxiv.md`
- `context/conference-formats/stanford-cs.md`

#### 3.3 Conference Templates
```bash
# Create templates/*/
✓ Official style files for each conference
✓ Example templates
✓ Bibliography examples
```

**Directories to create:**
- `templates/icml/`
- `templates/ieee/`
- `templates/acm/`
- `templates/generic/`

#### 3.4 Compilation Scripts
```bash
# Create scripts/compile_latex.py
✓ Multi-conference aware
✓ Automatic style file copying
✓ Error diagnosis and helpful messages
```

**Files to create:**
- `scripts/compile_latex.py`
- `scripts/validate_format.py`

**Phase 3 Deliverable:** User can convert papers between conference formats

---

### Phase 4: Citation Management (Week 4)

**Goal:** BibTeX management and citation style conversion

#### 4.1 Citation Manager Agent
```bash
# Create agents/citation-manager.md
✓ BibTeX entry creation from DOIs/URLs
✓ Citation style conversion
✓ Reference validation
```

**Files to create:**
- `agents/citation-manager.md`
- `context/citation-awareness.md`
- `context/citation-formats/bibtex-guide.md`

#### 4.2 Citation Scripts
```bash
# Create scripts/manage_citations.py
✓ DOI → BibTeX conversion
✓ Citation style detection and conversion
✓ Duplicate detection
```

**Files to create:**
- `scripts/manage_citations.py`

**Phase 4 Deliverable:** Automated bibliography management

---

### Phase 5: Bundle Variants and Advanced Features (Week 5)

**Goal:** Pre-composed variants and advanced capabilities

#### 5.1 Pre-Composed Variants
```bash
# Create bundles/with-gemini.md
✓ Includes base + Gemini MCP
✓ Enhanced for conceptual figure generation
✓ Documents setup requirements (API keys)
```

**Files to create:**
- `bundles/with-gemini.md`
- `bundles/latex-only.md`
- `bundles/neurips-focused.md`

#### 5.2 Skills for Cowork Integration
```bash
# Create skills/amplifier-expert/
✓ Amplifier philosophy and patterns skill
✓ Enables non-technical users to leverage bundle
```

**Files to create:**
- `skills/amplifier-expert/skill.md`

#### 5.3 Quality Veto System
```bash
# Enhance figure-artist with automated checks
✓ Resolution verification (300 DPI min)
✓ Color scheme validation
✓ Text readability checks
✓ Format verification (vector preferred)
```

**Updates to:**
- `agents/figure-artist.md`
- `context/imaging/quality-veto-rules.md`

**Phase 5 Deliverable:** Production-ready bundle with variants

---

## Updated Figure Generation Strategy

Based on imaging research, the strategy is now:

| Figure Type | Approach | Rationale |
|-------------|----------|-----------|
| **Data plots** | Matplotlib → tikzplotlib | Gold standard for publication |
| **Statistical graphics** | Seaborn | Built on matplotlib, publication-ready |
| **Mathematical diagrams** | TikZ/PGFPlots | LaTeX-native, perfect integration |
| **NN architectures** | PlotNeuralNet (TikZ) | Specialized tool, excellent results |
| **Flowcharts** | Mermaid → SVG or TikZ | Fast prototyping, embeddable |
| **Conceptual illustrations** | Gemini Imagen (optional) | Only for non-technical imagery |

**Key decision:** Gemini API is **optional enhancement** for conceptual figures only, not core capability.

---

## File Structure (Complete)

```
amplifier-bundle-scientificpaper/
├── bundle.md                           # Root bundle (thin)
├── ARCHITECTURE.md                     # Architecture documentation
├── IMPLEMENTATION_PLAN.md              # This file
├── README.md                           # User-facing documentation
│
├── behaviors/                          # Thin capability modules
│   ├── latex-authoring.yaml
│   ├── figure-generation.yaml
│   └── conference-styling.yaml
│
├── agents/                             # Context sink specialists
│   ├── paper-architect.md
│   ├── figure-artist.md
│   ├── latex-expert.md
│   └── citation-manager.md
│
├── context/                            # Heavy documentation (on-demand)
│   ├── latex-awareness.md
│   ├── figure-generation-awareness.md
│   ├── paper-structure-awareness.md
│   ├── citation-awareness.md
│   ├── conference-styling-awareness.md
│   ├── conference-formats/
│   │   ├── neurips.md
│   │   ├── icml.md
│   │   ├── acl.md
│   │   ├── ieee.md
│   │   ├── acm.md
│   │   ├── arxiv.md
│   │   └── stanford-cs.md
│   ├── imaging/
│   │   ├── matplotlib-scientific.md
│   │   ├── tikz-patterns.md
│   │   ├── quality-veto-rules.md
│   │   └── plotneuralnet-guide.md
│   └── citation-formats/
│       └── bibtex-guide.md
│
├── templates/                          # LaTeX templates
│   ├── neurips/
│   │   ├── neurips_2024.sty
│   │   ├── template.tex
│   │   └── example.bib
│   ├── icml/
│   ├── ieee/
│   ├── acm/
│   └── generic/
│
├── scripts/                            # Executable utilities
│   ├── compile_latex.py
│   ├── validate_format.py
│   ├── generate_figure.py
│   ├── validate_figure.py
│   └── manage_citations.py
│
├── bundles/                            # Pre-composed variants
│   ├── with-gemini.md
│   ├── latex-only.md
│   └── neurips-focused.md
│
├── skills/                             # Cowork integration
│   └── amplifier-expert/
│       └── skill.md
│
├── tests/                              # Testing
│   ├── test_bundle_structure.py
│   ├── test_latex_compilation.py
│   └── test_figure_generation.py
│
└── examples/                           # Usage examples
    ├── neurips-paper/
    └── icml-paper/
```

---

## Dependencies

### Python Packages (requirements.txt)
```
matplotlib>=3.8.0
seaborn>=0.13.0
tikzplotlib>=0.10.1
pypdf>=4.0.0
requests>=2.31.0
bibtexparser>=1.4.0
```

### System Requirements
- LaTeX distribution (TeX Live 2023+ recommended)
- pdflatex, bibtex, latexmk
- Optional: Inkscape for SVG conversion

### Optional API Keys
- `GOOGLE_API_KEY` - Gemini/Imagen (for with-gemini variant only)

---

## Testing Strategy

### Unit Tests (60%)
- Template parsing and validation
- Conference format detection
- Figure code generation
- BibTeX entry creation

### Integration Tests (30%)
- LaTeX compilation pipeline
- Agent spawning and context loading
- Script execution via bash tool

### E2E Tests (10%)
- Full paper creation (NeurIPS format)
- Conference format conversion (NeurIPS → ICML)
- Figure generation quality checks

---

## Anti-Patterns to Avoid ❌

From foundation-expert consultation:

1. **Fat bundle with all contexts loaded** → Use context sink pattern
2. **Hardcoded conference formats in bundle.md** → Externalize to context/
3. **Single monolithic agent** → Split by concern
4. **Duplicating foundation tools** → Inherit, don't redeclare
5. **Inline figure generation code** → Use scripts/ for deterministic operations
6. **Heavy docs in behaviors** → Keep behaviors thin, docs in context/
7. **Gemini for data plots** → Use matplotlib/tikz (research finding)
8. **Missing agent examples** → Always include trigger examples in meta.description

---

## Next Steps

### Immediate Actions (Today)

1. **Create root bundle.md** - Establish foundation inheritance
2. **Create first behavior + agent pair** - Prove context sink pattern
3. **Add NeurIPS template** - Test template + context flow

### This Week

1. Complete Phase 1 (Core Structure)
2. Test with real paper creation workflow
3. Validate bundle.md with foundation-expert if needed

### Validation Checkpoints

Before each phase completion:
- [ ] All files follow thin bundle pattern
- [ ] Agents have complete meta.description with examples
- [ ] Heavy docs in context/, not behaviors
- [ ] Templates accessible via @scientificpaper:templates/
- [ ] Scripts executable and bundle-aware
- [ ] No duplicate tool declarations from foundation

---

## Success Criteria

**Phase 1 Success:**
```bash
amplify --bundle @scientificpaper "Create a NeurIPS paper on transformer efficiency"
# → Generates structured paper with correct formatting
```

**Phase 2 Success:**
```bash
amplify --bundle @scientificpaper "Create a plot showing training loss curves"
# → Generates matplotlib plot, converts to TikZ, embeds in LaTeX
```

**Full Bundle Success:**
```bash
amplify --bundle @scientificpaper "Convert my NeurIPS paper to ICML format"
# → Successful format conversion with validation
```

---

## Research Files Generated

All research saved to working directory:
- `amplifier-docs-research.md` (28.9 KB) - Amplifier bundle development patterns
- `arxiv-paper-research.md` - PaperBanana architecture insights
- `conference-styling-research.md` - All conference format specifications
- `scientific-imaging-research.md` - Figure generation tool evaluation

These files serve as authoritative references during implementation.
