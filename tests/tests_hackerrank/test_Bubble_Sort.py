#!/usr/bin/env python3
import unittest
from hackerrank.Bubble_Sort import *


class TestBubble_Sort(unittest.TestCase):
    def setUp(self):
        self.bubbleSort = countSwaps

    def test_bubble_Sort(self):
        self.assertEqual(self.bubbleSort([6, 4, 1]), [1, 4, 6])
