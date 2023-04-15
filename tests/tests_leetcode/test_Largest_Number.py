#!/usr/bin/env python3
import unittest
from leetcode.Largest_Number import Solution

class TestLargestNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largest_number(self):
        self.assertEqual(self.solution.largestNumber([10,2]), "210")
        self.assertEqual(self.solution.largestNumber([3,30,34,5,9]), "9534330")
        self.assertEqual(self.solution.largestNumber([10,29,2,3,4,5,6,7,8,9]), "987654329210")
        self.assertEqual(self.solution.largestNumber([2,20,200]), "220200") 
        self.assertEqual(self.solution.largestNumber([200,3,30,34,5,9,19,18]), "95343302001918")
        self.assertEqual(self.solution.largestNumber([3,90,40,200,94,86]), "949086403200")
        self.assertEqual(self.solution.largestNumber([12, 10, 29, 20, 2, 200, 300, 30]), "30300292202001210")
