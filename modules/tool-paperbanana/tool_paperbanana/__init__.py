"""
PaperBanana: Multi-agent academic illustration generation tool.

Implements the PaperBanana architecture from arXiv 2601.23265.
"""

__version__ = "1.0.0"

from typing import Any

from .mount import PaperBananaToolMount


async def mount(coordinator: Any, config: dict[str, Any] | None = None) -> None:
    """
    Amplifier module entry point.

    Instantiates PaperBananaToolMount and registers it with the coordinator.
    """
    tool = PaperBananaToolMount(config)
    await coordinator.mount("tools", tool, name=tool.name)


__all__ = ["PaperBananaToolMount", "mount"]
