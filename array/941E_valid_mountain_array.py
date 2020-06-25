"""
Given an array A of integers, return true if and only
 if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
"""


import unittest


def valid_moutain(A):
    i, j, n = 0, len(A) - 1, len(A)
    while i + 1 < n and A[i] < A[i + 1]: i += 1
    while j > 0 and A[j - 1] > A[j]: j -= 1
    return 0 < i == j < n - 1


class TestCase(unittest.TestCase):

    def do(self, f):
        self.assertEqual(f([2, 1]), False)
        self.assertFalse(f([3, 5, 5]))
        self.assertFalse(f([0, 2, 3, 3 ,5, 1]))

    def testcase(self):
        self.do(valid_moutain)

if __name__ == "__main__":
    unittest.main()