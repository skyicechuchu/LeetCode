"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""


import unittest

def sort_parity(nums):
    """
    Inutition: Two pointer
    Time: O(n)
    Space: O(1)
    """

    odd, even = 0, len(nums) - 1
    while odd < even:
        if nums[odd] % 2 > nums[even] % 2:
            nums[odd], nums[even] = nums[even], nums[odd]
        if nums[odd] % 2 == 0:
            odd += 1
        if nums[even] % 2 == 1:
            even -= 1
    return nums

def sort_parity_1(nums):
    """
    sort
    Time: O(nlog(n))
    Space: O(n)
    """
    nums.sort(key = lambda x: x % 2)
    return nums

class TestCase(unittest.TestCase):
    def do(self, f):
        self.assertIn(f([3,1,2,4]),[[4,2,3,1], [2,4,1,3], [4,2,1,3], [2, 4, 3, 1]])

    def testcase1(self):
        self.do(sort_parity)
    
    def testcase2(self):
        self.do(sort_parity_1)

if __name__ == "__main__":
    unittest.main()