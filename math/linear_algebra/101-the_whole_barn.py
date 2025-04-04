#!/usr/bin/env python3
"""Defines `add_matrices`."""


def add_matrices(mat1, mat2):
    """Adds two matrices."""
    if (type(mat1) is not list or type(mat2) is not list):
        return None
    if len(mat1) != len(mat2):
        return None
    new_matrix = []
    for i in range(len(mat1)):
        element = add_matrices(mat1[i], mat2[i])
        if element is None:
            return None
        new_matrix.append(element)
    if type(new_matrix[0]) is not list:
        return list(x + y for x, y in zip(mat1, mat2))
    return new_matrix
