# PaperBanana Integration - Complete Implementation Plan

**Date:** 2026-02-04  
**Bundle:** amplifier-bundle-scientificpaper  
**Architecture:** 3-layer integration (Tool → Agent → Recipe)  

---

## Executive Summary

This plan implements PaperBanana's multi-agent academic illustration system (arXiv 2601.23265) into the scientific paper bundle using a **3-layer composable architecture**:

1. **Layer 1: Tool Module** - `tool-paperbanana` (mechanism)
2. **Layer 2: Enhanced Agent** - `figure-artist` with PaperBanana knowledge (intelligence)
3. **Layer 3: Recipe Workflow** - Multi-stage orchestration with approval gates (orchestration)

**Recommendation:** Start with **Phase 1** (minimal viable integration) for quick value delivery, then enhance with **Phase 2** (specialized agents) based on usage patterns.

---

## Architecture Overview

```
┌──────────────────────────────────────────────────────────┐
│ USER INTERACTION                                         │
├──────────────────────────────────────────────────────────┤
│ Layer 3: RECIPE WORKFLOW (Orchestration)                │
│ • recipes/paperbanana-figure.yaml                        │
│ • Explicit multi-step process with approval gates       │
│ • Uses figure-artist + tool-paperbanana                  │
├──────────────────────────────────────────────────────────┤
│ Layer 2: ENHANCED AGENT (Intelligence)                  │
│ • agents/figure-artist.md (enhanced)                     │
│ • Decides when to use tool-paperbanana                   │
│ • Context sink for PaperBanana documentation             │
│ • Quality veto rules expertise                           │
├──────────────────────────────────────────────────────────┤
│ Layer 1: TOOL MODULE (Mechanism)                        │
│ • modules/tool-paperbanana/                              │
│ • Core PaperBanana implementation                        │
│ • 5 sub-components: Retriever → Planner → Stylist →     │
│                     Visualizer → Critic                  │
│ • Protocol-compliant Python tool                         │
└──────────────────────────────────────────────────────────┘
```

**User Journeys:**
- **Simple:** "Create a figure" → figure-artist uses tool-paperbanana intelligently
- **Direct:** Explicitly call tool-paperbanana for fine control
- **Complex:** Run recipe for multi-stage workflow with approval gates

---

## Phase 1: Minimal Viable Integration ⭐ **Start Here**

### Objective
Get PaperBanana functionality working quickly with minimal complexity. All 3 layers functional, reusing existing figure-artist agent.

### Deliverables

#### 1. Tool Module: `modules/tool-paperbanana/`

**Purpose:** Core PaperBanana mechanism (5-agent orchestration)

**Structure:**
```
modules/tool-paperbanana/
├── pyproject.toml                  # Module package config
├── README.md                       # Documentation
└── tool_paperbanana/
    ├── __init__.py
    ├── mount.py                    # Tool protocol implementation
    ├── retriever.py                # Context extraction from paper
    ├── planner.py                  # Content & style planning
    ├── visualizer.py               # Figure generation (matplotlib/tikz)
    ├── critic.py                   # Quality validation (8 veto rules)
    └── utils.py                    # Shared utilities
```

**Protocol Interface:**

```python
# Input (from agent or recipe)
{
    "paper_content": str,           # Paper text (abstract + methods)
    "figure_type": str,             # "methodology" | "plot" | "architecture"
    "style_requirements": {
        "conference": str,          # "neurips" | "icml" | "ieee"
        "colorblind_safe": bool,
        "width": str                # "column" | "page"
    },
    "quality_rules": list[str],     # Veto rules to enforce
    "max_iterations": int           # Refinement attempts (default: 3)
}

# Output (ToolResult)
{
    "success": bool,
    "figure_path": str,             # Path to generated figure
    "format": str,                  # "pdf" | "tikz" | "png"
    "metadata": {
        "iterations": int,
        "rules_passed": list[str],
        "rules_failed": list[str],
        "critique": str
    },
    "error": str | None
}
```

