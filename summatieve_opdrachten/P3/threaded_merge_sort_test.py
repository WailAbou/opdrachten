import threaded_merge_sort as tms 
import numpy as np
import time


def time_merge_sort(size, threads=8, min_num=-100.0, max_num=100.0):
    '''Creates an array of unsorted data, sort it and checks if it sorted correctly.'''
    unsorted_data = np.random.uniform(min_num, max_num, size)

    start_single = time.time()
    sorted_data_single = tms.merge_sort(unsorted_data)
    end_single = time.time()
    succes = sorted(unsorted_data) == sorted_data_single
    
    print(f'Time taken for single threaded: {end_single - start_single}')
    print(f'The data with size {size} using single thread has been succesfully sorted = {succes}\n')

    start_multi = time.time()
    sorted_data_multi = tms.merge_sort_threaded(unsorted_data, threads)
    end_multi = time.time()
    succes = sorted(unsorted_data) == sorted_data_multi

    print(f'Time taken for multi threaded: {end_multi - start_multi}')
    print(f'The data with size {size} using {threads} threads has been succesfully sorted = {succes}\n')
   

if __name__ == "__main__":
    '''Tests 4 different situations
    1. even number data points and even number threads 
    2. even number data points and odd number threads
    3. odd number data points and even number threads
    4. odd number data points and odd number threads'''
    time_merge_sort(80, 8)
    time_merge_sort(80, 7)
    time_merge_sort(81, 8)
    time_merge_sort(81, 7)
