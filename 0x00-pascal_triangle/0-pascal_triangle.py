#!/usr/bin/python3
"""
 This module defines a function that generates pascal_triangle(n)
"""


def pascal_triangle(n):
    """
    Represent Pascal's triangle of size n.

    Return a list of integers contain in the
    generated triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
