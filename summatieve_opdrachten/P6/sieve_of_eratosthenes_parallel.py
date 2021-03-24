import numpy as np
import math

# Gets the begin value of the array chunk
BLOCK_LOW = lambda rank, size, n: (rank * n) // size
# Gets the end value of the array chunk
BLOCK_HIGH = lambda rank, size, n: BLOCK_LOW(rank + 1, size, n)
# Gets the size of the array chunk
BLOCK_SIZE = lambda rank, size, n: BLOCK_LOW(rank + 1, size, n) - BLOCK_LOW(rank, size, n)


def sieve_parallel(n, rank, size, comm):
    '''given n the rank the size (amount of processes) and the communication
    returns a list of the final primes if rank 0 or else returns None'''

    low_value = 2 + BLOCK_LOW(rank, size, n - 1)
    high_value = 2 + BLOCK_HIGH(rank, size, n - 1)
    block_size = BLOCK_SIZE(rank, size, n - 1)
    # List of integers from low_value to high_value
    marked = np.arange(low_value, high_value)

    prime, first, index = 2, 0, 0
    # Looping until prime^2 is bigger then n then we know we found all the primes
    while (prime_start := prime * prime) <= n:

        # Gets the first multiple of the prime to start marking from
        if prime_start > low_value:
            first = prime_start - low_value
        else:
            first = prime - (low_value % prime) if low_value % prime != 0 else 0

        # Marking all the multiple of the primes excep it self
        marked[first:block_size:prime] = -1

        # If rank 0 find the next prime to broadcast it to the other ranks
        if rank == 0:
            while marked[index] == -1:
                index += 1
            prime = index + 2
            index += 1

        prime = comm.bcast(prime)
    
    # Filter all the -1 out
    primes = list(filter(lambda x: x != -1, marked))
    # Reduce all the primes list to 1 in the root processes
    primes = comm.reduce(primes)
    return primes
