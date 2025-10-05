#!/usr/bin/python3
"""
Module for calculating rainwater retention
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Args:
        walls: A list of non-negative integers representing wall heights

    Returns:
        Integer indicating total amount of rainwater retained

    The algorithm works by finding the maximum height to the left and right
    of each position, then calculating the water that can be trapped at that
    position as min(left_max, right_max) - current_height.
    """
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    total_water = 0

    # Arrays to store the maximum height to the left and right of each index
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate water trapped at each position
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        if water_level > walls[i]:
            total_water += water_level - walls[i]

    return total_water
