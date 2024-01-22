import unittest
import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from quick_sort import my_quicksort_v1, my_quicksort_v2  # Updated import statements


class TestMyQuickSortV1(unittest.TestCase):  # Updated class name
    def test_empty_array(self):
        array = list()
        result = list()

        self.assertEqual(my_quicksort_v1(array), result)

    def test_single_element(self):
        array = [1]
        result = [1]

        self.assertEqual(my_quicksort_v1(array), result)

    def test_increasing_order(self):
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(my_quicksort_v1(array), result)

    def test_decreasing_order(self):
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(my_quicksort_v1(array), result)

    def test_random_order(self):
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(my_quicksort_v1(array), result)


class TestMyQuickSortV2(unittest.TestCase):  # Updated class name
    def test_empty_array(self):
        array = list()
        result = list()

        self.assertEqual(my_quicksort_v2(array), result)

    def test_single_element(self):
        array = [1]
        result = [1]

        self.assertEqual(my_quicksort_v2(array), result)

    def test_increasing_order(self):
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(my_quicksort_v2(array), result)

    def test_decreasing_order(self):
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(my_quicksort_v2(array), result)

    def test_random_order(self):
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]

        self.assertEqual(my_quicksort_v2(array), result)


if __name__ == "__main__":
    unittest.main()
