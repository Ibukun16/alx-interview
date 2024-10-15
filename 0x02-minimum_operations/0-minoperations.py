#!/usr/bin/python3
"""
A text file contains a single character H but the text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Calculates the fewest numbermof operations needed
    to result in exactly n H characters in the file.
    """
    if not isinstance(n, int) or n <= 1:
        return (0)

    operations = 0

    # Start from n and find its factors
    while n > 1:
        for factor in range(2, n + 1):
            if n % factor == 0:  # While fac is a factor of n
                operations += factor  # Count operations
                n //= factor  # Reduce n by the factor

    return operations
