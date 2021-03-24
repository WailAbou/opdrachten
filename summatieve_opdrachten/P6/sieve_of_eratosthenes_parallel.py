import numpy as np
import math


BLOCK_LOW = lambda rank, size, n: (rank * n) // size
BLOCK_HIGH = lambda rank, size, n: BLOCK_LOW(rank + 1, size, n)
BLOCK_SIZE = lambda rank, size, n: BLOCK_LOW(rank + 1, size, n) - BLOCK_LOW(rank, size, n)


def sieve_parallel(n, rank, size, comm):
    low_value = 2 + BLOCK_LOW(rank, size, n - 1)
    high_value = 2 + BLOCK_HIGH(rank, size, n - 1)
    block_size = BLOCK_SIZE(rank, size, n - 1)
    marked = np.arange(low_value, high_value)

    prime, first, index = 2, 0, 0
    while (prime_start := prime * prime) <= n:

        if prime_start > low_value:
            first = prime_start - low_value
        else:
            first = prime - (low_value % prime) if low_value % prime != 0 else 0

        marked[first:block_size:prime] = -1

        if rank == 0:
            while marked[index] == -1:
                index += 1
            prime = index + 2
            index += 1

        prime = comm.bcast(prime)
    
    primes = list(filter(lambda x: x != -1, marked))
    primes = comm.reduce(primes)
    return primes
