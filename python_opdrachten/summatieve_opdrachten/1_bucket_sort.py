import math

def bucket_sort(data):
    postives, negatives = [x for x in data if x >= 0], [-x for x in data if x < 0]
    sort_list(postives), sort_list(negatives)

    negatives = list(map(lambda x: -x, reversed(negatives)))
    data[:] = negatives + postives

def sort_list(data):
    k = len(str(max(data))) if len(data) > 0 else 0
    decimal = math.ceil(len(str(min(data))) / 2) if len(data) > 0 else 0 

    for i in range(k):
        bucket = [[] for y in range(10)]
        for number in data:
            digit = get_digit(number, decimal, i)
            bucket[digit].append(number)
        data[:] = sum(bucket, [])

def get_digit(number, decimal, n):
    number = int(number * (10 ** (decimal - 1))) if type(number) != int else number
    return number // 10 ** n % 10
