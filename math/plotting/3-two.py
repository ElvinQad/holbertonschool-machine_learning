#!/usr/bin/env python3
"""
This module provides a function to plot the exponential
decay of radioactive elements.
"""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """
    Plots the exponential decay of Carbon-14 (C-14) and Radium-226 (Ra-226)
    over time.

    The plot displays the fraction of each element remaining as
    a function of time,
    illustrating their respective decay rates.
    """
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(x, y1, 'r--', label='C-14')
    plt.plot(x, y2, 'g-', label='Ra-226')
    plt.legend(loc='upper right')
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of Radioactive Elements')
    plt.axis([0, 20_000, 0, 1])
    plt.show()