**Implementation Approach:**

```python
# tool_paperbanana/mount.py
class PaperBananaToolMount(ToolMount):
    async def execute(self, input: dict) -> ToolResult:
        # 1. Retrieve context
        context = await self.retriever.extract(input["paper_content"])
        
        # 2. Plan content & style
        content_plan = await self.planner.plan_content(context)
        style_plan = await self.planner.plan_style(
            context, 
            input["style_requirements"]
        )
        
        # 3. Generate figure
        figure = await self.visualizer.generate(content_plan, style_plan)
        
        # 4. Iterative refinement with critic
        for i in range(input.get("max_iterations", 3)):
            critique = await self.critic.evaluate(
                figure, 
                input["quality_rules"]
            )
            if critique.passed:
                break
            figure = await self.visualizer.refine(figure, critique)
        
        return ToolResult(
            success=critique.passed,
            figure_path=figure.path,
            format=figure.format,
            metadata={
                "iterations": i + 1,
                "rules_passed": critique.passed_rules,
                "rules_failed": critique.failed_rules,
                "critique": critique.summary
            }
        )
```

**Quality Veto Rules (from PaperBanana research):**

1. `no_low_quality_artifacts` - No visible grid artifacts, blur, distortion
2. `professional_colors` - No neon colors, proper color balance
3. `no_black_backgrounds` - Avoid unprofessional black backgrounds
4. `modern_style` - Appropriate fonts, no Comic Sans or excessive clip-art
5. `vector_preferred` - PDF/SVG over raster when possible
6. `appropriate_aspect_ratio` - Match conference requirements
7. `clear_labels` - All axes, legends, captions legible
8. `data_integrity` - Accurate representation of data

#### 2. Behavior Bundle: `behaviors/paperbanana.yaml`

**Purpose:** Package the tool for bundle composition

```yaml
---
bundle:
  name: paperbanana
  version: 1.0.0
  description: "PaperBanana multi-agent figure generation with quality veto rules"

tools:
  - module: tool-paperbanana
    source: scientificpaper:modules/tool-paperbanana
    config:
      default_max_iterations: 3
      default_quality_rules:
        - "no_low_quality_artifacts"
        - "professional_colors"
        - "no_black_backgrounds"
        - "modern_style"
        - "vector_preferred"
        - "appropriate_aspect_ratio"
        - "clear_labels"
        - "data_integrity"

agents:
  include:
    - scientificpaper:figure-artist  # Enhanced with PaperBanana

context:
  include:
    - scientificpaper:context/paperbanana-methodology.md
---

# PaperBanana Behavior

Adds PaperBanana multi-agent figure generation capabilities to the scientific paper bundle.

**Key Features:**
- Automated iterative refinement
- Quality veto rules enforcement
- Publication-ready output (PDF, TikZ, SVG)
- Conference-specific styling

**Usage:**
The figure-artist agent automatically uses tool-paperbanana when appropriate for complex figures requiring quality validation.
```

#### 3. Enhanced Agent: `agents/figure-artist.md`

**Enhancement:** Add PaperBanana section to existing agent

