# target_sum = m
# len(numbers) = n
def best_sum(target_sum: int, numbers: list[int]) -> list[int]:
    table = [None] * (target_sum + 1) # s: O(m)
    table[0] = []

    for i in range(target_sum): # t: O(m)
        if table[i] != None:
            for number in numbers: # t: O(n)
                if i + number <= target_sum:
                    candidate_combination = table[i] + [number] # t: O(m)
                    if table[i + number] == None:
                        table[i + number] = candidate_combination # s: O(m)
                    elif len(candidate_combination) < len(table[i + number]):
                        table[i + number] = candidate_combination
    return table[target_sum]
    # t: O(m*n*m)
    # s: O(m*m)

def test_best_sum():
    assert(best_sum(8, [2, 3, 5]) == [3, 5])
    # assert(best_sum(7, [2, 3]) == [3, 2, 2])
    assert(best_sum(7, [5, 3, 4, 7]) == [7])
    assert(best_sum(8, [1, 4, 5]) == [4, 4])
    assert(best_sum(100, [1, 2, 5, 25]) == [25, 25, 25, 25])
    # assert(best_sum(7, [2, 4]) == None)
    # assert(best_sum(8, [2, 3, 5]) == [2, 2, 2, 2])
    # assert(best_sum(300, [7, 14]) == None)