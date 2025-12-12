import matplotlib.pyplot as plt
from .utils import save_figure as save
from .themes import standard, dark, academic

THEMES = {"standard": standard, "dark": dark, "academic": academic}


def use(theme_name="standard"):
    """Apply a specific style template.

    Parameters
    ----------
    theme_name: str, optional
        Set the theme. One of 'standard', 'dark', 'academic'
        (default is 'standard')
    """
    if theme_name not in THEMES:
        raise ValueError(
            f"Theme '{theme_name}' not found. Available: {list(THEMES.keys())}"
        )

    plt.rcdefaults()

    THEMES[theme_name].apply()
    print(f"Using style: {theme_name}")
