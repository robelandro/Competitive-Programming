#!/usr/bin/env python3
import unittest
from leetcode.Sort_Colors import Solution

class TestSortColors(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sort_colors(self):
        self.assertEqual(self.solution.sortColors([2,0,2,1,1,0]), [0,0,1,1,2,2])
        self.assertEqual(self.solution.sortColors([2,0,1]), [0,1,2])
        self.assertEqual(self.solution.sortColors([0]), [0])
        self.assertEqual(self.solution.sortColors([1]), [1])
