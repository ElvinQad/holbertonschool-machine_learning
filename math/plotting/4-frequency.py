#!/usr/bin/env python3
"""
Module to plot a histogram of student grades.
"""
import numpy as np
import matplotlib.pyplot as plt

def frequency():
    """Plots a histogram of student grades."""
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)

    # Define bins and plot histogram
    bins = range(0, 101, 10)
    plt.hist(student_grades, bins=bins, edgecolor='black')

    # Set labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Set x-axis ticks and limits
    plt.xticks(bins)
    plt.xlim(0, 100)

    # Display the plot
    plt.show()
