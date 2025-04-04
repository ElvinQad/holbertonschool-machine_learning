#!/usr/bin/env python3
"""
This module defines a function to concatenate two matrices along a specific axis.
"""


def cat_matrices(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1 (list of lists): The first matrix.
        mat2 (list of lists): The second matrix.
        axis (int, optional): The axis along which to concatenate. Defaults to 0.

    Returns:
        list of lists: A new matrix containing the concatenation of mat1 and mat2 along the specified axis,
                       or None if the matrices cannot be concatenated.
    """
    if not isinstance(mat1, list) or not isinstance(mat2, list):
        return None

    shape1 = get_shape(mat1)
    shape2 = get_shape(mat2)

    if shape1 is None or shape2 is None or len(shape1) != len(shape2):
        return None

    if axis < 0 or axis >= len(shape1):
        return None

    for i in range(len(shape1)):
        if i != axis and shape1[i] != shape2[i]:
            return None

    return cat_recursive(mat1, mat2, axis)


def get_shape(mat):
    """
    Recursively determines the shape of a matrix (list of lists).

    Args:
        mat (list or number): The matrix to determine the shape of.

    Returns:
        list: A list representing the shape of the matrix, or None if the matrix is not well-formed.
    """
    if not isinstance(mat, list):
        return []

    if not mat:
        return [0]  # Handle empty lists

    length = len(mat)
    element_shape = get_shape(mat[0])

    for element in mat:
        if get_shape(element) != element_shape:
            return None

    return [length] + element_shape


def cat_recursive(mat1, mat2, axis, current_axis=0):
    """
    Recursively concatenates two matrices along a specific axis.

    Args:
        mat1 (list of lists): The first matrix.
        mat2 (list of lists): The second matrix.
        axis (int): The axis along which to concatenate.
        current_axis (int, optional): The current axis being processed. Defaults to 0.

    Returns:
        list of lists: A new matrix containing the concatenation of mat1 and mat2 along the specified axis.
    """
    if current_axis == axis:
        return mat1 + mat2

    result = []
    for i in range(len(mat1)):
        result.append(cat_recursive(mat1[i], mat2[i], axis, current_axis + 1))
    return result
