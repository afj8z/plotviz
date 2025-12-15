"""
plotviz
---

Provides shorthands for consistent and faster matplotlib plotting.
"""

from .core import use, Plot, show, snapshot

from .utils import save_figure

from .themes import THEMES

plot = Plot

__all__ = ["use", "plot", "show", "snapshot", "save_figure", "THEMES"]
