import math as m
import time

t0 = time.time()
a_square_list = [pow(i, 2) for i in range(1, 1001)]
b_square_list = [pow(i, 2) for i in range(1, 1001)]
c_square_list = [pow(i, 2) for i in range(1, 1001)]

for i, a in enumerate(a_square_list, 999):
    for j, b in enumerate(b_square_list, 999):
        for k, c in enumerate(c_square_list, 999):
            if c == (a + b) and (m.sqrt(a) + m.sqrt(b) + m.sqrt(c)) == 1000:
                print(m.sqrt(c) * m.sqrt(a) * m.sqrt(b))

t1 = time.time()

print(t1-t0)