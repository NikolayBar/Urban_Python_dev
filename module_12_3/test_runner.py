import runner_and_tournament as rt
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        rn1 = rt.Runner('xxx')
        for _ in range(10):
            rn1.walk()
        self.assertEqual(rn1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        rn2 = rt.Runner('xxx')
        for _ in range(10):
            rn2.run()
        self.assertEqual(rn2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rn1 = rt.Runner('xxx')
        rn2 =rt.Runner('yyy')
        for _ in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)

if __name__ == '__main__':
    unittest.main()