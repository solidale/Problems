inputWord = input()
k = 0
hello = "hello"
for i in range(len(inputWord)):
    if k == 5:
        break
    if k < 5 and inputWord[i] == hello[k]:
        k += 1

if k == 5:
    print("YES")
else:
    print("NO")

