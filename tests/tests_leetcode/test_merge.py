#!/usr/bin/env python3
import unittest
from leetcode.merge import Solution

class TestMerge(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge(self):
        self.assertEqual(self.solution.merge([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(self.solution.merge([[1,4],[4,5]]), [[1,5]])
