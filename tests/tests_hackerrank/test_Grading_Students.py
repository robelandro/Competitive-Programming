import unittest
from hackerrank.Grading_Students import *


class TestGradingStudents(unittest.TestCase):

    def setUp(self):
        self.gradingStudents = gradingStudents

    def test_grading_students(self):
        self.assertEqual(self.gradingStudents([73, 67, 38, 33]), [75, 67, 40, 33])
