import sys
sys.path.append('../')

import pytest
import pandas as pd
from src.plot import plot_hist
import matplotlib.axes

def test_plot_hist_returns_axes():
    # Create sample DataFrame
    df = pd.DataFrame({'values': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]})

    # Call the function
    ax = plot_hist(df, 'values', [1, 5], 4 )

    # Assert the return type is matplotlib.axes.Axes
    assert isinstance(ax, matplotlib.axes.Axes)
