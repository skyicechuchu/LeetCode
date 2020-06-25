"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""

import unittest


def remove_duplicates(arr):
    """
    Inutition: Two pointer
    Time: O(n)
    Space: O(l)
    """
    if not arr: return 0
    if len(arr) == 1: return 1
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1

class TestCase(unittest.TestCase):
    def do(self, f):
        self.assertEqual(f([0,0,1,1,1,2,2,3,3,4]), 5)
    
    def testcase(self):
        self.do(remove_duplicates)

if __name__ == "__main__":
    unittest.main()
