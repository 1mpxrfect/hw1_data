import unittest
from Task3.utils import time_difference


class TestTimeDifference(unittest.TestCase):

    def test_same_time(self):
        self.assertEqual(time_difference(7, 7), 0)

    def test_midnight_crossing(self):
        self.assertEqual(time_difference(22, 2), 4)
        self.assertEqual(time_difference(2, 22), 4)

    def test_within_same_day(self):
        self.assertEqual(time_difference(8, 13), 5)
        self.assertEqual(time_difference(13, 8), 5)

    def test_half_day_difference(self):
        self.assertEqual(time_difference(3, 15), 12)
        self.assertEqual(time_difference(9, 21), 12)

    def test_almost_full_day(self):
        self.assertEqual(time_difference(1, 23), 2)
        self.assertEqual(time_difference(23, 1), 2)


if __name__ == '__main__':
    unittest.main()
