from datetime import datetime

def fib(target: int) -> int:
    if target <= 2: return 1

    return fib(target - 1) + fib(target - 2)

def fib_tab(target: int) -> int:
    tab = [0] * (target)
    tab[0] = tab[1] = 1
    for i in range(2,target):
        tab[i] = tab[i - 1] + tab[i - 2]
    return tab[target - 1]

start = datetime.now()
print(fib(37))
print(f"Recursive solution took {datetime.now() - start}")

start = datetime.now()
print(fib_tab(37))
print(f"Tabulation solution took {datetime.now() - start}")