"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

import unittest

def find_disapper(nums):
    """
    Hash Table
    Time: O(n)
    Space: O(n)
    """
    hash_table = {}
    for num in nums:
        hash_table[num] = 1
    res = []

    for num in range(1, len(nums) + 1):
        if num not in hash_table:
            res.append(num)
    
    return res


def find_disapper1(nums):
    """
    Negating the numbers
    Time: O(n)
    Space: O(1)
    """
    for i in range(len(nums)):
        new_index = abs(nums[i]) - 1
        if nums[new_index] > 0:
            nums[new_index] *= -1
    res = []
    for i in range(1, len(nums) + 1):
        if nums[i - 1] > 0:
            res.append(i)
    return res


class TestCase(unittest.TestCase):
    def do(self, f):
        self.assertEqual(f([4,3,2,7,8,2,3,1]), [5, 6])

    def testcase1(self):
        self.do(find_disapper)
    
    def testcase2(self):
        self.do(find_disapper1)


if __name__ == "__main__":
    unittest.main()