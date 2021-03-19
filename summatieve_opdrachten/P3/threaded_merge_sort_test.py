import threaded_merge_sort as tms 
import numpy as np


def check_sort(size, threads=8, min_num=-100.0, max_num=100.0):
    '''Creates an array of unsorted data, sort it and checks if it sorted correctly.'''
    unsorted_data = np.random.uniform(min_num, max_num, size)
    sorted_data = tms.merge_sort_threaded(unsorted_data, threads)
    succes = sorted(unsorted_data) == sorted_data
    print(f'The data with size {size} using {threads} threads has been succesfully sorted = {succes}')

if __name__ == "__main__":
    '''Tests 4 different situations
    1. even number data points and even number threads 
    2. even number data points and odd number threads
    3. odd number data points and even number threads
    4. odd number data points and odd number threads'''
    check_sort(80, 8)
    check_sort(80, 7)
    check_sort(81, 8)
    check_sort(81, 7)
