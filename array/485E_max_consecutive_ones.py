"""
Given a binary array, find the maximum number of consecutive 1s in this array.
https://leetcode.com/problems/max-consecutive-ones/
Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000v
"""

import unittest

def findmaxconsecutiveones(nums):
    """
    input: nums: List[int]
    return: int
    Time Complexity: O(n)
    Space: O(1)
    """
    if not nums: return None
    maxlen = 0
    temp = 0
    for each in nums:
        if each == 1:
            temp += 1
            maxlen = max(maxlen, temp)
        else:
            temp = 0

    return maxlen


def findmaxconsecutiveones_string(nums):
    """
    Time: O(n)
    space: O(n)
    """
    return max(map(len, "".join(map(str, nums)).split('0')))

class TestCase(unittest.TestCase):
    def do(self, f):
        self.assertEqual(f([1,1,0,1,1,1]), 3)
        self.assertEqual(f([1]), 1)
        self.assertEqual(f([0]), 0)
        self.assertEqual(f([0, 0, 0, 1, 1, 1, 1, 0, 1]), 4)
    
    def test1(self):
        self.do(findmaxconsecutiveones)
    
    def test2(self):
        self.do(findmaxconsecutiveones_string)

if __name__ == "__main__":
    unittest.main()
