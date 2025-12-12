import os
import matplotlib.pyplot as plt


def save_figure(script_path: str, add_axes: bool = True, color: str = "black"):
    """Saves figure as a transparent png based on script name.

    Parameters
    ----------
    script_path: str
        The path to the script in which function is called
    add_axes: bool, optional
        Draw the x and y axis in plot (default is True)
    color: str, optional
        Color for the axis (default is 'black')
    """
    if add_axes:
        plt.axhline(0, color=color, linewidth=0.8)
        plt.axvline(0, color=color, linewidth=0.8)

    base_name = os.path.splitext(os.path.basename(script_path))[0]
    filename = f"{base_name}.svg"

    plt.savefig(filename, bbox_inches="tight", transparent=True)
    print(f"Saved: {filename}")
