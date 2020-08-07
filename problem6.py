import time

n = 100
sum_of_squares = 0

sums_of_numbers = 0

t0 = time.time()

sum_of_squares = (n * (n + 1) * ((2 * n) + 1)) / 6

sums_of_numbers = (n * (n + 1) / 2)

# for i in range(1, 101):

#     sum_of_squares += i ** 2

#     sums_of_numbers += i

square_of_sums = sums_of_numbers ** 2
t1 = time.time()

print(t1 - t0)

print(square_of_sums - sum_of_squares)
