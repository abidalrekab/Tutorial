import cal_modu
import unittest


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = cal_modu.add(123.24,34)
        self.assertEqual(result,157.24,"Addition")

    def test_subtract(self):
        result = cal_modu.subtract(123,100)
        self.assertEqual(result,23, "Subtraction")

    def test_multiplication(self):
        result = cal_modu.multiplication(12,10)
        self.assertEqual(result,120,"multiplication")

    def test_division(self):
        result = cal_modu.division(120,6)
        self.assertEqual(result,20,"Division")




if __name__ == '__main()__' :
    unittest.TestCase

