# len(target) = m
# len(word_bank) = n

def can_construct_tabulation(target: str, word_bank: list[str]) -> bool:
    table = [False] * (len(target) + 1) # s: O(m)
    table[0] = True

    for i in range(len(target)): # t: O(m)
        if table[i] == True:
            for word in word_bank: # t: O(n)
                # suffix = target[i:]
                # if suffix.startswith(word) == True:
                #     table[i + len(word)] = True
                if (target[i:i + len(word)] == word): # t: O(m)
                    table[i + len(word)] = True
    
    return table[len(target)]
    # time: O(m*m*n)
    # space: O(m)
    
def test_can_construct_tabulation():
    assert can_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
    assert can_construct_tabulation("skateboard", ["bo","rd","ate","t","ska","sk","boar"]) == False
    assert can_construct_tabulation("eeeeeeeeeeeeeeef", ["e"]) == False
    