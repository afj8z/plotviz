def pltall(func_list: list[tuple(int | float)]):
    for fun in func_list:
        plt.show(*fun)
