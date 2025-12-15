from ._internal import plt, os, PlotContext, GridContext


def save_figure(script_path: str, add_axes: bool = True, color: str = "black"):
    """
    Saves figure.
    """
    if add_axes:
        plt.axhline(0, color=color, linewidth=0.8)
        plt.axvline(0, color=color, linewidth=0.8)

    if os.path.isabs(script_path) or "/" in script_path or "\\" in script_path:
        base_name = os.path.splitext(os.path.basename(script_path))[0]
    else:
        base_name = script_path

    filename = f"{base_name}.svg"

    plt.savefig(filename, bbox_inches="tight", transparent=True)
    print(f"Saved: {filename}")


def apply_layout(ctx: PlotContext, grd: GridContext):
    if ctx.figsize:
        plt.gcf().set_size_inches(*ctx.figsize)

    ax = plt.gca()

    if ctx.style_naked:
        ax.spines["left"].set_position(("data", 0))
        ax.spines["bottom"].set_position(("data", 0))
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    if grd:
        # Defaults from the current rcParams
        grid_kw = {
            "color": plt.rcParams.get("grid.color", "gray"),
            "linestyle": plt.rcParams.get("grid.linestyle", "-"),
            "linewidth": plt.rcParams.get("grid.linewidth", 0.8),
        }

        # Apply grid visibility
        ax.grid(visible=grd.grid_enabled, alpha=grd.grid_alpha, **grid_kw)

        # Apply Axis Lines (at x=0 and y=0)
        # Use theme's edge color so it works in dark mode
        axis_col = plt.rcParams.get("axes.edgecolor", "black")

        show_x, show_y = False, False

        if isinstance(grd.axis_enabled, bool):
            show_x = grd.axis_enabled
            show_y = grd.axis_enabled
        elif isinstance(grd.axis_enabled, tuple) and len(grd.axis_enabled) == 2:
            show_x, show_y = grd.axis_enabled

        if show_x:
            plt.axhline(0, color=axis_col, linewidth=0.8)
        if show_y:
            plt.axvline(0, color=axis_col, linewidth=0.8)

        # Apply Limits
        if all(v is not None for v in [grd.xmin, grd.xmax, grd.ymin, grd.ymax]):
            ax.axis((grd.xmin, grd.xmax, grd.ymin, grd.ymax))
        else:
            if grd.xmin is not None:
                ax.set_xlim(left=grd.xmin)
            if grd.xmax is not None:
                ax.set_xlim(right=grd.xmax)
            if grd.ymin is not None:
                ax.set_ylim(bottom=grd.ymin)
            if grd.ymax is not None:
                ax.set_ylim(top=grd.ymax)