```markdown
---
meta:
  name: figure-artist
  description: |
    **MUST be used for creating publication-ready scientific figures.**
    
    [... existing description ...]
    
    Enhanced with PaperBanana multi-agent approach for:
    - Methodology diagrams with iterative refinement
    - Statistical plots with quality veto rules
    - Architecture diagrams with professional styling
    
    [... existing examples ...]
---

# Figure Artist Agent

[... existing content ...]

---

## PaperBanana Integration

### When to Use tool-paperbanana

**Use PaperBanana approach for:**
- Complex methodology diagrams requiring multiple refinement iterations
- User explicitly requests "PaperBanana-style" or "automated refinement"
- Figures that must meet strict publication quality standards
- Architecture diagrams for academic papers
- When you need automatic quality validation

**Use matplotlib/tikz directly for:**
- Simple training curves, bar charts, scatter plots
- User has specific matplotlib/seaborn requirements
- Need fine-grained control over every plot element
- Quick prototyping or draft figures

### PaperBanana Workflow

1. **Retrieve Context:** Extract relevant information from paper
2. **Plan Content:** Determine what elements to include
3. **Plan Style:** Select colors, fonts, layout per conference
4. **Generate:** Create initial figure
5. **Critique:** Apply 8 quality veto rules
6. **Refine:** Iterate based on critique (up to 3 times)

### Quality Veto Rules (Red Lines)

Always enforce these 8 rules from PaperBanana research:

1. **No Low-Quality Artifacts:** Avoid grid artifacts, blur, distorted shapes
2. **Professional Colors:** No jarring neon colors, use ColorBrewer palettes
3. **No Black Backgrounds:** Considered unprofessional in academic papers
4. **Modern Style:** Appropriate fonts (no Comic Sans), minimal clip-art
5. **Vector Preferred:** Use PDF/SVG over PNG when possible
6. **Appropriate Aspect Ratio:** Match conference column/page width
7. **Clear Labels:** All text, axes, legends must be legible at print size
8. **Data Integrity:** Accurate representation, no misleading visualizations

### Using tool-paperbanana

```python
# Example tool invocation
paperbanana_result = await use_tool("paperbanana", {
    "paper_content": """
        Abstract: We propose a novel attention mechanism...
        Methods: Our approach consists of three stages...
    """,
    "figure_type": "methodology",
    "style_requirements": {
        "conference": "neurips",
        "colorblind_safe": True,
        "width": "page"
    },
    "quality_rules": [
        "no_low_quality_artifacts",
        "professional_colors",
        "no_black_backgrounds",
        "modern_style",
        "vector_preferred",
        "appropriate_aspect_ratio",
        "clear_labels",
        "data_integrity"
    ],
    "max_iterations": 3
})

# Result includes:
# - figure_path: Path to generated figure
# - format: "pdf" | "tikz" | "png"
# - metadata: iterations, rules_passed, rules_failed, critique
```

### Integration with Existing Workflow

Your complete figure generation workflow now includes:

1. **Assess Request:** Determine complexity and requirements
2. **Choose Approach:**
   - **tool-paperbanana:** Complex diagrams needing refinement
   - **matplotlib/seaborn:** Direct data visualization
   - **tikz:** Mathematical diagrams, custom graphics
   - **PlotNeuralNet:** Neural network architectures
3. **Generate Figure:** Use selected tool/library
4. **Validate Quality:** Check against veto rules (automatic with PaperBanana)
5. **Provide Integration:** LaTeX code to include figure

@scientificpaper:context/paperbanana-methodology.md

[... rest of existing agent content ...]
```

#### 4. Context Documentation: `context/paperbanana-methodology.md`

**Purpose:** Heavy documentation loaded only when figure-artist spawns

```markdown
# PaperBanana Methodology

**Source:** arXiv 2601.23265 - "PaperBanana: Automating Academic Illustration for AI Scientists"

## Overview

PaperBanana is a multi-agent framework for automating the generation of publication-ready academic illustrations. It addresses the final major bottleneck in AI-driven research workflows.

## Multi-Agent Architecture

### 1. Retriever Agent
**Purpose:** Extract relevant information from paper content

**Capabilities:**
- Semantic search through paper sections
- Identify key concepts, methods, results
- Extract data for visualization
- Reference similar figures from literature

### 2. Planner Agent (Content)
**Purpose:** Determine what elements should be included

**Capabilities:**
- Identify essential vs. extraneous information
- Maintain faithfulness to paper content
- Ensure conciseness
- Plan visual hierarchy

### 3. Stylist Agent
**Purpose:** Design visual aesthetics

**Capabilities:**
- Select color schemes (ColorBrewer, colorblind-safe)
- Choose fonts and typography
- Determine layout and composition
- Apply conference-specific styling

### 4. Visualizer Agent
**Purpose:** Generate the actual figure

**Capabilities:**
- Render methodology diagrams
- Create statistical plots
- Generate architecture diagrams
- Support multiple formats (PDF, TikZ, PNG, SVG)

### 5. Critic Agent
**Purpose:** Quality validation and refinement guidance

**Capabilities:**
- Apply 8 quality veto rules
- Generate structured critique
- Identify specific improvement areas
- Track refinement iterations

## Quality Evaluation Metrics

PaperBanana evaluates on 4 dimensions from PaperBananaBench:

1. **Faithfulness:** Accurate representation of paper content
2. **Conciseness:** Avoids unnecessary elements
3. **Readability:** Clear labels, appropriate visual hierarchy
4. **Aesthetics:** Professional appearance, publication standards

## Iterative Refinement Process

```
Generate Initial Figure
    ↓
