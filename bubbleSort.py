
import random

def bubbleSort(inputList: list[int]):
    for i in range(len(inputList)):
        for j in range(i, len(inputList)):
            if inputList[i] > inputList[j]:
                inputList[i], inputList[j] = inputList[j], inputList[i]

inputList = [random.randint(-100, 100) for x in range(20)]
print(inputList)

bubbleSort(inputList)
print(inputList)