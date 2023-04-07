#!/usr/bin/env python3
import unittest 
from leetcode.smallerNumbersThanCurrent import Solution

class TestsmallerNumbersThanCurrent(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_smallerNumbersThanCurrent(self):
        self.assertEqual(self.solution.smallerNumbersThanCurrent([6,5,4,8]), [2,1,0,3])
