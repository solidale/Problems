"""
3
dog
dogdogdogdog
catcatcat
"""

numberOfWords = int(input())
for i in range(numberOfWords):
    line = input()
    abbreviation = ""

    if len(line) > 10:
        print(line[0] + str(len(line) - 2) + line[-1])
    else:
        print(line)
