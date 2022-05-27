from simple_calc import simple_calc
from unittest import TestCase


class calc_test(TestCase):
    calc = simple_calc()

    def test_add(self):
        actual = self.calc.add(2, 4)
        expected = 6
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calc.subtract(10, 6)
        expected = 4
        self.assertEqual(actual, expected)

    def test_multiply(self):
        actual = self.calc.multiply(10, 6)
        expected = 60
        self.assertEqual(actual, expected)
        pass

    def test_division(self):
        actual = self.calc.division(10, 2)
        expected = 5
        self.assertEqual(actual, expected)
        pass
