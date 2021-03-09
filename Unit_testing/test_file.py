import unittest
import file_under_test

class TestUpper(unittest.TestCase):
	def test_one_word(self):
		text = 'Hello!'
		result = file_under_test.upper_text(text)
		self.assertEqual(result,'HELLO!')

class TestUpper1(unittest.TestCase):
	def test_one_word(self):
		text = 'Hello!'
		result = file_under_test.upper_text(text)
		self.assertNotEqual(result,'HELLO!')

if __name__=='__main__':
	unittest.main()