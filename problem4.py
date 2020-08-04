"""
Project Euler

Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time

product_list = []


def is_palindrome(product_of_list):
    rev = 0
    temp = product_of_list
    while product_of_list > 0:
        remainder = product_of_list % 10
        rev = (rev * 10) + remainder
        product_of_list = product_of_list // 10
    if temp == rev:
        return True
    return False


t0 = time.time()
for i in range(100, 999):
    for j in range(100, 999):
        product = i * j
        if is_palindrome(product):
            product_list.append(product)

product_list.sort()
t1 = time.time()
print("time taken : " + format(t1 - t0) + " sec")
print(product_list[-1])
