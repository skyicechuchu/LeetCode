"""
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, 
also in sorted non-decreasing order.
https://leetcode.com/problems/squares-of-a-sorted-array/
 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""


import unittest

def squares_sort(nums):
    """
    Time: O(nlog(n))
    Space: O(n)
    """
    return sorted(x * x for x in nums)


def sqaure_two_pointer_deque(nums):
    """
    Intuition: Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing order, then some non-negative elements with squares in increasing order.
    Time: O(n)
    Space: O(n)
    """
    from collections import deque
    res = deque()
    l, r = 0, len(nums) - 1
    while l <= r:
        left, right = abs(nums[l]), abs(nums[r])
        if left < right:
            res.appendleft(right * right)
            r -= 1
        else:
            res.appendleft(left * left)
            l += 1
    return list(res)


class TestCaset(unittest.TestCase):
    def do(self, f):
        self.assertEqual(f([-4,-1,0,3,10]), [0,1,9,16,100])
        self.assertEqual(f([-7,-3,2,3,11]), [4,9,9,49,121])
        self.assertEqual(f([0]), [0])

    def test1(self):
        self.do(squares_sort)
    
    def test2(self):
        self.do(sqaure_two_pointer_deque)


if __name__ == "__main__":
    unittest.main()
