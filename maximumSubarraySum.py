import random
from datetime import datetime

# input = [-1, 2, 4, -3, 5, 2, -5, 2]


input = [random.randint(-10, 10) for i in range(10**4)] # of length n

# O(n^3) solution
start = datetime.now()
max_sum = 0
subarray = []

for a in range(len(input)): # O(n)
    for b in range(a, len(input)): # O(n)
        curr = input[a:b] # O(n)
        if sum(curr) > max_sum:
            subarray = curr
            max_sum = sum(curr)
print(f"sum of max subarray is {max_sum}")
print(f"O(n^3) solution took {datetime.now() - start}")

# O(n^2) solution
# start = datetime.now()
# sum = 0
# a = 0
# b = 0
# max_sum = 0
# for a in range(len(input)):
#     sum = 0
#     for b in range(len(input)):
#         sum += input[b]
#         max_sum = max(max_sum, sum)
# print(f"sum of max subarray is {max_sum}")
# print(f"O(n^2) solution took {datetime.now() - start}")


# O(n) solution
start = datetime.now()
sum = 0
max_sum = 0
for k in range(len(input)):
    sum = max(input[k], sum + input[k])
    max_sum = max(sum, max_sum)
print(f"sum of max subarray is {max_sum}")
print(f"O(n) solution took {datetime.now() - start}")

