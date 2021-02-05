from bucket_sort_1 import *
import numpy as np
import random
import unittest


class TestNotebook(unittest.TestCase):
    
    def test_sort_real_numbers(self):
        temp_list = list(map(lambda x: round(x, 10), np.random.uniform(low=0.5, high=100.005, size=(100000,))))
        test_list, test_list[:] = [], temp_list
        temp_list.sort(), bucket_sort(test_list)
        self.assertEqual(test_list, temp_list)

    def test_sort_natural_numbers(self):
        temp_list = random.sample(range(-100000, 100000), 100000)
        test_list, test_list[:] = [], temp_list
        temp_list.sort(), bucket_sort(test_list)
        self.assertEqual(test_list, temp_list)

    def test_sort_negatives(self):
        temp_list = random.sample(range(-200000, 0), 100000)
        test_list, test_list[:] = [], temp_list
        temp_list.sort(), bucket_sort(test_list)
        self.assertEqual(test_list, temp_list)

    def test_sort_positives(self):
        temp_list = random.sample(range(0, 200000), 100000)
        test_list, test_list[:] = [], temp_list
        temp_list.sort(), bucket_sort(test_list)
        self.assertEqual(test_list, temp_list)
        

unittest.main(argv=[''], verbosity=2, exit=False)
