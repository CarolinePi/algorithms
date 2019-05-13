import time
from functools import wraps


class Interface(object):
    def sorting(self): raise NotImplementedError

    @staticmethod
    def timer(func):
        """Decorator for function which count time. """
        @wraps(func)
        def inner(self, *args, **kwargs):
            start_time = time.time()
            func(self)
            print("Time: %s" % (time.time() - start_time))
        return inner


class BubbleSort(Interface):
    def __init__(self):
        self.__array = []

    @Interface.timer
    def sorting(self):
        for i in range(len(self.__array) - 1):
            for j in range(i, len(self.__array)):
                if self.__array[i] > self.__array[j]:
                    self.__array[i], self.__array[j] = self.__array[j], self.__array[i]
        return self.__array

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, value):
        self.__array = value


class SelectionSort(Interface):
    def __init__(self):
        self.__array = []

    def minimum(self, i):
        """ Find minimum in array. """
        temp = self.__array[i]
        temp_index = i
        for iterator in range(i + 1, len(self.__array)):
            if self.__array[iterator] < temp:
                temp = self.__array[iterator]
                temp_index = iterator
        return temp_index

    @Interface.timer
    def sorting(self):
        for i in range(len(self.__array)):
            minim_index = self.minimum(i)
            self.__array[i], self.__array[minim_index] = self.__array[minim_index], self.__array[i]
        return self.__array

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, value):
        self.__array = value


class InsertionSort(Interface):
    def __init__(self):
        self.__array = []

    @Interface.timer
    def sorting(self):
        if len(self.__array) <= 1:
            return self.__array
        else:
            for i in range(len(self.__array)):
                temp = self.__array[i]
                k = i - 1
                while k >= 0 and temp < self.__array[k]:
                    self.__array[k+1], self.__array[k] = self.__array[k], self.__array[k+1]
                    k -= 1
        return self.__array

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, value):
        self.__array = value


class QuickSort(Interface):
    def __init__(self):
        self.__array = []
        self.__array = self.sorting(self.__array)
        self.start_time = 0

    def sorting(self, x):
        if len(x) <= 1:
            return x
        else:
            left = []
            right = []
            pivot = len(x) // 2
            i = 0
            j = len(x) - 1
            while i < pivot:
                if x[i] >= x[pivot]:
                    left.append(x[i])
                else:
                    right.append(x[i])
                i += 1

            while j > pivot:
                if x[j] >= x[pivot]:
                    left.insert(0, x[j])
                else:
                    right.insert(0, x[j])
                j -= 1
            return self.sorting(right) + [x[pivot]] + self.sorting(left)

    @property
    def array(self):
        return self.__array

    @array.setter
    def array(self, value):
        self.__array = value
        self.start_time = time.time()
        self.__array = self.sorting(self.__array)
        print("Time: %s" % (time.time() - self.start_time))


if __name__ == "__main__":
    # Run unit tests
    import unittest
    suite = unittest.defaultTestLoader.discover('./unit-test', pattern='sorting_test.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)
