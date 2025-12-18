from .._internal import plt, norm, arange


def densfunc(xmin, xmax):
    x = arange(xmin, xmax, 0.001)
    plt.plot(x, norm.pdf(x))
    plt.show()
