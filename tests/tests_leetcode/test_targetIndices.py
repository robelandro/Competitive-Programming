#!/usr/bin/env python3
import unittest 
from leetcode.targetIndices import Solution

class TesttargetIndices(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_targetIndices(self):
        self.assertEqual(self.solution.targetIndices([8,1,2,2,3], 8), [4])
