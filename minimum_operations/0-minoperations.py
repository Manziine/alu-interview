#!/usr/bin/python3
"""
Minimum Operations Module

This module contains a function to calculate the minimum number of operations
needed to result in exactly n H characters in a text file using only
Copy All and Paste operations.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n H
    characters.

    Args:
        n (int): The target number of H characters

    Returns:
        int: The minimum number of operations needed, or 0 if n is impossible
        to achieve
    """
    if n <= 1:
        return 0

    # If n is impossible to achieve (not a positive integer), return 0
    if not isinstance(n, int) or n < 1:
        return 0

    # Use optimized approach for large numbers
    # For large n, we use a more memory-efficient method
    if n > 1000000:
        return _minOperationsLarge(n)

    # Use dynamic programming approach for smaller numbers
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # We start with 1 H character

    for i in range(2, n + 1):
        # Try all possible divisors of i
        for j in range(1, i):
            if i % j == 0:
                # If we can get j H characters, we can copy all and paste
                # (i/j - 1) times
                # Total operations = operations to get j + 1 (copy) +
                # (i/j - 1) (paste)
                operations = dp[j] + 1 + (i // j - 1)
                dp[i] = min(dp[i], operations)

    return dp[n] if dp[n] != float('inf') else 0


def _minOperationsLarge(n):
    """
    Optimized function for large numbers using factorization approach.
    """
    if n == 1:
        return 0

    # Find the prime factorization of n
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)

    # If n was 1, return 0
    if not factors:
        return 0

    # The minimum operations is the sum of all prime factors
    return sum(factors)
