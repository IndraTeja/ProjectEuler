import time
import math

n = 2000000
counter = 2
sum_of_primes = 0


def is_prime(prime):
    for i in range(2, int(math.sqrt(prime)) + 1):
        if prime % i == 0:
            return False
    return True


t0 = time.time()
while True:
    if is_prime(counter):
        sum_of_primes += counter
    if counter == n:
        break
    counter += 1
t1 = time.time()

print(t1 - t0)
print(sum_of_primes)
