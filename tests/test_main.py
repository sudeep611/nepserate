# Test Script
# If this test pass then everything should work fine

from nepserate import ScrapeRate
import unittest

class TestScrapeRate(unittest.TestCase):

	def test_result(self):
		ns = ScrapeRate()
		# Check if the return type is list
		self.assertEqual(type(ns.getRate("ADBL")), type([])) 


if __name__ == '__main__':
	unittest.main()