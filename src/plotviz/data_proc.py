from ._internal import plt, Number


def _pltall_array(func_list: list[tuple[Number, Number]]):
    """Plots all tuples in the provided list."""
    for fun in func_list:
        plt.plot(*fun)


def _pltall_dict(func_list: dict[str, Number]):
    """Plots all tuples in the provided list."""
    for name, fun in func_list:
        plt.plot(*fun)


def _pltarray_singlex(x, func_list: list[tuple[Number]] | None):
    """Plots all tuples in the provided list."""
    if func_list:
        for fun in func_list:
            plt.plot(x, fun)
