#!/usr/bin/env python3
"""Domino piling"""
import unittest
from codeforces.A_Domino_piling import *

class TestDominoPiling(unittest.TestCase):

    def setUp(self):
        self.dominoPiling = domino_pilling

    def test_domino_pilling(self):
        self.assertEqual(domino_pilling(2, 4), 4)
        self.assertEqual(domino_pilling(3, 3), 4)
        self.assertEqual(domino_pilling(3, 1), 1)
        self.assertEqual(domino_pilling(1, 5), 2)
