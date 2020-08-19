import time

triangle_num = 0
n = 1
divisor_count = 0
loop = True

def highest_divisors(n):
    divisor_count = 0
    for i in range(1, n//2):
        if(n % i == 0):
            divisor_count += 1
    return divisor_count

t0 = time.time()
while loop:
    n = n + 1
    triangle_num = (n * (n+1) // 2)
    divisor = (highest_divisors(triangle_num))
    if (divisor > 500):
        print(divisor)
        print("triangle num is", triangle_num)
        # print(triangle_num)
        loop = False
t1 = time.time()
print(t1-t0)
