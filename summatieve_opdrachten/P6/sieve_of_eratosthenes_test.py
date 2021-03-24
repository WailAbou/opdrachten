from sieve_of_eratosthenes_parallel import sieve_parallel
from sieve_of_eratosthenes_sequential import sieve_sequential
from mpi4py import MPI
from sympy import primerange


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


def time_it(time_func, *args):
    '''Times the function calls and returns the elapsed 
    time along with the function result'''

    start_time = MPI.Wtime()
    func_result = time_func(*args)
    end_time = MPI.Wtime()
    elapsed_time = end_time - start_time
    return func_result, elapsed_time


def test_primes(n):
    '''Run the parallel sieve and sequential sieve given n 
    as the range of integers to search primes for prints their results 
    and checks if they are correct'''
    
    primes_parallel, elapsed_time = time_it(sieve_parallel, n, rank, size, comm)

    if rank == 0:
        primes = list(primerange(0, n + 1))
        print(f"\nSuccefully found the primes of {n} numbers in parallel = {primes_parallel == primes}")
        print(f"Total elapsed time: {elapsed_time}")

        primes_sequential, elapsed_time = time_it(sieve_sequential, n)
        print(f"\nSuccefully found the primes of {n} numbers in sequential = {primes_sequential == primes}")
        print(f"Total elapsed time: {elapsed_time}")


test_primes(100)
test_primes(1_000)
test_primes(100_000)
test_primes(1_000_000)
