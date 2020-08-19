sum = 0
one_hundred_nums = []

with open(file="problem-13.txt") as file:
    data = file.read().replace('\n', '')


def list_numbers(data, n):
    for start in range(0, len(data), n):
        yield data[start:start + n]


for d in list_numbers(data, 50):
    one_hundred_nums.append(d)

for i in one_hundred_nums:
    sum += int(i)

print(str(sum)[0:10])
