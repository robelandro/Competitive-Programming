#!/usr/bin/env python3
import unittest
from leetcode.rearrangeArray import Solution

class TestRearrangeArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rearrangeArray(self):
        self.assertEqual(self.solution.rearrangeArray([1,2,3,4,5,6]), [4, 1, 5, 2, 6, 3])
