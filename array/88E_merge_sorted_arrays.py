"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
https://leetcode.com/problems/merge-sorted-array/
Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


import unittest


def merge_sort1(nums1, m, nums2, n):
    """
    Time: O((m+n)log(m+n))
    Space: o(m)
    """
    nums1[:] = sorted(nums1[:n] + nums2)
    return nums1

def merge_sort2(nums1, m, nums2, n):
    """
    Intutation: Two pointers strat from end
    Time: O(m + n)
    Space: O(1)
    """
    p1, p2, p = m -1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1
    nums1[:p2 + 1] = nums2[:p2+1]
    return nums1

class TestCase(unittest.TestCase):
    def do(self, f):
        self.assertEqual(f([1,2,3,0,0,0],3, [2,5,6], 3), [1,2,2,3,5,6])

    
    def test1(self):
        self.do(merge_sort1)
    
    def test2(self):
        self.do(merge_sort2)

if __name__ == "__main__":
    unittest.main()
