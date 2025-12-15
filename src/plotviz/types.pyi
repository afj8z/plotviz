from dataclasses import dataclass

CoordPair = tuple[int | float, int | float]
Number = int | float

@dataclass
class GridContext:
    xmin: Number | None = None
    xmax: Number | None = None
    ymin: Number | None = None
    ymax: Number | None = None
    grid_alpha: float = 0.15
    grid_enabled: bool = True
    axis_enabled: bool | tuple[bool, bool] = True

@dataclass
class PlotContext:
    figsize: CoordPair = (10, 6)
    style_naked: bool = False
    theme: str | None = None
