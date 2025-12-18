"""
Core Logic: Defines global configuration verbs and the Plot handle.
"""

from ._internal import plt, linspace, PlotContext, GridContext, DataContext, Number
from .utils import apply_layout, save_figure
from .themes import THEMES
from .data_proc import _pltarray_singlex

_active_theme = "standard"


def _apply_theme(theme_name: str):
    """Internal helper to apply a theme to rcParams."""
    if theme_name not in THEMES:
        valid = list(THEMES.keys())
        raise ValueError(f"Theme '{theme_name}' not found. Available: {valid}")

    plt.rcdefaults()
    mod = THEMES[theme_name]
    mod.apply() if hasattr(mod, "apply") else mod.set_style()


def use(theme_name: str = "standard"):
    """
    Sets the global matplotlib theme.
    """
    global _active_theme
    _active_theme = theme_name
    _apply_theme(theme_name)
    print(f"Using style: {theme_name}")


class Plot:
    """
    Configuration handle for a plot.
    """

    def __init__(self):
        self.ctx = PlotContext()
        self.grd = GridContext()
        self.dta = DataContext()
        self.ctx.theme = _active_theme

    def style(
        self,
        fig_size: tuple[float, float] | None = None,
        style: str | None = None,
        theme: str | None = None,
    ):
        """
        Sets visual style parameters.
        If a theme is provided, it is applied immediately to global rcParams.
        """
        if fig_size:
            self.ctx.figsize = fig_size

        if style == "naked":
            self.ctx.style_naked = True

        if theme:
            self.ctx.theme = theme
            # Apply immediately so subsequent plotting uses correct colors
            _apply_theme(theme)

        return self

    def grid(
        self,
        lim: tuple[float, float, float, float] | None = None,
        enabled: bool | None = None,
        alpha: float | None = None,
        axis: bool | tuple[bool, bool] = True,
    ):
        """Sets grid limits (xmin, xmax, ymin, ymax) and style."""
        if lim and len(lim) == 4:
            self.grd.xmin = lim[0]
            self.grd.xmax = lim[1]
            self.grd.ymin = lim[2]
            self.grd.ymax = lim[3]

        if enabled is not None:
            self.grd.grid_enabled = enabled

        if alpha is not None:
            self.grd.grid_alpha = alpha

        if axis:
            self.grd.axis_enabled = axis

        return self

    def data(
        self,
        x: tuple[Number, Number, Number] | None = None,
        f: list[tuple[Number]] | None = None,
    ):
        if x is not None:
            self.dta.xstart = x[0]
            self.dta.xend = x[1]
            self.dta.xsamp = x[2]

        if f is not None:
            self.dta.lines = f
        return self


def show(plot_handle: Plot):
    """Applies settings and shows the plot."""
    # consistent theme settings
    if plot_handle.ctx.theme:
        _apply_theme(plot_handle.ctx.theme)
    if all(
        v is not None
        for v in [
            plot_handle.dta.xstart,
            plot_handle.dta.xend,
            plot_handle.dta.xsamp,
            plot_handle.dta.lines,
        ]
    ):
        x = linspace(
            plot_handle.dta.xstart,
            plot_handle.dta.xend,
            plot_handle.dta.xsamp,
        )
        funxs = plot_handle.dta.lines
        _pltarray_singlex(x, funxs)

    apply_layout(plot_handle.ctx, plot_handle.grd)
    plt.show()


def snapshot(plot_handle: Plot, filename: str | None = None):
    """Applies settings, saves, and shows."""
    if plot_handle.ctx.theme:
        _apply_theme(plot_handle.ctx.theme)

    apply_layout(plot_handle.ctx, plot_handle.grd)
    save_figure(script_path=filename if filename else __file__)
    plt.show()
