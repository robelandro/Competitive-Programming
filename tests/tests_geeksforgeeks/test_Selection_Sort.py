#!/usr/bin/env python3
import unittest
from geeksforgeeks.Selection_Sort import Solution


class TestSelectionSort(unittest.TestCase):
    
	def setUp(self):

		self.selectionsort = Solution()

	def test_selectionSort(self):
		test_arr =[2, 8, 5, 3, 9, 4, 1]
		self.assertEqual(self.selectionsort.selectionSort(arr=test_arr, n=7), [1, 2, 3, 4, 5, 8, 9])
