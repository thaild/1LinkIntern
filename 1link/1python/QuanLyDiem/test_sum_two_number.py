from unittest import TestCase
from sum_util import sum_two_number

class TestSum_two_number(TestCase):
	def test_sum_two_number(self):
		self.assertEqual(6, sum_two_number(2, 4))

	def test_sum_two_number(self):
		self.assertEqual(7, sum_two_number(2, 4))