Apply Critic (8 veto rules)
    ↓
Pass? → Done
    ↓ Fail
Refine Based on Critique
    ↓
(Repeat up to max_iterations)
```

## Implementation in tool-paperbanana

The tool module implements this architecture with:
- `retriever.py` - Context extraction
- `planner.py` - Content & style planning
- `visualizer.py` - Figure generation
- `critic.py` - Quality validation

All coordinated by `mount.py` which implements the Tool protocol.

## References

- Paper: https://arxiv.org/abs/2601.23265
- GitHub: https://dwzhu-pku.github.io/PaperBanana/
- Research notes: @scientificpaper:research/arxiv-paper-research.md
```

#### 5. Recipe: `recipes/paperbanana-figure.yaml`

**Purpose:** Explicit multi-stage workflow with approval gates

**Complete recipe provided by recipe-author:**

```yaml
---
name: "paperbanana-figure-generation"
version: "1.0.0"
description: "Multi-stage figure generation with PaperBanana approach, quality validation, and human-in-loop approval"

# Context variables - can be overridden when executing recipe
context:
  paper_content: ""                           # Required: Paper text (abstract + methods)
  figure_type: "methodology"                  # "methodology" | "plot" | "architecture"
  conference: "neurips"                       # Target conference for styling
  colorblind_safe: true                       # Use colorblind-friendly palettes
  width: "page"                               # "column" | "page"
  max_refinement_iterations: 3                # Max attempts to refine figure

# Stage 1: PLANNING (with approval gate)
stages:
  - name: "planning"
    description: "Extract context and plan figure before generation"
    approval_required: true
    approval_prompt: |
      📋 **Figure Plan Review**
      
      Please review the proposed figure plan before generation:
      
      {{figure_plan}}
      
      ✅ **Approve** to proceed with generation
      ❌ **Deny** to revise the plan
    
    steps:
      # Step 1.1: Extract context from paper
      - id: "extract-context"
        agent: "scientificpaper:figure-artist"
        prompt: |
          **MODE: Context Extraction**
          
          Extract key information from this paper for figure generation:
          
          ```
          {{paper_content}}
          ```
          
          **Figure Type:** {{figure_type}}
          **Conference:** {{conference}}
          
          Identify:
          - Key concepts and methodology details
          - Visual elements needed (boxes, arrows, data points)
          - Technical terminology to include
          - Relationships between components
          
          Provide structured extraction suitable for figure planning.
        output: "paper_context"
        timeout: 300
        on_error: "fail"  # Critical step - must succeed
      
      # Step 1.2: Plan the figure
      - id: "plan-figure"
        agent: "scientificpaper:figure-artist"
        depends_on: ["extract-context"]
        prompt: |
          **MODE: Figure Planning**
          
          Based on the extracted context, create a detailed figure plan:
          
          **Context:**
          {{paper_context}}
          
          **Requirements:**
          - Type: {{figure_type}}
          - Conference: {{conference}}
          - Width: {{width}}
          - Colorblind-safe: {{colorblind_safe}}
          
          Provide:
          1. **Content Plan:** What elements to include, visual hierarchy
          2. **Style Plan:** Colors, fonts, layout, aspect ratio
          3. **Quality Targets:** Which veto rules are most critical
          4. **LaTeX Integration:** How to include in paper
          
          Be specific and detailed - this plan will be reviewed before generation.
        output: "figure_plan"
        timeout: 300
        on_error: "fail"

  # Stage 2: GENERATION
  - name: "generation"
    description: "Generate figure with PaperBanana and validate quality"
    
    steps:
      # Step 2.1: Generate using tool-paperbanana
      - id: "generate-figure"
        agent: "scientificpaper:figure-artist"
        prompt: |
          **MODE: Figure Generation**
          
          Generate the figure using the PaperBanana approach (tool-paperbanana):
          
          **Approved Plan:**
          {{figure_plan}}
          
          **Context:**
          {{paper_context}}
          
          **Style Requirements:**
          - Conference: {{conference}}
          - Width: {{width}}
          - Colorblind-safe: {{colorblind_safe}}
          
          Use tool-paperbanana with:
          - paper_content: Full context above
          - figure_type: {{figure_type}}
          - style_requirements: As specified
          - quality_rules: All 8 veto rules
          - max_iterations: {{max_refinement_iterations}}
          
          Provide:
          - Figure file path
          - Generation metadata (iterations, rules passed/failed)
          - LaTeX integration code
        output: "generation_result"
        timeout: 900  # 15 minutes for generation + iterations
        on_error: "fail"  # Must succeed
      
      # Step 2.2: Validate quality
      - id: "validate-quality"
        agent: "scientificpaper:figure-artist"
        depends_on: ["generate-figure"]
        parse_json: true  # Extract structured validation results
        prompt: |
          **MODE: Quality Validation**
          
          Validate the generated figure against all quality criteria:
          
          **Generation Result:**
          {{generation_result}}
          
          **Validation Checklist (8 Veto Rules):**
          1. ❓ No low-quality artifacts (grid, blur, distortion)
          2. ❓ Professional colors (no neon, good contrast)
          3. ❓ No black backgrounds
          4. ❓ Modern style (appropriate fonts)
          5. ❓ Vector format preferred
          6. ❓ Appropriate aspect ratio
          7. ❓ Clear labels (legible at print size)
          8. ❓ Data integrity (accurate representation)
          
          **Return structured JSON:**
          ```json
          {
            "quality_passed": true/false,
            "severity": "pass|minor|major|critical",
            "issues": [
              {"rule": "rule_name", "severity": "minor|major|critical", "description": "..."}
            ],
            "compliant_checks": {
              "no_artifacts": true/false,
              "professional_colors": true/false,
              "no_black_bg": true/false,
              "modern_style": true/false,
              "vector_format": true/false,
              "aspect_ratio": true/false,
              "clear_labels": true/false,
              "data_integrity": true/false
            }
          }
          ```
        output: "quality_check"
        timeout: 300
        on_error: "fail"

  # Stage 3: REFINEMENT (conditional - only if quality fails)
  - name: "refinement"
    description: "Refine figure if quality validation identified issues"
    
    steps:
      # Step 3.1: Assess if refinement needed
      - id: "assess-refinement-need"
        agent: "scientificpaper:figure-artist"
        depends_on: ["validate-quality"]
        prompt: |
          **MODE: Refinement Assessment**
          
          Quality check results:
          {{quality_check}}
          
          Analyze the severity:
          - **pass:** No refinement needed ✅
          - **minor:** Optional refinement (cosmetic issues)
          - **major:** Refinement recommended (functionality issues)
          - **critical:** Refinement required (publication blockers)
          
          Provide recommendation: Should we refine the figure?
        output: "refinement_assessment"
        timeout: 120
        on_error: "continue"
      
      # Step 3.2: Refine figure (conditional)
      - id: "refine-figure"
        condition: "{{quality_check.severity}} == 'major' or {{quality_check.severity}} == 'critical'"
        depends_on: ["assess-refinement-need"]
        agent: "scientificpaper:figure-artist"
        prompt: |
          **MODE: Figure Refinement**
          
          Refine the figure to address quality issues:
          
          **Quality Issues:**
          {{quality_check.issues}}
          
          **Failed Checks:**
          {{quality_check.compliant_checks}}
          
          **Original Generation:**
          {{generation_result}}
          
          Use tool-paperbanana again with:
          - Focus on failed quality rules
          - Reduce max_iterations to 2 (we've already tried once)
          - Same style requirements
          
          Provide refined figure with improvements documented.
        output: "refined_result"
        timeout: 600  # 10 minutes for refinement
        on_error: "continue"  # If refinement fails, user can review original
      
      # Step 3.3: Validate refinement (if refinement ran)
      - id: "validate-refinement"
        condition: "{{quality_check.severity}} == 'major' or {{quality_check.severity}} == 'critical'"
        depends_on: ["refine-figure"]
        parse_json: true
        agent: "scientificpaper:figure-artist"
        prompt: |
          **MODE: Refinement Validation**
          
          Re-validate the refined figure:
          
          **Refined Result:**
          {{refined_result}}
          
          **Previous Issues:**
          {{quality_check.issues}}
          
          Check if issues were resolved. Use same JSON format as initial validation.
        output: "final_quality_check"
        timeout: 300
        on_error: "continue"

# Recipe-level configuration
recursion:
  max_depth: 2
  max_total_steps: 25

metadata:
  author: "scientificpaper"
  tags: ["paperbanana", "figures", "quality-validation"]
  usage: |
    Execute with:
    
    amplifier run "execute recipes/paperbanana-figure.yaml with \
      paper_content='Your paper abstract and methods...' \
      figure_type='methodology' \
      conference='neurips'"
---

# PaperBanana Figure Generation Recipe

Multi-stage workflow for generating publication-ready figures using the PaperBanana approach.

## Features

- ✅ Context extraction and figure planning
- ✅ Human approval gate before expensive generation
- ✅ Automated quality validation (8 veto rules)
- ✅ Conditional refinement based on quality severity
- ✅ JSON-structured validation results
- ✅ Conference-specific styling

## Workflow

1. **Planning Stage:** Extract context → Plan figure → **[Approval Required]**
2. **Generation Stage:** Generate with tool-paperbanana → Validate quality
3. **Refinement Stage:** Assess need → Refine if needed → Re-validate

## Usage Example

```bash
amplifier run "execute recipes/paperbanana-figure.yaml with \
  paper_content='We propose a novel transformer architecture...' \
  figure_type='methodology' \
  conference='neurips' \
  colorblind_safe=true"
