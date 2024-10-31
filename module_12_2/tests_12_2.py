import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):
    N_TST = 0

    @classmethod
    def setUpClass(cls):
        cls.all_result = {}

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_result.items():
            x = [v[x].name for x in v.keys()]
            x.insert(-1, ' и ')
            if len(x) > 3:
                x.insert(1, ', ')
            print(f'{k}.', ''.join(x))

    def setUp(self):
        self.r_1 = rt.Runner('Усэйн', 10)
        self.r_2 = rt.Runner('Андрей', 9)
        self.r_3 = rt.Runner('Ник', 3)
        self.dist = 90
        self.result = {}
        TournamentTest.N_TST += 1

    def test_start_1(self):
        turn = rt.Tournament(self.dist, self.r_1, self.r_3)
        self.result = turn.start()
        last_run = max(self.result.keys())
        self.assertTrue(self.result[last_run] == 'Ник')
        self.all_result[self.N_TST] = self.result

    def test_start_2(self):
        turn = rt.Tournament(self.dist, self.r_2, self.r_3)
        self.result = turn.start()
        last_run = max(self.result.keys())
        self.assertTrue(self.result[last_run] == 'Ник')
        self.all_result[self.N_TST] = self.result

    def test_start_3(self):
        turn = rt.Tournament(self.dist, self.r_1, self.r_2, self.r_3)
        self.result = turn.start()
        last_run = max(self.result.keys())
        self.assertTrue(self.result[last_run] == 'Ник')
        self.all_result[self.N_TST] = self.result

    def test_start_4(self):
        self.dist = 1
        turn = rt.Tournament(self.dist, self.r_3, self.r_1, self.r_2)
        self.result = turn.start()
        test = sorted([x for x in self.result.values()], key=lambda x: x.speed, reverse=True)
        test = dict(zip(range(1, len(self.result)+1), test))
        self.assertEqual(test, self.result)
        self.all_result[self.N_TST] = self.result

if __name__ == '__main__':
    unittest.main()
