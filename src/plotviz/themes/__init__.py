from . import standard, dark, academic

# Define Registry here so both core.py and __init__.py can see it
THEMES = {"standard": standard, "dark": dark, "academic": academic}

__all__ = ["THEMES", "standard", "dark", "academic"]