```

## Error Handling

- **Planning failures:** Recipe stops (review paper_content)
- **Generation failures:** Recipe stops (check tool-paperbanana config)
- **Refinement failures:** Recipe continues (original figure available)
```

#### 6. Update Root Bundle: `bundle.md`

Add PaperBanana behavior to includes:

```yaml
behaviors:
  include:
    - scientificpaper:behaviors/latex-authoring
    - scientificpaper:behaviors/figure-generation
    - scientificpaper:behaviors/conference-styling
    - scientificpaper:behaviors/paperbanana  # NEW
```

### Phase 1 File Structure

```
scientificpaper/
├── bundle.md                                    # MODIFIED - add paperbanana behavior
├── behaviors/
│   ├── latex-authoring.yaml
│   ├── figure-generation.yaml
│   ├── conference-styling.yaml
│   └── paperbanana.yaml                         # NEW
├── agents/
│   └── figure-artist.md                         # MODIFIED - add PaperBanana section
├── modules/
│   └── tool-paperbanana/                        # NEW - entire module
│       ├── pyproject.toml
│       ├── README.md
│       └── tool_paperbanana/
│           ├── __init__.py
│           ├── mount.py
│           ├── retriever.py
│           ├── planner.py
│           ├── visualizer.py
│           ├── critic.py
│           └── utils.py
├── recipes/
│   └── paperbanana-figure.yaml                  # NEW
└── context/
    └── paperbanana-methodology.md               # NEW
```

