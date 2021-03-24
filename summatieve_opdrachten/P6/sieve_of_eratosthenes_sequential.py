import numpy as np
import math


def sieve_sequential(n):
    '''given n gets all the primes from 2 to n and returns it'''
    
    prime, numbers = 2, np.arange(2, n)
    # Looping until square of n then we know we found all the primes
    for i in range(math.isqrt(n)):
        if numbers[i] != 0:
            prime = numbers[i]

        # Stopping if k^2 is bigger then n
        if (start := prime ** 2) > n:
            break

        # Marking all numbers from start - 2 to n with steps of k (prime) with 0
        numbers[start-2:n:prime] = 0

    # Reduce all the primes list to 1 in the root processes
    primes = list(filter(lambda num: num != 0, numbers))
    return primes
