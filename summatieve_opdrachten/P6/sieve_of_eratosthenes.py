import numpy as np
from mpi4py import MPI
import math


def sieve(N):
    k, numbers = 2, np.arange(2, N)
    for i in range(math.isqrt(N)):
        if numbers[i] != 0:
            k = numbers[i]

        if (start := k ** 2) > N:
            break

        numbers[start-2:N:k] = 0

    primes = list(filter(lambda num: num != 0, numbers))
    return primes
