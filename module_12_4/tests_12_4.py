import rt_with_exceptions as rt
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format="%(asctime)s | %(levelname)s | %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            rn1 = rt.Runner('xxx', speed=-2)
            for _ in range(10):
                rn1.walk()
            self.assertEqual(rn1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            rn2 = rt.Runner(['xxx'])
            for _ in range(10):
                rn2.run()
            self.assertEqual(rn2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        rn1 = rt.Runner('xxx')
        rn2 = rt.Runner('yyy')
        for _ in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)


if __name__ == '__main__':
    unittest.main()
