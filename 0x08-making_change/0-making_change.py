#!/usr/bin/python3
"""Solution to interiew question on: Fewest no
of coins required to eet a given total amount
"""


def makeChange(coins, total):
    """fewest no of coins to meet total amt"""
    if total <= 0:
        return 0

    # sort coins in descending order of value

    coins.sort(reverse=True)
    change = 0
    for c in coins:
        div = total // c
        change += div
        total -= (div * c)
    if total != 0:
        return -1
    return change
