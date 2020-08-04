"""
Project Euler

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math
import time

num = 600851475143


def is_prime(prime):
    for n in range(2, prime):
        if prime % n == 0:
            return False
    print(prime)
    return True


t0 = time.time()
for i in range(2, int(math.sqrt(num))):
    if num % i == 0:
        is_prime(i)

t1 = time.time()

print(t1 - t0)
