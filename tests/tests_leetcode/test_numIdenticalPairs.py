#!/usr/bin/env python3
import unittest
from leetcode.numIdenticalPairs import Solution


class TestNumIdenticalPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numIdenticalPairs(self):
        self.assertEqual(self.solution.numIdenticalPairs([1,2,3,1,1,3]), 4)
        self.assertEqual(self.solution.numIdenticalPairs([1,1,1,1]), 6)
        self.assertEqual(self.solution.numIdenticalPairs([1,2,3]), 0)
