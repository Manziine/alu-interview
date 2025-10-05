#!/usr/bin/python3
"""
Additional test cases for rain function
"""
rain = __import__('0-rain').rain

if __name__ == "__main__":
    # Test case 1: Original test cases
    print("Test 1:", rain([0, 1, 0, 2, 0, 3, 0, 4]))  # Expected: 6
    print("Test 2:", rain([2, 0, 0, 4, 0, 0, 1, 0]))  # Expected: 6
    
    # Test case 3: Empty list
    print("Test 3:", rain([]))  # Expected: 0
    
    # Test case 4: Single element
    print("Test 4:", rain([5]))  # Expected: 0
    
    # Test case 5: Two elements
    print("Test 5:", rain([3, 2]))  # Expected: 0
    
    # Test case 6: All same height
    print("Test 6:", rain([3, 3, 3, 3]))  # Expected: 0
    
    # Test case 7: Descending order
    print("Test 7:", rain([5, 4, 3, 2, 1]))  # Expected: 0
    
    # Test case 8: Ascending order
    print("Test 8:", rain([1, 2, 3, 4, 5]))  # Expected: 0
    
    # Test case 9: Valley in the middle
    print("Test 9:", rain([3, 0, 2, 0, 4]))  # Expected: 7
    
    # Test case 10: Multiple valleys
    print("Test 10:", rain([3, 0, 0, 2, 0, 4]))  # Expected: 10
