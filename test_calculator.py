import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(100, 200), 300)  
        self.assertEqual(self.calc.add(-100, 50), -50)

    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(40, 20), 20)
        self.assertEqual(self.calc.subtract(20, 40), -20)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(7, 1), 7)

    def test_divide(self):
        self.assertEqual(self.calc.divide(80, 4), 20)
        self.assertEqual(self.calc.divide(90, 2), 45)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(100, 30), 10)
        self.assertEqual(self.calc.modulo(100, 20), 0)

if __name__ == '__main__':
    unittest.main()