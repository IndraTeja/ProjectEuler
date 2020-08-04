
# LCM = 1

# for i in range(2,20):
#     for j in range(2,i):
#         if i % j == 0:
#             LCM = LCM * j

# print(LCM)


# lcm_list = [1,2,3,4,5,6,7,8,9,10]

# for i in lcm_list:
#     if lcm_list//i == 1:
#         lcm_list[i] = 1
#     else:
#         lcm_list[i] = lcm_list//i


# i = 1

# while(i % 2 != 0 and i % 3 != 0 and i % 4 != 0 and i % 5 != 0 and i % 6 != 0 and i % 7 != 0 and i % 8 != 0 and i % 9 != 0 and i % 10 != 0 and i % 11 != 0 and i % 12 != 0 and i % 13 != 0 and i % 14 != 0 and i % 15 != 0 and i % 16 != 0 and i % 17 != 0 and i % 18 != 0 and i % 19 != 0 and i % 20 != 0):
#     i += 1

# print(i)

import math 

lcm = 1

for i in range(1,21):
    lcm = (lcm * i) // math.gcd(i,lcm)

print(lcm)