"""
Visualizer Agent: Generate figures from content and style plans.

Implements the fourth stage of the PaperBanana multi-agent architecture.
"""

import os
from pathlib import Path
from typing import Any

from .utils import ContentPlan, Critique, Figure, StylePlan


class Visualizer:
    """Generate figures using matplotlib/tikz based on plans."""

    def __init__(self, output_dir: str = "figures"):
        """Initialize visualizer with output directory."""
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True, parents=True)

    def generate(self, content_plan: ContentPlan, style_plan: StylePlan) -> Figure:
        """
        Generate initial figure from plans.

        Args:
            content_plan: What to include in the figure
            style_plan: Visual aesthetics

        Returns:
            Figure object with path and metadata
        """
        # Import matplotlib here to avoid issues if not installed
        try:
            import matplotlib.pyplot as plt
        except ImportError as e:
            raise RuntimeError("matplotlib is required for figure generation") from e

        # Create figure with specified dimensions
        fig, ax = plt.subplots(figsize=(style_plan.width_inches, style_plan.height_inches), dpi=300)

        # Apply style
        self._apply_style(fig, ax, style_plan)

        # Generate based on layout
        if style_plan.layout == "horizontal":
            self._generate_horizontal_layout(ax, content_plan, style_plan)
        elif style_plan.layout == "vertical":
            self._generate_vertical_layout(ax, content_plan, style_plan)
        else:
            self._generate_grid_layout(ax, content_plan, style_plan)

        # Add relationships (arrows)
        self._add_relationships(ax, content_plan, style_plan)

        # Save figure
        output_path = self.output_dir / f"figure_{os.getpid()}.{style_plan.format}"
        plt.tight_layout()
        plt.savefig(
            output_path,
            format=style_plan.format,
            bbox_inches="tight",
            dpi=300 if style_plan.format == "png" else None,
        )
        plt.close()

        return Figure(
            path=str(output_path),
            format=style_plan.format,
            width_inches=style_plan.width_inches,
            height_inches=style_plan.height_inches,
            metadata={
                "num_elements": len(content_plan.elements),
                "num_relationships": len(content_plan.relationships),
                "layout": style_plan.layout,
            },
        )

    def refine(self, figure: Figure, critique: Critique) -> Figure:
        """
        Refine figure based on critique.

        Args:
            figure: Current figure
            critique: Quality validation results

        Returns:
            Refined Figure object
        """
        # For now, this is a simplified refinement
        # In a full implementation, this would parse the critique
        # and make specific adjustments based on failed rules

        # Generate a new figure with adjustments
        # This is a placeholder - full implementation would be more sophisticated

        return figure  # Return same figure for now

    def _apply_style(self, fig: Any, ax: Any, style_plan: StylePlan) -> None:
        """Apply style settings to figure."""
        # Set font
        import matplotlib.pyplot as plt

        plt.rcParams["font.family"] = style_plan.font_family
        plt.rcParams["font.size"] = style_plan.font_size

        # Remove axes for diagram-style figures
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")

    def _generate_horizontal_layout(
        self, ax: Any, content_plan: ContentPlan, style_plan: StylePlan
    ) -> None:
        """Generate horizontal pipeline layout."""
        import matplotlib.patches as mpatches

        elements = content_plan.elements
        num_elements = len(elements)

        if num_elements == 0:
            return

        # Calculate spacing
        spacing = 8.0 / num_elements
        x_positions = {}

        # Draw boxes
        for i, element in enumerate(elements):
            x = 1.0 + i * spacing
            y = 5.0
            x_positions[element] = (x, y)

            # Determine color based on hierarchy
            priority = content_plan.hierarchy.get(element, 2)
            color_idx = min(i, len(style_plan.color_scheme) - 1)
            color = style_plan.color_scheme[color_idx]

            # Draw box
            box = mpatches.FancyBboxPatch(
                (x - 0.4, y - 0.5),
                0.8,
                1.0,
                boxstyle="round,pad=0.1",
                facecolor=color,
                edgecolor="black",
                linewidth=2 if priority == 1 else 1,
                alpha=0.7,
            )
            ax.add_patch(box)

            # Add label
            label = content_plan.labels.get(element, element)
            # Truncate if too long
            if len(label) > 20:
                label = label[:17] + "..."

            ax.text(
                x,
                y,
                label,
                ha="center",
                va="center",
                fontsize=style_plan.font_size,
                fontweight="bold" if priority == 1 else "normal",
                wrap=True,
            )

        # Store for relationship drawing
        self._element_positions = x_positions

    def _generate_vertical_layout(
        self, ax: Any, content_plan: ContentPlan, style_plan: StylePlan
    ) -> None:
        """Generate vertical architecture layout."""
        import matplotlib.patches as mpatches

        elements = content_plan.elements
        num_elements = len(elements)

        if num_elements == 0:
            return

        # Calculate spacing
        spacing = 8.0 / num_elements
        x_positions = {}

        # Draw boxes
        for i, element in enumerate(elements):
            x = 5.0
            y = 9.0 - i * spacing
            x_positions[element] = (x, y)

            # Determine color
            color_idx = min(i, len(style_plan.color_scheme) - 1)
            color = style_plan.color_scheme[color_idx]
            priority = content_plan.hierarchy.get(element, 2)

            # Draw box
            box = mpatches.FancyBboxPatch(
                (x - 1.5, y - 0.4),
                3.0,
                0.8,
                boxstyle="round,pad=0.1",
                facecolor=color,
                edgecolor="black",
                linewidth=2 if priority == 1 else 1,
                alpha=0.7,
            )
            ax.add_patch(box)

            # Add label
            label = content_plan.labels.get(element, element)
            if len(label) > 30:
                label = label[:27] + "..."

            ax.text(
                x,
                y,
                label,
                ha="center",
                va="center",
                fontsize=style_plan.font_size,
                fontweight="bold" if priority == 1 else "normal",
            )

        self._element_positions = x_positions

    def _generate_grid_layout(
        self, ax: Any, content_plan: ContentPlan, style_plan: StylePlan
    ) -> None:
        """Generate grid network layout."""
        import math

        import matplotlib.patches as mpatches

        elements = content_plan.elements
        num_elements = len(elements)

        if num_elements == 0:
            return

        # Calculate grid dimensions
        cols = math.ceil(math.sqrt(num_elements))
        rows = math.ceil(num_elements / cols)

        x_spacing = 8.0 / cols
        y_spacing = 8.0 / rows

        x_positions = {}

        # Draw nodes in grid
        for i, element in enumerate(elements):
            row = i // cols
            col = i % cols

            x = 1.0 + col * x_spacing + x_spacing / 2
            y = 9.0 - row * y_spacing - y_spacing / 2
            x_positions[element] = (x, y)

            # Determine color
            color_idx = min(i, len(style_plan.color_scheme) - 1)
            color = style_plan.color_scheme[color_idx]
            priority = content_plan.hierarchy.get(element, 2)

            # Draw circle
            circle = mpatches.Circle(
                (x, y),
                0.4,
                facecolor=color,
                edgecolor="black",
                linewidth=2 if priority == 1 else 1,
                alpha=0.7,
            )
            ax.add_patch(circle)

            # Add label
            label = content_plan.labels.get(element, element)
            if len(label) > 15:
                label = label[:12] + "..."

            ax.text(
                x,
                y,
                label,
                ha="center",
                va="center",
                fontsize=style_plan.font_size - 1,
                fontweight="bold" if priority == 1 else "normal",
            )

        self._element_positions = x_positions

    def _add_relationships(self, ax: Any, content_plan: ContentPlan, style_plan: StylePlan) -> None:
        """Add arrows for relationships between elements."""
        if not hasattr(self, "_element_positions"):
            return

        import matplotlib.patches as mpatches

        for source, target in content_plan.relationships:
            if source not in self._element_positions or target not in self._element_positions:
                continue

            x1, y1 = self._element_positions[source]
            x2, y2 = self._element_positions[target]

            # Draw arrow
            arrow = mpatches.FancyArrowPatch(
                (x1, y1),
                (x2, y2),
                arrowstyle="->",
                mutation_scale=20,
                linewidth=1.5,
                color="gray",
                alpha=0.6,
            )
            ax.add_patch(arrow)
