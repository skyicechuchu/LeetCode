"""
https://leetcode.com/problems/duplicate-zeros/
Given a fixed length array arr of integers, duplicate each occurrence of zero, 
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""

import unittest


def duplicate_zero(arr):
    """
    In place
    Time: O(N^2)
    Space: O(1) -> In-place
    """
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
        i += 1
    return arr

def duplicate_zero_2(arr):
    """
    Intuition: This algo goes barckwards and applies correct shifting distance
               to every element
    Time: O(n)
    Space: O(1)  -> In-place
    """
    n = len(arr)
    j = n + arr.count(0)
    for i in range(n - 1, -1, -1):
        j -= 1
        if j < n:
            arr[j] = arr[i]
        if arr[i] == 0:
            j -= 1
            if j < n:
                arr[j] = 0
    return arr
        



class TestCase(unittest.TestCase):
    def do(self, f):
        self.assertEqual(f([1,0,2,3,0,4,5,0]), [1,0,0,2,3,0,0,4])
        self.assertEqual(f([1,2,3]), [1, 2, 3])
        self.assertEqual(f([0, 0]), [0, 0])

    def test1(self):
        self.do(duplicate_zero)
    
    def test2(self):
        self.do(duplicate_zero_2)


if __name__ == "__main__":
    unittest.main()