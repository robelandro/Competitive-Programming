#!/usr/bin/env python3
import unittest
from hackerrank.Insertion_Sort1 import *


class TestInsertionSort1(unittest.TestCase):
    def setUp(self):
        """
        This is a setUp function that initializes an instance variable insertionSort1.
        """
        self.insertionSort1 = insertionSort1
    
    def testinsertionSort1(self):
        """
        The function tests the insertion sort algorithm on two different input arrays and checks if the
        output is correct.
        """
        self.assertEqual(self.insertionSort1(5, [2, 4, 6, 8, 3]), [2, 3, 4, 6, 8])
        self.assertEqual(self.insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
