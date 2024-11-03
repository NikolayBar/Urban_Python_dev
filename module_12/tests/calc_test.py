import unittest
import module_12.calc as calc

class CalcTest(unittest.TestCase):

    @unittest.skip("Временно пропущен")
    def test_add(self):

        self.assertEqual(calc.add(1, 2), 3)
    @unittest.skipIf(True, "skipIf <- True")
    def test_sub(self):
        self.assertEqual(calc.sub(7,4), 3)

    def test_mul(self):
        self.assertEqual(calc.mul(5,5), 25)
    @unittest.skipUnless(False, "skipUnless <- False")
    def test_div(self):
        self.assertEqual(calc.div(21, 7), 3)
        self.assertEqual(calc.div(3, 0), 'На ноль делить нельзя')

if __name__ == '__main__':
    unittest.main()
