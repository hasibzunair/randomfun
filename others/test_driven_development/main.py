import unittest
from calc import Calculator

class CalculatorTest(unittest.TestCase):
	# init class
	calculator = Calculator()
	# test adder
	def test_add(self):
		self.assertEqual(4, self.calculator.add(2,2))
		self.assertEqual(3.2, self.calculator.add(1,2.2))
	# test subtracter
	def test_minus(self):
	        self.assertEqual(2, self.calculator.minus(3,1))
        	self.assertEqual(-2, self.calculator.minus(1,3))
	# test mult
	def test_multiple(self):
        	self.assertEqual(12, self.calculator.multiple(3,4))
        	self.assertEqual(13.5, self.calculator.multiple(3,4.5))
	# test div
	def test_divide(self):
        	self.assertEqual(3, self.calculator.divide(9,3))



if __name__ == "__main__":
	unittest.main()


