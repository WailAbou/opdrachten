from sieve_of_eratosthenes import sieve
from mpi4py import MPI
from sympy import primerange

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def test_primes(n):
    start_time = MPI.Wtime()
    primes = sieve(n, rank, size, comm)
    end_time = MPI.Wtime()

    if rank == 0:
        print(f"\nSuccefully found the primes of {n} numbers = {primes == list(primerange(0, n + 1))}")
        print(f"Total elapsed time: {end_time - start_time}")


test_primes(100)
test_primes(1_000)
test_primes(100_000)
test_primes(1_000_000)
