import unittest
import sys
import os.path
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import sorting


class TestHashTable(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testsort(self):
        bsort = sorting.BubbleSort()
        qsort = sorting.QuickSort()
        isort = sorting.InsertionSort()
        ssort = sorting.SelectionSort()
        bsort.array = [5, 9, 3, 7, 2, 7, 2, 1, 5]
        qsort.array = [5, 9, 3, 7, 2, 7, 2, 1, 5]
        isort.array = [5, 9, 3, 7, 2, 7, 2, 1, 5]
        ssort.array = [5, 9, 3, 7, 2, 7, 2, 1, 5]
        self.assertEqual(bsort.array, [1, 2, 2, 3, 5, 5, 7, 7, 9])
        self.assertEqual(qsort.array, [1, 2, 2, 3, 5, 5, 7, 7, 9])
        self.assertEqual(isort.array, [1, 2, 2, 3, 5, 5, 7, 7, 9])
        self.assertEqual(ssort.array, [1, 2, 2, 3, 5, 5, 7, 7, 9])

        array = []
        while len(array) <= random.randint(10000, 100000):
            array.append(random.randint(0, 100000))
        print("Len:", len(array))
        bsort = sorting.BubbleSort()
        qsort = sorting.QuickSort()
        isort = sorting.InsertionSort()
        ssort = sorting.SelectionSort()
        bsort.array = array
        qsort.array = array
        isort.array = array
        ssort.array = array
        self.assertEqual(bsort.array, sorted(array))
        self.assertEqual(qsort.array, sorted(array))
        self.assertEqual(isort.array, sorted(array))
        self.assertEqual(ssort.array, sorted(array))


if __name__ == '__main__':
    unittest.main()
