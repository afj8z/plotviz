"""
Internal 'Header' File.
"""

# External Libraries
import os
import matplotlib.pyplot as plt
from cycler import cycler
from typing import Optional  # Added for logic checks
from scipy.stats import norm
from numpy import arange, linspace


# Internal Constants & Types
from .palettes import DEFAULT_COLORS
from .types import CoordPair, Number, PlotContext, GridContext, DataContext
