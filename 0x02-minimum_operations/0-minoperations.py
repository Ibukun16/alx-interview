#!/usr/bin/python3
"""
A text file contains a single character H but the text editor
can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file.
"""
import math


def minOperations(n):
    """
    Calculates the fewest numbermof operations needed
    to result in exactly n H characters in the file.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Start from n and find its factors
    for c in range(3, int(math.sqrt(n)) + 1, 2):
        while n % c == 0:
            factors.append(c)
            n //= c
    if n > 2:
        factors.append(n)
    numOps = sum(factors)
    return int(numOps)
