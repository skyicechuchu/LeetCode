"""
Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


import unittest


def move_zero(nums):
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    return nums


class TestCase(unittest.TestCase):
    def do(self, f):
        self.assertEqual(f([0,1,0,3,12]), [1,3,12,0,0])
        self.assertEqual(f([0, 0, 0, 0, 1]), [1, 0, 0, 0, 0])
        self.assertEqual(f([1, 2, 3, 4]), [1, 2, 3, 4])

    def testcase1(self):
        self.do(move_zero)


if __name__ == "__main__":
    unittest.main()