from bucket_sort_1 import *
import numpy as np
import random
import unittest


class TestNotebook(unittest.TestCase):
    
    def test_sort_real_numbers(self):
        temp_list = list(map(lambda x: round(x, 10), np.random.uniform(low=-100.005, high=100.005, size=(100000,))))
        test_list, test_list[:] = [], temp_list
        temp_list.sort(), bucket_sort(test_list)
        self.assertEqual(test_list, temp_list)

    def test_sort_natural_numbers(self):
        temp_list = random.sample(range(0, 100000), 500)
        test_list, test_list[:] = [], temp_list
        temp_list.sort(), bucket_sort(test_list)
        self.assertEqual(test_list, temp_list)

    def test_sort_mix_numbers(self):
        temp_list = random.sample(range(0, 100000), 50000) + list(map(lambda x: round(x, 3), np.random.uniform(low=0.005, high=100.005, size=(50000,))))
        test_list, test_list[:] = [], temp_list
        temp_list.sort(), bucket_sort(test_list)
        self.assertEqual(test_list, temp_list)
        

unittest.main(argv=[''], verbosity=2)
