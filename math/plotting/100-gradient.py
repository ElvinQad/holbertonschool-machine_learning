#!/usr/bin/env python3
""" plot mountain elevation as a scatter plot with colorbar """
import numpy as np
import matplotlib.pyplot as plt

def gradient():

    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))

    plt.xlabel("x coordinate (m)")
    plt.ylabel("y coordinate (m)")
    plt.title("Mountain Elevation")

    scatter = plt.scatter(x, y, c=z, cmap='viridis')
    cbar = plt.colorbar(scatter)
    cbar.set_label('elevation (m)')

    plt.show()