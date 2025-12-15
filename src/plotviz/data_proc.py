from ._internal import plt, Number


def pltall(func_list: list[tuple[Number, ...]]):
    """Plots all tuples in the provided list."""
    for fun in func_list:
        plt.plot(*fun)
