import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_1(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add_2(self):
        self.assertEqual(self.calc.add(4, 1), 5)

    def test_sub_1(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)
    def test_sub_2(self):
        self.assertEqual(self.calc.subtract(19, 10), 9)

    def test_mult_1(self):
        self.assertEqual(self.calc.multiply(8, 5), 40)
    def test_mult_2(self):
        self.assertEqual(self.calc.multiply(10, -1), -10)

    def test_divi_1(self):
        self.assertEqual(self.calc.divide(49, 7), 7)
    def test_divi_2(self):
        self.assertEqual(self.calc.divide(-4, 16), 4)
    def test_divi_2(self):
        self.assertEqual(self.calc.divide(108, 0), "Divisor is Zero")

    def test_mod_1(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)
    def test_mod_2(self):
        self.assertEqual(self.calc.modulo(8, 3), 2)
    def test_mod_3(self):
        self.assertEqual(self.calc.modulo(12, 3), 0)

if __name__ == '__main__':
    unittest.main()
