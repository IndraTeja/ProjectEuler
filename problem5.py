import math

lcm = 1

for i in range(1,21):
    lcm = (lcm * i) // math.gcd(i,lcm)

print(lcm)