### Testing Strategy for Phase 1

#### Test 1: Tool Module Direct Use
```bash
amplifier run --bundle scientificpaper "Use tool-paperbanana to generate a methodology diagram"
```

#### Test 2: Agent Intelligent Use
```bash
amplifier run --bundle scientificpaper "Create a figure for my transformer paper using automated refinement"
```

#### Test 3: Recipe Workflow
```bash
amplifier run "execute recipes/paperbanana-figure.yaml with \
  paper_content='Abstract: We propose...' \
  figure_type='methodology' \
  conference='neurips'"
```

Expected: Approval gate, quality validation, conditional refinement

---

## Phase 2: Specialized Agents (Future Enhancement)

### Objective
Add explicit control over each PaperBanana stage with dedicated agents. Only implement if Phase 1 usage patterns show need for fine-grained orchestration.

### Additional Deliverables

#### 1. Five Specialized Agents

Create in `agents/` directory:

- **`paperbanana-retriever.md`** - Context extraction specialist
- **`paperbanana-planner.md`** - Content planning specialist
- **`paperbanana-stylist.md`** - Style planning specialist
- **`paperbanana-visualizer.md`** - Figure generation specialist
- **`paperbanana-critic.md`** - Quality validation specialist

Each agent:
- 100+ word meta.description with WHY/WHEN/WHAT/HOW
- 5+ examples with commentary
- Context sink for its domain
- @mentions to paperbanana-methodology.md

