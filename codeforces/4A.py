# import sys

# w = int(input())
# if w == 1 or w == 2:
#     print("NO")
# elif w % 2 == 0:
#     print("YES")
# else:
#     print("NO")


def calculateFrequencies(combination: list[int]):
    freq = {}
    for number in combination:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1
    return freq

print(calculateFrequencies([2,2,2,2]))
print(calculateFrequencies([2,3,3]))
print(calculateFrequencies([3,2,3]))
print(calculateFrequencies([2,3,3]) == calculateFrequencies([3,2,3]))