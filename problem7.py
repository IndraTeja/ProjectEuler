"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math
import time

n = 2

counter = 0


def is_prime(prime):
    # checking only odd numbers
    for i in range(2, int(math.sqrt(prime))):

        if prime % i == 0:
            return False
    return True


t0 = time.time()
while True:
    # eliminate even numbers
    # if n % 2 == 0:
    #     pass
    if is_prime(n):
        counter += 1

    if counter == 10001:
        break

    n += 1
t1 = time.time()

print(t1 - t0)

print(n)
