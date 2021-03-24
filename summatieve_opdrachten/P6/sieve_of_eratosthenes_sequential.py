import numpy as np
import math


def sieve_sequential(n):
    k, numbers = 2, np.arange(2, n)
    for i in range(math.isqrt(n)):
        if numbers[i] != 0:
            k = numbers[i]

        if (start := k ** 2) > n:
            break

        numbers[start-2:n:k] = 0

    primes = list(filter(lambda num: num != 0, numbers))
    return primes
