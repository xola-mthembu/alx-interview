#!/usr/bin/python3
"""
This module contains the function that calculates the perimeter of an island
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of the island in a grid.
    
    Args:
        grid (list of list of int): 2D list representing the island.
    
    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Start by adding 4 for each land cell
                perimeter += 4
                # Check if there's land above, subtract 2 if true
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                # Check if there's land to the left, subtract 2 if true
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
