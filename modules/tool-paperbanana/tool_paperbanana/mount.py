"""
PaperBanana Tool Mount: Main entry point implementing Tool protocol.

Orchestrates the 5-agent PaperBanana workflow:
Retriever → Planner → Stylist → Visualizer → Critic
"""

import json
from typing import Any

from amplifier_core import ToolResult  # type: ignore[import]

from .critic import Critic
from .planner import Planner
from .retriever import Retriever
from .visualizer import Visualizer


class PaperBananaToolMount:
    """
    Tool mount for PaperBanana multi-agent figure generation.

    Implements the Tool protocol for Amplifier.
    """

    def __init__(self, config: dict[str, Any] | None = None):
        """
        Initialize PaperBanana tool with configuration.

        Args:
            config: Optional configuration dict with:
                - default_max_iterations: Max refinement iterations (default: 3)
                - default_quality_rules: Quality rules to enforce
                - output_dir: Directory for generated figures (default: "figures")
        """
        self.config = config or {}
        self.default_max_iterations = self.config.get("default_max_iterations", 3)
        self.default_quality_rules = self.config.get(
            "default_quality_rules",
            [
                "no_low_quality_artifacts",
                "professional_colors",
                "no_black_backgrounds",
                "modern_style",
                "vector_preferred",
                "appropriate_aspect_ratio",
                "clear_labels",
                "data_integrity",
            ],
        )
        self.output_dir = self.config.get("output_dir", "figures")

        # Initialize components
        self.retriever = Retriever()
        self.planner = Planner()
        self.visualizer = Visualizer(output_dir=self.output_dir)
        self.critic = Critic()

    @property
    def name(self) -> str:
        """Tool name for Amplifier registration."""
        return "paperbanana"

    @property
    def description(self) -> str:
        """Tool description shown to the LLM."""
        return (
            "Generate publication-quality academic figures using the PaperBanana "
            "multi-agent pipeline (arXiv 2601.23265). Extracts key concepts from "
            "paper text, plans content and style, generates figures via Gemini/Imagen, "
            "and applies 8 quality veto rules with iterative refinement."
        )

    @property
    def input_schema(self) -> dict[str, Any]:
        """JSON schema for tool inputs."""
        return {
            "type": "object",
            "properties": {
                "paper_content": {
                    "type": "string",
                    "description": (
                        "Paper text (abstract and methods section) to generate a figure for"
                    ),
                },
                "figure_type": {
                    "type": "string",
                    "enum": ["methodology", "plot", "architecture"],
                    "description": "Type of figure to generate",
                },
                "style_requirements": {
                    "type": "object",
                    "description": (
                        "Visual style requirements (conference, colorblind_safe, width_inches)"
                    ),
                },
                "quality_rules": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Quality veto rules to enforce (defaults to all 8 rules)",
                },
                "max_iterations": {
                    "type": "integer",
                    "description": "Maximum refinement iterations (default: 3)",
                },
            },
            "required": ["paper_content"],
        }

    async def execute(self, input_data: dict[str, Any]) -> ToolResult:
        """
        Execute PaperBanana workflow to generate a figure.

        Args:
            input_data: Dict with:
                - paper_content: str (required) - Paper text (abstract + methods)
                - figure_type: str - "methodology" | "plot" | "architecture"
                - style_requirements: dict - Conference, colorblind_safe, width
                - quality_rules: list[str] - Veto rules to enforce
                - max_iterations: int - Refinement attempts

        Returns:
            ToolResult with JSON-serialized payload containing:
                - success: bool
                - figure_path: str (if success)
                - format: str (if success)
                - metadata: dict
                - error: str (if failure)
        """
        try:
            # Extract and validate inputs
            paper_content = input_data.get("paper_content", "")
            if not paper_content:
                return ToolResult(
                    success=False,
                    output=json.dumps({"success": False, "error": "paper_content is required"}),
                )

            style_requirements = input_data.get("style_requirements", {})
            quality_rules = input_data.get("quality_rules", self.default_quality_rules)
            max_iterations = input_data.get("max_iterations", self.default_max_iterations)

            # STAGE 1: Retrieve context from paper
            context = self.retriever.extract(paper_content)

            # STAGE 2: Plan content (what to include)
            content_plan = self.planner.plan_content(context)

            # STAGE 3: Plan style (visual aesthetics)
            style_plan = self.planner.plan_style(context, style_requirements)

            # STAGE 4: Generate initial figure
            figure = self.visualizer.generate(content_plan, style_plan)

            # STAGE 5: Iterative refinement with critic
            critique = None
            iteration_count = 0

            for i in range(max_iterations):
                iteration_count = i + 1

                # Evaluate quality
                critique = self.critic.evaluate(figure, quality_rules)

                if critique.passed:
                    # Quality check passed!
                    break

                if i < max_iterations - 1:
                    # Try to refine
                    figure = self.visualizer.refine(figure, critique)

            # Return results
            if critique:
                payload = {
                    "success": critique.passed,
                    "figure_path": figure.path,
                    "format": figure.format,
                    "metadata": {
                        "iterations": iteration_count,
                        "rules_passed": critique.passed_rules,
                        "rules_failed": critique.failed_rules,
                        "critique": critique.summary,
                        "severity": critique.severity,
                        "width_inches": figure.width_inches,
                        "height_inches": figure.height_inches,
                        "num_elements": figure.metadata.get("num_elements", 0),
                        "layout": figure.metadata.get("layout", "unknown"),
                    },
                    "error": None if critique.passed else f"Quality issues: {critique.severity}",
                }
                return ToolResult(success=critique.passed, output=json.dumps(payload))
            else:
                # No critique (shouldn't happen)
                payload = {
                    "success": True,
                    "figure_path": figure.path,
                    "format": figure.format,
                    "metadata": {
                        "iterations": iteration_count,
                        "width_inches": figure.width_inches,
                        "height_inches": figure.height_inches,
                    },
                }
                return ToolResult(success=True, output=json.dumps(payload))

        except Exception as e:
            payload = {
                "success": False,
                "error": f"PaperBanana execution failed: {str(e)}",
            }
            return ToolResult(success=False, output=json.dumps(payload))
