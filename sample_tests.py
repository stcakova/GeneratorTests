import unittest
import itertools
import solution


class TestGenerators(unittest.TestCase):

    def test_cycle_count(self):
        mirror_count = solution.alternate(lambda: itertools.count(1, 10),
                                          lambda: itertools.cycle('ABC'))
        sequence = [next(mirror_count) for i in range(20)]
        self.assertEqual(
            sequence,
            [1, 'A', 11, 'B', 21, 'C', 31, 'A', 41, 'B',
             51, 'C', 61, 'A', 71, 'B', 81, 'C', 91, 'A'])

    def test_cycle_repeat_count(self):
        mirror_count = solution.alternate(lambda: itertools.count(2, -10),
                                          lambda: itertools.repeat('KOK'),
                                          lambda:  itertools.cycle("ABCD"))

        sequence = [next(mirror_count) for i in range(30)]
        self.assertEqual(
            sequence,
            [2, 'KOK', 'A', -8, 'KOK', 'B', -18, 'KOK', 'C',  -28,
             'KOK', 'D', -38, 'KOK', 'A', -48, 'KOK', 'B', -58, 'KOK',
             'C', -68, 'KOK', 'D', -78, 'KOK', 'A', -88, 'KOK', 'B'])

    def test_repeat_cycle(self):
        mirror_count = solution.alternate(lambda: itertools.repeat('ABC'),
                                          lambda: itertools.cycle('WXYZ'))
        sequence = [next(mirror_count) for i in range(20)]
        self.assertEqual(
            sequence,
            ['ABC', 'W', 'ABC', 'X', 'ABC', 'Y', 'ABC', 'Z', 'ABC', 'W',
             'ABC', 'X', 'ABC', 'Y', 'ABC', 'Z', 'ABC', 'W', 'ABC', 'X'])

    def test_double_count(self):
        mirror_count = solution.alternate(lambda: itertools.count(1, 1),
                                          lambda: itertools.count(-1, -1))
        sequence = [next(mirror_count) for i in range(20)]
        self.assertEqual(
            sequence,
            [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8,
             -8, 9, -9, 10, -10])


if __name__ == '__main__':
    unittest.main()
