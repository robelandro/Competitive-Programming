#!/usr/bin/env python3
import unittest 
from leetcode.Sorting_the_Sentence import Solution

class TestSortingtheSentence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_Sorting_the_Sentence(self):
        self.assertEqual(self.solution.sortSentence("is2 sentence4 This1 a3"), "This is a sentence")
