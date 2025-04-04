#!/usr/bin/env python3
"""
This module provides a function to plot a simple line graph.
"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots a simple line graph of y = x^3 from x = 0 to 10.
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, 'r-')
    plt.xlim(0, 10)
    plt.show()
