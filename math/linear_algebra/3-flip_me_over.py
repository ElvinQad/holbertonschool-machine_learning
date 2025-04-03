#!/usr/bin/env python3
"""
This module contains a function to transpose a 2D matrix.

The `matrix_transpose` function takes a 2D matrix as input and returns its transpose.
"""

def matrix_transpose(matrix):
    """Transposes a 2D matrix."""
    transposed = [
        [row[n] for row in matrix]
        for n in range(len(matrix[0]))
    ]

    return transposed