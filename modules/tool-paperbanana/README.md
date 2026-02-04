# PaperBanana Tool Module

Multi-agent academic illustration generation tool based on PaperBanana (arXiv 2601.23265).

## Overview

This tool implements the PaperBanana architecture for automating publication-ready academic figure generation. It orchestrates five specialized agents:

1. **Retriever** - Extract context from paper content
2. **Planner** - Plan content and style
3. **Visualizer** - Generate figures
4. **Critic** - Validate quality with 8 veto rules
5. **Refinement Loop** - Iterative improvement

## Usage

### From Python

```python
from tool_paperbanana import PaperBananaToolMount

# Initialize tool
tool = PaperBananaToolMount(config={
    "output_dir": "figures",
    "default_max_iterations": 3
})

# Generate figure
result = tool.execute_sync({
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

print(result["figure_path"])  # Path to generated figure
print(result["metadata"])     # Quality metrics and iterations
```

### From Amplifier

The tool is automatically registered when the `paperbanana` behavior is included in a bundle.

```yaml
# bundle.md
behaviors:
  include:
    - scientificpaper:behaviors/paperbanana
```

Then use via figure-artist agent or directly:

```
"Create a methodology diagram for my transformer paper using PaperBanana"
```

## Quality Veto Rules

8 red-line rules from PaperBanana research:

1. **no_low_quality_artifacts** - No grid artifacts, blur, distortion
2. **professional_colors** - ColorBrewer palettes, no neon
3. **no_black_backgrounds** - White/light backgrounds only
4. **modern_style** - Professional fonts, minimal clip-art
5. **vector_preferred** - PDF/SVG over PNG
6. **appropriate_aspect_ratio** - Conference-appropriate dimensions
7. **clear_labels** - Legible text at print size
8. **data_integrity** - Accurate data representation

## Configuration

### Tool Config

```yaml
tools:
  - module: tool-paperbanana
    config:
      default_max_iterations: 3
      output_dir: "figures"
      default_quality_rules:
        - "no_low_quality_artifacts"
        - "professional_colors"
        # ... all 8 rules
```

### Conference Specs

Supports: neurips, icml, acl, ieee, acm

Automatically adapts figure dimensions and styling to conference requirements.

## Dependencies

- matplotlib>=3.7.0
- tikzplotlib>=0.10.0
- scienceplots>=2.1.0
- seaborn>=0.12.0
- numpy>=1.24.0
- pandas>=2.0.0
- colorcet>=3.0.0 (ColorBrewer palettes)
- pillow>=10.0.0

## Output

Returns:

```python
{
    "success": bool,
    "figure_path": str,          # Path to generated figure
    "format": str,                # "pdf" | "svg" | "png"
    "metadata": {
        "iterations": int,         # Refinement iterations used
        "rules_passed": list[str], # Quality rules that passed
        "rules_failed": list[str], # Quality rules that failed
        "critique": str,           # Human-readable summary
        "severity": str,           # "pass" | "minor" | "major" | "critical"
        "width_inches": float,
        "height_inches": float,
        "num_elements": int,
        "layout": str              # "horizontal" | "vertical" | "grid"
    },
    "error": str | None           # Error message if failed
}
```

## Architecture

Following Amplifier's **mechanism, not policy** philosophy:

- **Mechanism**: This tool provides figure generation capability
- **Intelligence**: figure-artist agent decides when to use it
- **Policy**: Recipes orchestrate multi-stage workflows

## References

- Paper: https://arxiv.org/abs/2601.23265
- GitHub: https://dwzhu-pku.github.io/PaperBanana/
- Bundle: @scientificpaper:behaviors/paperbanana
