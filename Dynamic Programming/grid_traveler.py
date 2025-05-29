from datetime import datetime
import pandas as pd

def grid_traveler(m: int, n: int) -> int:
    if m == 0 or n == 0: return 0
    table = [[0 for i in range(n + 1)] for j in range(m + 1)]
    table[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            if i < m:
                table[i + 1][j] += table[i][j]
            if j < n:
                table[i][j + 1] += table[i][j]
    return table[m][n]


rows, cols = (10, 10)
table2 = [[0 for i in range(cols)] for j in range(rows)]
for i in range(rows):
    for j in range(cols):
        table2[i][j] = grid_traveler(i, j)

print(pd.DataFrame(table2))

def test_grid_traveler():
    assert(grid_traveler(1, 1) == 1)
    assert(grid_traveler(2, 3) == 3)
    assert(grid_traveler(3, 2) == 3)
    assert(grid_traveler(3, 3) == 6)
    assert(grid_traveler(18, 18) == 2333606220)