from .._internal import plt, cycler, DEFAULT_COLORS, CoordPair


def set_style(fig_xy: CoordPair = (10, 6)):
    """Overwrites matplotlib defaults with user preferences"""
    c = DEFAULT_COLORS
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.serif"] = ["IBM Plex Serif"] + plt.rcParams["font.serif"]
    plt.rcParams["font.size"] = 12
    plt.rcParams["text.color"] = c["black"]

    plt.rcParams["axes.labelcolor"] = c["black"]
    plt.rcParams["axes.titlecolor"] = c["black"]
    plt.rcParams["xtick.color"] = c["black"]
    plt.rcParams["ytick.color"] = c["black"]

    plt.rcParams["axes.spines.top"] = False
    plt.rcParams["axes.spines.right"] = False

    custom_cycle = cycler(
        color=[
            c["blue"],
            c["red"],
            c["green"],
            c["orange"],
            c["sky"],
            c["yellow"],
        ]
    )
    plt.rcParams["axes.prop_cycle"] = custom_cycle

    plt.rcParams["lines.linewidth"] = 2.5
    plt.rcParams["lines.markersize"] = 8

    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.color"] = c["black"]
    plt.rcParams["grid.alpha"] = 0.15
    plt.rcParams["grid.linestyle"] = "--"

    plt.rcParams["figure.figsize"] = fig_xy
    plt.rcParams["figure.autolayout"] = True
