#!/usr/bin/env python3
import unittest
from hackerrank.Counting_Sort1Any import *


class TestCountingSort1(unittest.TestCase):
    def setUp(self):
        """
        This is a setUp function that initializes an instance variable countingSort1.
        """
        self.countingSort1 = countingSort

    def testcountingSort1(self):
        """
        The function tests the counting sort algorithm on two different input arrays and checks if the
        output is correct.
        """
        self.assertEqual(self.countingSort1([1, 1, 3, 2, 1]), [0, 3, 1, 1])
        self.assertEqual(self.countingSort1([4, 6, 5, 3, 3, 1]), [0, 1, 0, 2, 1, 1, 1])
