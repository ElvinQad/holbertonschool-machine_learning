#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def change_scale():
    """
    Plots exponential decay of C-14 with logarithmic y-axis scale
    """
    x = np.arange(0, 28651, 5730)
    r = np.log(0.5)
    t = 5730
    y = np.exp((r / t) * x)

    plt.plot(x, y, 'b-')  # Add explicit blue line style
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of C-14')
    plt.yscale('log')
    plt.axis([0, 28650, 0.001, 1])
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
