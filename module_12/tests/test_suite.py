import unittest
import calc_test
import test_new_calc

calcST = unittest.TestSuite()
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(calc_test.CalcTest))
calcST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(calcST)