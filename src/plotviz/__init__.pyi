"""
plotviz
---

Provides shorthands for consistent and faster matplotlib plotting.
"""

from typing import Any, Optional, Dict
from .core import Plot as Plot

THEMES: Dict[str, Any]

def use(theme_name: str = "standard") -> None: ...
def show(plot_handle: Plot) -> None: ...
def snapshot(plot_handle: Plot, filename: Optional[str] = ...) -> None: ...
def save_figure(script_path: str, add_axes: bool = ..., color: str = ...) -> None: ...

class plot(Plot): ...

__all__ = ["use", "plot", "show", "snapshot", "save_figure", "THEMES"]
