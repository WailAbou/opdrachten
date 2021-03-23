import unittest
import sympy
from sieve_of_eratosthenes import sieve
import time


class TestSieve(unittest.TestCase):
    
    def compare_primes(self, N):
        start = time.time()
        my_primes = sieve(N)
        end = time.time()
        print(f'\nIt takes {end - start:.2f} seconds to find the primes of {N} elements.')

        other_primes = list(sympy.primerange(0, N))
        self.assertEqual(my_primes, other_primes)

    # def test_100_000(self):
        # self.compare_primes(100_000)

    # def test_1_000_000(self):
    #     self.compare_primes(1_000_000)

    def test_10_000_000(self):
        self.compare_primes(10_000_000)


unittest.main(argv=[''], verbosity=2)
