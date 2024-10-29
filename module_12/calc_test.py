import calc
import unittest

class CalcTest(unittest.TestCase):

    def test_add(self):

        self.assertEqual(calc.add(1, 2), 3)

    def test_sub(self):
        self.assertEqual(calc.sub(7,4), 3)

    def test_mul(self):
        self.assertEqual(calc.mul(5,5), 25)

    def test_div(self):
        self.assertEqual(calc.div(21, 7), 3)
        self.assertEqual(calc.div(3, 0), 'На ноль делить нельзя')

if __name__ == '__main__':
    unittest.main()
