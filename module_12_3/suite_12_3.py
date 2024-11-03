import unittest as ut
import test_turnament as turn
import test_runner as rann

test_suite = ut.TestSuite()
test_suite.addTest(ut.TestLoader().loadTestsFromTestCase(turn.TournamentTest))
test_suite.addTest(ut.TestLoader().loadTestsFromTestCase(rann.RunnerTest))

runner = ut.TextTestRunner(verbosity=2)
runner.run(test_suite)
