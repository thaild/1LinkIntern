from unittest import TestCase
from test_unittest import sum_two_number
class TestSum(TestCase):
	def test_sum(self):
		self.assertEqual(2, sum_two_number(2, 0))
