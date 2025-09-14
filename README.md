# Minimum Operations

## Project Overview
This project implements a solution to calculate the minimum number of operations needed to result in exactly n 'H' characters in a text file using only two operations: "Copy All" and "Paste".

## Problem Description
In a text file, there is a single character H. Your text editor can execute only two operations in this file:
- **Copy All**: Copy all characters currently in the file
- **Paste**: Paste the characters from the clipboard

Given a number n, the task is to calculate the fewest number of operations needed to result in exactly n H characters in the file.

## Algorithm
The solution uses a dynamic programming approach:
1. For each target number i from 2 to n, we try all possible divisors j of i
2. If we can achieve j H characters, we can copy all and paste (i/j - 1) times to get i H characters
3. The total operations = operations to get j + 1 (copy) + (i/j - 1) (paste)
4. We choose the minimum operations among all possible divisors

## Files Structure
```
minimum_operations/
├── 0-minoperations.py    # Main implementation file
├── 0-main.py            # Test file with examples
└── test_9.py            # Additional test for n=9 case
```

## Usage

### Running the main test
```bash
cd minimum_operations
python 0-main.py
```

### Expected Output
```
Min # of operations to reach 4 char: 4
Min # of operations to reach 12 char: 7
```

### Testing with n=9
```bash
python test_9.py
```

Expected output:
```
Min # of operations to reach 9 char: 6
```

## Example Walkthrough (n=9)
Starting with 1 H character:
1. H → Copy All → Paste → HH (2 operations)
2. HH → Paste → HHH (1 operation)
3. HHH → Copy All → Paste → HHHHHH (2 operations)
4. HHHHHH → Paste → HHHHHHHHH (1 operation)

Total operations: 6

## Function Signature
```python
def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H characters.
    
    Args:
        n (int): The target number of H characters
        
    Returns:
        int: The minimum number of operations needed, or 0 if n is impossible to achieve
    """
```

## Requirements
- Python 3.4.3+
- All files are executable
- Code follows PEP 8 style guidelines
- All files end with a newline
- First line of all files is exactly `#!/usr/bin/python3`

## Author
Ineza Manzi Arnaud

## Project Information
- **Weight**: 1
- **Project Type**: Novice
- **Duration**: Sep 1, 2025 - Sep 14, 2025
- **Repository**: alu-interview
