import unittest 
from ../Fizz-Buzz import Solution

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
		self.solution = Solution()

	def test_fizz_buzz(self):
		self.assertEqual(self.solution.fizzBuzz(15), [
			"1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"
		])
