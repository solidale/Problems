

def can_sum(target_sum: int, numbers: list[int]) -> bool:
    table = [False] * (target_sum + 1)
    table[0] = True

    for i in range(len(table)):
        if table[i] == True:
            for number in numbers:
                reachable_number = i + number
                if reachable_number <= target_sum:
                    table[reachable_number] = True
    return table[target_sum]

def test_can_sum():
    assert(can_sum(0, [1, 2, 3, 4]) == True)
    assert(can_sum(4, [1, 2, 3]) == True)
    assert(can_sum(2, [3, 4, 5]) == False)
    assert(can_sum(7, [5, 4, 3]) == True)
    assert(can_sum(7, [2, 3]) == True)
    assert(can_sum(7, [5, 3, 4, 7]) == True)
    assert(can_sum(7, [2, 4]) == False)
    assert(can_sum(8, [2, 3, 5]) == True)
    assert(can_sum(300, [7, 14]) == False)