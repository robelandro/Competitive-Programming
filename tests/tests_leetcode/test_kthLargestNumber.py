#!/usr/bin/env python3
import unittest
from leetcode.kthLargestNumber import Solution

class TestKthLargestNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kth_largest_number(self):
        self.assertEqual(self.solution.kthLargestNumber(["2","21","12","1"], 3), "2")
        self.assertEqual(self.solution.kthLargestNumber(["0","0"], 2), "0")
        self.assertEqual(self.solution.kthLargestNumber(["1"], 1), "1")
        self.assertEqual(self.solution.kthLargestNumber(["3","6","7","10"], 4), "3")
        self.assertEqual(self.solution.kthLargestNumber(["2","21","12","1"], 3), "2")
        self.assertEqual(self.solution.kthLargestNumber(["0","0"], 2), "0")
        self.assertEqual(self.solution.kthLargestNumber(["1"], 1), "1")
        self.assertEqual(self.solution.kthLargestNumber(["3","6","7","10"], 4), "3")
        self.assertEqual(self.solution.kthLargestNumber(["2","21","12","1"], 3), "2")
        self.assertEqual(self.solution.kthLargestNumber(["0","0"], 2), "0")
        self.assertEqual(self.solution.kthLargestNumber(["1"], 1), "1")
        self.assertEqual(self.solution.kthLargestNumber(["3","6","7","10"], 4), "3")
        self.assertEqual(self.solution.kthLargestNumber(["2","21","12","1"], 3), "2")
        self.assertEqual(self.solution.kthLargestNumber(["0","0"], 2), "0")
        self.assertEqual(self.solution.kthLargestNumber(["1"], 1), "1")
        self.assertEqual(self.solution.kthLargestNumber(["3","6","7","10"], 4), "3")
        self.assertEqual(self.solution.kthLargestNumber(["2","21","12","1"], 3), "2")
        self.assertEqual(self.solution.kthLargestNumber(["0","0"], 2), "0")
        self.assertEqual(self.solution.kthLargestNumber(["1"], 1), "1")
        self.assertEqual(self.solution.kthLargestNumber(["3","6","7","10"], 4), "3")
        self.assertEqual(self.solution.kthLargestNumber(["2","21","12","1"], 3), "2")
        self.assertEqual(self.solution.kthLargestNumber(["0","0"], 2), "0")
