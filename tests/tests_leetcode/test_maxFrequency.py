#!/usr/bin/env python3
import unittest
from leetcode.maxFrequency import Solution

class TestMaxFrequency(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_frequency(self):
        self.assertEqual(self.solution.maxFrequency([1, 1, 1, 2, 2, 2, 3, 3, 3, 4], 6), 7)
        self.assertEqual(self.solution.maxFrequency([1, 4, 8, 13], 5), 2)
        self.assertEqual(self.solution.maxFrequency([3, 9, 6], 2), 1)