#### 2. Enhanced Behavior

Update `behaviors/paperbanana.yaml` to include specialized agents:

```yaml
agents:
  include:
    - scientificpaper:figure-artist           # Still available
    - scientificpaper:paperbanana-retriever
    - scientificpaper:paperbanana-planner
    - scientificpaper:paperbanana-stylist
    - scientificpaper:paperbanana-visualizer
    - scientificpaper:paperbanana-critic
```

#### 3. Advanced Recipes

Create specialized recipes in `recipes/`:

- **`paperbanana-methodology.yaml`** - Optimized for methodology diagrams
- **`paperbanana-plot.yaml`** - Optimized for statistical plots
- **`paperbanana-architecture.yaml`** - Optimized for neural architectures
- **`paperbanana-custom.yaml`** - Full control over all parameters

Each uses the 5 specialized agents explicitly.

### When to Implement Phase 2

Implement Phase 2 if:
- Users frequently need to customize specific stages
- Research/experimentation with PaperBanana approach
- Want explicit control over each agent's role
- Phase 1 shows limitations in complex scenarios

---

## Implementation Checklist

### Phase 1 (Minimal Viable)

- [ ] **Tool Module**
  - [ ] Create `modules/tool-paperbanana/` structure
  - [ ] Implement `mount.py` with Tool protocol
  - [ ] Implement retriever.py (context extraction)
  - [ ] Implement planner.py (content + style planning)
  - [ ] Implement visualizer.py (figure generation)
  - [ ] Implement critic.py (8 quality veto rules)
  - [ ] Add pyproject.toml with dependencies
  - [ ] Write README.md with usage examples

- [ ] **Behavior Bundle**
  - [ ] Create `behaviors/paperbanana.yaml`
  - [ ] Declare tool-paperbanana with config
  - [ ] Include figure-artist agent
  - [ ] Include methodology context

- [ ] **Enhanced Agent**
  - [ ] Update `agents/figure-artist.md`
  - [ ] Add PaperBanana integration section
  - [ ] Document when to use tool-paperbanana
  - [ ] Add quality veto rules documentation
  - [ ] Include usage examples

- [ ] **Context Documentation**
  - [ ] Create `context/paperbanana-methodology.md`
  - [ ] Document 5-agent architecture
  - [ ] Explain quality evaluation metrics
  - [ ] Add references to arXiv paper

- [ ] **Recipe**
  - [ ] Create `recipes/paperbanana-figure.yaml`
  - [ ] Implement planning stage with approval
  - [ ] Implement generation stage with validation
  - [ ] Implement conditional refinement stage
  - [ ] Add usage documentation

