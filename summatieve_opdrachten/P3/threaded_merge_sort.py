import multiprocessing


def merge_sort_threaded(data, processes=multiprocessing.cpu_count()):
    '''Divides the data into the available processes, sort them locally and 
    then sort them globaly before returning the sorterd result'''

    # Ceils the data divided by the processes
    batch_size = -(-len(data) // processes)
    pool = multiprocessing.Pool(processes=processes)

    # Distrubutes the data between lists so we can pass them to the thread
    data = [data[i * batch_size : (i + 1) * batch_size] for i in range(processes)]
    results = pool.map(merge_sort, data)

    # Begins with a list of the results with a length of the amount of processes
    # then sorts and merges it with the neighbouring one until there is 1 list
    # extra is to keep in mind if we use an odd number of threads which will result in an odd number of results
    # in this case we simply pop it from the stack and put it back after we have sorted the neigbouring one
    # in this case when there would be one list to end with it would be the one plus the odd one to sort as last
    while len(results) > 1:
        extra = results.pop() if len(results) % 2 == 1 else None
        results = [(results[i], results[i + 1]) for i in range(0, len(results), 2)]
        results = pool.map(merge, results) + ([extra] if extra else [])

    return results[0]


def merge_sort(data):
    '''Divides the data into chunks until they are at unit size 
    then sorts them and merges them back up'''

    # Stop condition this means we are at the unit size
    if (length := len(data)) <= 1:
        return data

    # Gets the integer middle by floor dividing the length
    middle = length // 2
    # Divides the data list into two
    left, right = merge_sort(data[:middle]), merge_sort(data[middle:])
    
    # Merges the left and right parts back together
    return merge(left, right)


def merge(*data):
    '''Merges two list together by going trough them both and comparing each
    note the * before data, this is so we can both pass it as a 2 tuples (left, right) which works well for multiprocessing  
    and as 2 separate arguments left, right'''

    # Initializing of all the variables
    left, right = data[0] if len(data) == 1 else data
    left_length, right_length = len(left), len(right)
    left_index, right_index = 0, 0
    merged_data = []

    # While loop going trough all the elements as long as we haven't reached either end
    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            merged_data.append(left[left_index])
            left_index += 1
        else:
            merged_data.append(right[right_index])
            right_index += 1
    
    # Adding the remaining end to the merged data list 
    merged_data.extend(right[right_index:] if left_index == left_length else left[left_index:])
    
    return merged_data
