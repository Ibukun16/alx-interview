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
    if not isinstance(n, int) or n < 2:
        return 0

    numOps = 0

    # Start from n and find its factors
    for c in range(2, n + 1):
        while n % c == 0:
            numOps += c
            n /= c
    return int(numOps)
