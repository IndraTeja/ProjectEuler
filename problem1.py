"""
Project Euler

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

sum_of_multiples = 0

for i in range(3, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_of_multiples = i + sum_of_multiples  # O(n)

print(sum_of_multiples)

# target = 1_000_000_000

# def sum_divisible_by(n):
#     p = target / n
#     return n * ((p * (p+1)) / 2)

# print(sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15))
