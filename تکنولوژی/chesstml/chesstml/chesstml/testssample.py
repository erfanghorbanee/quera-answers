import unittest
from bs4 import BeautifulSoup
from solution import process


class Test(unittest.TestCase):
	def test_1(self):
		self.assertEqual(process("htmlsampletest1.html"), 1)

	def test_2(self):
		self.assertEqual(process("htmlsampletest2.html"), 4)
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																									