- [ ] **Bundle Integration**
  - [ ] Update `bundle.md` to include paperbanana behavior
  - [ ] Test bundle loading
  - [ ] Verify agents discoverable

- [ ] **Testing**
  - [ ] Test tool direct use
  - [ ] Test agent intelligent use
  - [ ] Test recipe workflow end-to-end
  - [ ] Validate quality veto rules
  - [ ] Test approval gate functionality

### Phase 2 (Future Enhancement)

- [ ] Create 5 specialized agents (retriever, planner, stylist, visualizer, critic)
- [ ] Update paperbanana.yaml to include new agents
- [ ] Create advanced recipes for specific use cases
- [ ] Add agent-specific context documentation
- [ ] Test fine-grained orchestration
- [ ] Document when to use specialized vs. enhanced figure-artist

---

## Dependencies

### Python Packages (for tool-paperbanana)

```toml
[project]
name = "tool-paperbanana"
version = "1.0.0"
requires-python = ">=3.10"
dependencies = [
    "matplotlib>=3.7.0",
    "tikzplotlib>=0.10.0",
    "scienceplots>=2.1.0",
    "seaborn>=0.12.0",
    "numpy>=1.24.0",
    "pandas>=2.0.0",
    "colorcet>=3.0.0",        # ColorBrewer palettes
    "pillow>=10.0.0",
    "cairosvg>=2.7.0",        # SVG conversion
]
```

### External APIs (Optional)

If using Gemini API for generation (from PaperBanana paper):
- Google Cloud AI credentials
- Gemini-3-Pro access
- Nano-Banana-Pro model access

**Note:** Phase 1 can work without external APIs using matplotlib/tikz generation locally.

---

## Success Metrics

### Phase 1 Success Criteria

1. ✅ All 3 layers functional (tool, agent, recipe)
2. ✅ 8 quality veto rules enforced
3. ✅ Approval gates working in recipe
4. ✅ Conditional refinement based on quality
5. ✅ Figure-artist intelligently uses tool-paperbanana
6. ✅ Generated figures pass quality validation

### Phase 2 Success Criteria

1. ✅ 5 specialized agents discoverable
2. ✅ Fine-grained control over each stage
3. ✅ Advanced recipes using specialized agents
4. ✅ Context sinks properly distributed

---

## Architecture Principles Applied

### ✅ Mechanism, Not Policy
- Tool provides capability (mechanism)
- Agent makes decisions (intelligence)
- Recipe orchestrates explicitly (policy)

### ✅ Ruthless Simplicity
- Start minimal (Phase 1)
- Add complexity only when needed (Phase 2)
- Don't over-engineer upfront

### ✅ Bricks & Studs
- Tool module is self-contained
- Stable Tool protocol interface
- Can be swapped/enhanced independently

### ✅ Context Sinks
- figure-artist sinks heavy PaperBanana docs
- Docs load only when agent spawns
- Parent session stays lean

### ✅ Thin Bundle Pattern
- Inherits from foundation
- Behaviors package capabilities
- No duplication

### ✅ Composable Layers
- Each layer builds on previous
- Can be used independently
- Clear separation of concerns

---

## Next Steps

1. **Review this plan** with the user
2. **Delegate to modular-builder** for implementation:
   - Tool module implementation
   - Behavior creation
   - Agent enhancement
   - Recipe creation
3. **Test Phase 1** thoroughly before considering Phase 2
4. **Gather usage feedback** to inform Phase 2 priorities
5. **Document patterns** for future bundle authors

---

## Questions for User

Before implementation:

1. Do you have access to Gemini API for generation, or should we focus on matplotlib/tikz local generation?
2. Any specific figure types to prioritize (methodology, plots, architectures)?
3. Should we mock tool-paperbanana initially for faster testing, or implement fully?
4. Are there additional quality veto rules beyond the 8 from PaperBanana paper?

---

**Status:** Architecture complete, ready for implementation delegation
