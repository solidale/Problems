def count_construct_tabulation(target: str, word_bank: list[str]) -> int:
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(table)):
        for word in word_bank:
            if target[i: i + len(word)] == word:
                table[i + len(word)] += table[i]

    return table[len(target)]

def test_count_construct_tabulation():
    assert(count_construct_tabulation("abcdef", ["ab", "cd", "ef", "abc", "def"]) == 2)
    assert(count_construct_tabulation("purple", ["purp", "p", "ur", "le", "purpl"]) == 2)
    assert(count_construct_tabulation("abcdef",  ["a","b","ab","cde","f"]) == 2)
    assert(count_construct_tabulation("abcdef", ["a","b", "ab", "c", "cd", "cde", "abcde"]) == 0)
    assert(count_construct_tabulation("abcdef",  ["a","b","ab","cde","f"]) == 2)
    assert(count_construct_tabulation("abcdef", ["a","b", "ab", "c", "cd", "cde", "abcde"]) == 0)