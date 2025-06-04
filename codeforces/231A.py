"""
3
1 1 0
1 1 1
1 0 0
"""

numberOfProblems = int(input())
numberOfSolvedProblems = 0

for i in range(numberOfProblems):
    line = input()
    line = line.split(" ")
    numbers = [int(x) for x in line]
    if sum(numbers) > 1:
        numberOfSolvedProblems += 1

print(numberOfSolvedProblems)

        