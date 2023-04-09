#!/usr/bin/env python3
import unittest
from leetcode.kClosest import Solution

class TestKClosest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_k_closest(self):
        self.assertEqual(self.solution.kClosest([[1,3],[-2,2]], 1), [[-2,2]])
        self.assertEqual(self.solution.kClosest([[3,3],[5,-1],[-2,4]], 2), [[3,3],[-2,4]])
