#!/usr/bin/env python3
import sys
from random import randint

def generate_array(amount: int, outfile: str) -> None:
    with open(outfile, 'w') as file:
        print("Writing random numbers to file.")
        file.write(str(amount))
        file.write(" ")
        for _ in range(amount):
            file.write(str(randint(0, 10**6)))
            file.write(" ")
    print("Done writing", amount, "random numbers to", outfile)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        amount = int(sys.argv[1])
        if len(sys.argv) >= 3:
            outfile = sys.argv[2]
        else:
            outfile = str(amount)   +".txt"
    else:
        amount = int(input("How many elements are required in the array? "))
        outfile = input("Specify name of output file: ")

    generate_array(amount, outfile)