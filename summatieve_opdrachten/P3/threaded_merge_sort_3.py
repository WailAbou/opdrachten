import multiprocessing


def merge_sort_threaded(data):
    processes = multiprocessing.cpu_count()
    batch_size = len(data) // processes
    pool = multiprocessing.Pool(processes=processes)

    data = [data[i * batch_size : (i + 1) * batch_size] for i in range(processes)]
    data = pool.map(merge_sort, data)

    while len(data) > 1:
        data = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        data = pool.map(merge, data)

    return data[0]


def merge_sort(data):
    if (length := len(data)) <= 1:
        return data

    middle = length // 2
    left, right = merge_sort(data[:middle]), merge_sort(data[middle:])
    
    return merge(left, right)


def merge(*data):
    left, right = data[0] if len(data) == 1 else data
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0

    merged_data = []
    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            merged_data.append(left[left_index])
            left_index += 1
        else:
            merged_data.append(right[right_index])
            right_index += 1
    merged_data.extend(right[right_index:] if left_index == left_length else left[left_index:])

    return merged_data
