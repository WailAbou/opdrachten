import threaded_merge_sort_3 as tms 
import numpy as np


if __name__ == "__main__":
    unsorted_data = np.random.uniform(-100.0, 100.0, 1000)
    sorted_data = tms.merge_sort_threaded(unsorted_data)
    print(sorted(unsorted_data) == sorted_data)
