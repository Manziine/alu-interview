# Rain Water Retention

## Description
This project implements a solution to calculate how many square units of water will be retained after it rains, given a list of non-negative integers representing the heights of walls.

## Problem
Given a list of non-negative integers representing the heights of walls with unit width 1, as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

## Algorithm
The solution uses a dynamic programming approach:
1. For each position, calculate the maximum height to its left
2. For each position, calculate the maximum height to its right
3. The water trapped at each position is: `min(left_max, right_max) - current_height`
4. Sum up all the water trapped at each position

Time Complexity: O(n)
Space Complexity: O(n)

## Usage
```python
#!/usr/bin/python3
rain = __import__('0-rain').rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

walls = [2, 0, 0, 4, 0, 0, 1, 0]
print(rain(walls))  # Output: 6
```

## Files
- `0-rain.py`: Contains the `rain()` function implementation
- `0_main.py`: Test file with example cases
- `README.md`: This file

## Requirements
- Ubuntu 14.04 LTS
- Python 3.4.3
- PEP 8 style (version 1.7.x)
- No external modules allowed
