import unittest
from unittest import mock
import string_calculator as calc

class StringCalculatorTestCase(unittest.TestCase):
	
	def test_add_empty(self):
		obj = calc.StringCalculator()
		input_string = ""
		check_str = 0
		self.assertEqual(obj.add(input_string), check_str)

	def test_add_self(self):
		obj = calc.StringCalculator()
		input_string = "2"
		check_str = 2
		self.assertEqual(obj.add(input_string), check_str)

	def test_add_comma(self):
		obj = calc.StringCalculator()
		input_string = "2,3"
		check_str = 5
		self.assertEqual(obj.add(input_string), check_str)

	def test_add_new_line(self):
		obj = calc.StringCalculator()
		input_string = "2\n3"
		check_str = 5
		self.assertEqual(obj.add(input_string), check_str)	

	def test_add_new_line_and_comma(self):
		obj = calc.StringCalculator()
		input_string = "1\n2,3\n4"
		check_str = 10
		self.assertEqual(obj.add(input_string), check_str)

	def test_add_below_zero(self):
		obj = calc.StringCalculator()
		input_string = "-1,2,-3"
		check_str = "отрицательные числа запрещены: -1,-3"
		self.assertEqual(obj.add(input_string), check_str)		

	def test_add_bigger_thousand(self):
		obj = calc.StringCalculator()
		input_string = "200, 1000, 2000, 100"
		check_str = 300
		self.assertEqual(obj.add(input_string), check_str)					

	def test_single_diviator(self):
		obj = calc.StringCalculator()
		input_string = "//#\n1#2"
		check_str = 3
		self.assertEqual(obj.add(input_string), check_str)

	def test_multiple_diviator(self):
		obj = calc.StringCalculator()
		input_string = "//####\n1####2"
		check_str = 3
		self.assertEqual(obj.add(input_string), check_str)					

if __name__ == '__main__':
    unittest.main()
