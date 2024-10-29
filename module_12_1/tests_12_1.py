import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        rn1 = runner.Runner('xxx')
        for _ in range(10):
            rn1.walk()
        self.assertEqual(rn1.distance, 50)

    def test_run(self):
        rn2 = runner.Runner('xxx')
        for _ in range(10):
            rn2.run()
        self.assertEqual(rn2.distance, 100)

    def test_challenge(self):
        rn1 = runner.Runner('xxx')
        rn2 = runner.Runner('yyy')
        for _ in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)

if __name__ == '__main__':
    unittest.main()