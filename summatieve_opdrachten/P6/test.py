import numpy as np
from mpi4py import MPI
import math


def BLOCK_LOW(rank, size, n):
    return (rank * n) // size

def BLOCK_HIGH(rank, size, n):
    return BLOCK_LOW(rank + 1, size, n) - 1

def BLOCK_SIZE(rank, size, n):
    return BLOCK_LOW(rank + 1, size, n) - BLOCK_LOW(rank, size, n)

comm = MPI.COMM_WORLD
comm.barrier()

elapsed_time = -MPI.Wtime()
rank = comm.Get_rank()
size = comm.Get_size()

n = 100
low_value = 2 + BLOCK_LOW(rank, size, n - 1)
high_value = 2 + BLOCK_HIGH(rank, size, n - 1)
block_size = BLOCK_SIZE(rank, size, n - 1)

marked = np.zeros(block_size)
prime = 2
first = 0
index = 0
while prime * prime <= n:
    if prime * prime > low_value:
        first = prime * prime - low_value
    else:
        if low_value % prime == 0:
            first = 0
        else:
            first = prime - (low_value % prime)

    for i in range(first, block_size, prime):
        marked[i] = 1

    if rank == 0:
        while marked[index] != 0:
            index += 1
        prime = index + 2
        index += 1
    prime = comm.bcast(prime)

print(rank, marked)
count = 0
global_count = 0
for i in range(block_size):
    if marked[i] == 0:
        count += 1

global_count = comm.reduce(count)
elapsed_time += MPI.Wtime()

if rank == 0:
    print(f"{global_count} primes are less than or eqaul to {n}")
    print(f"Total elapsed time: {elapsed_time}")