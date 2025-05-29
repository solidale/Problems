
# target_sum = m
# len(numbers) = n
def how_sum(target_sum: int, numbers: list[int]) -> list[int]:
    table = [None] * (target_sum + 1) # s: O(m)
    table[0] = []

    for i in range(target_sum): # t: O(m)
        if table[i] != None:
            for number in numbers: # t: O(n)
                if i + number <= target_sum:
                    table[i + number] = table[i] + [number] # t: O(m), s: O(m)
    return table[target_sum]
    # t: O(m^2*n)
    # s: O(m^2)

def test_how_sum():
    assert(how_sum(0, [1, 2, 3]) == [])
    assert(how_sum(8, [2, 4, 5]) == [2, 2, 2, 2])
    assert(how_sum(4, [3, 5]) == None)
    assert(how_sum(7, [5, 3, 4]) == [4, 3])

    assert(how_sum(7, [2, 3]) == [3, 2, 2])
    assert(how_sum(7, [5, 3, 4, 7]) == [4, 3])
    assert(how_sum(7, [2, 4]) == None)
    assert(how_sum(8, [2, 3, 5]) == [2, 2, 2, 2])
    assert(how_sum(300, [7, 14]) == None)

