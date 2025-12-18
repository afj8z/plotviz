from dataclasses import dataclass
from typing import TypeAlias

# Type Aliases
CoordPair: TypeAlias = tuple[int | float, int | float]
Number: TypeAlias = int | float


# Dataclasses
@dataclass
class GridContext:
    """Struct to hold grid and axis settings."""

    xmin: Number | None = None
    xmax: Number | None = None
    ymin: Number | None = None
    ymax: Number | None = None
    grid_alpha: float = 0.15
    grid_enabled: bool = True
    axis_enabled: bool | tuple[bool, bool] = True


@dataclass
class PlotContext:
    """Struct to hold plot layout configuration."""

    theme: str | None = None
    figsize: CoordPair = (10, 6)
    style_naked: bool = False


@dataclass
class DataContext:
    """Struct to hold data that populates the plot."""

    xstart: Number | None = None
    xend: Number | None = None
    xsamp: Number | None = None
    lines: list[tuple[Number]] | None = None
