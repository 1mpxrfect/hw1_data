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

    def test_edge_case_noon_midnight(self):
        self.assertEqual(time_difference(12, 0), 12)
        self.assertEqual(time_difference(0, 12), 12)

    def test_wraparound(self):
        self.assertEqual(time_difference(6, 30), 6)
        self.assertEqual(time_difference(30, 6), 6)

    def test_large_time_difference(self):
        self.assertEqual(time_difference(4, 18), 10)
        self.assertEqual(time_difference(18, 4), 10)

    def test_exactly_halfway(self):
        self.assertEqual(time_difference(0, 12), 12)
        self.assertEqual(time_difference(12, 0), 12)

    def test_time_just_before_midnight(self):
        self.assertEqual(time_difference(23, 0), 1)
        self.assertEqual(time_difference(0, 23), 1)

    def test_cyclic_case_larger_than_24(self):
        self.assertEqual(time_difference(25, 7), 6)
        self.assertEqual(time_difference(7, 25), 6)

    def test_case_around_6AM(self):
        self.assertEqual(time_difference(6, 5), 1)
        self.assertEqual(time_difference(5, 6), 1)

    def test_case_around_6PM(self):
        self.assertEqual(time_difference(18, 19), 1)
        self.assertEqual(time_difference(19, 18), 1)

    def test_crossing_from_23_to_1(self):
        self.assertEqual(time_difference(23, 1), 2)
        self.assertEqual(time_difference(1, 23), 2)

    def test_case_before_and_after_3AM(self):
        self.assertEqual(time_difference(2, 3), 1)
        self.assertEqual(time_difference(3, 2), 1)
        self.assertEqual(time_difference(0, 3), 3)
        self.assertEqual(time_difference(3, 0), 3)

    def test_time_difference_equal_to_0AM(self):
        self.assertEqual(time_difference(0, 23), 1)
        self.assertEqual(time_difference(23, 0), 1)

if __name__ == '__main__':
    unittest.main()
