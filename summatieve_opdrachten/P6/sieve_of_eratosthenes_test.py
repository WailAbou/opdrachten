from sieve_of_eratosthenes_parallel import sieve_parallel
from sieve_of_eratosthenes_sequential import sieve_sequential
from mpi4py import MPI
from sympy import primerange


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def time_it(time_func, *args):
    start_time = MPI.Wtime()
    time_val = time_func(*args)
    end_time = MPI.Wtime()
    elapsed_time = end_time - start_time
    return time_val, elapsed_time


def test_primes(n):
    primes_parallel, elapsed_time = time_it(sieve_parallel, n, rank, size, comm)

    if rank == 0:
        print(f"\nSuccefully found the primes of {n} numbers in parallel = {primes_parallel == list(primerange(0, n + 1))}")
        print(f"Total elapsed time: {elapsed_time}")

        primes_sequential, elapsed_time = time_it(sieve_sequential, n)
        print(f"\nSuccefully found the primes of {n} numbers in sequential = {primes_sequential == list(primerange(0, n + 1))}")
        print(f"Total elapsed time: {elapsed_time}")


test_primes(100)
test_primes(1_000)
test_primes(100_000)
test_primes(1_000_000)
