#!/usr/bin/python3
"""Module that computes the the island perimeter
"""

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.

    Args:
        grid (_type_): _description_
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    lg = len(grid)
    for g, row in enumerate(grid):
        lr = len(row)
        for r, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                    g == 0 or (len(grid[g - 1]) > r and grid[g - 1][r] == 0),
                    r == lr - 1 or (lr > r + 1 and row[r + 1] == 0),
                    g == lg - 1 or (len(grid[g + 1]) > r and grid[g + 1][r] == 0),
                    r == 0 or row[r - 1] == 0,
                )
            perimeter += sum(edges)
    return perimeter