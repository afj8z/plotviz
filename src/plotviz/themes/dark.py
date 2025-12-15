# Import from private header
from .._internal import plt, cycler, DEFAULT_COLORS


def apply():
    c = DEFAULT_COLORS
    plt.rcParams["figure.facecolor"] = c["black"]
    plt.rcParams["axes.facecolor"] = c["black"]
    plt.rcParams["text.color"] = c["white"]
    plt.rcParams["axes.labelcolor"] = c["white"]
    plt.rcParams["xtick.color"] = c["white"]
    plt.rcParams["ytick.color"] = c["white"]

    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.color"] = c["white"]
    plt.rcParams["grid.alpha"] = 0.2

    # Lighter cycle for contrast against dark bg
    custom_cycle = cycler(color=[c["sky"], c["orange"], c["yellow"]])
    plt.rcParams["axes.prop_cycle"] = custom_cycle
