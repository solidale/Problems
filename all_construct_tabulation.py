
# m = len(target)
# n = len(word_bank)
def all_construct_tabulation(target: str, word_bank: list[str]) -> list[list[str]]:
    table = [[] for i in range(len(target) + 1)] # s: O(n*m)
    table[0] = [[]]

    for i in range(len(target)): 
        for word in word_bank: 
            if target[i: i + len(word)] == word: 
                for combination in table[i]: 
                    table[i + len(word)].append(combination + [word]) 
    
    print(table)
    return len(table[len(target)])
    # time: O(n^m)
    # space: O(n^m)


def test_all_construct_tabulation():
    assert(all_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]) == 4)
    assert(all_construct_tabulation("purple", ["purp", "p", "ur", "le", "purpl"]) == 2)
    assert(all_construct_tabulation("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == 0)