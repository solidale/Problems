from datetime import datetime

def all_construct(target: str, word_bank: list[str]) -> list[list[str]]:
    if target == "": return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [[word] + ways for ways in suffix_ways]
            flat_target_ways = [item for sublist in target_ways for item in sublist]
            result.append(flat_target_ways)
    
    return result

def test_all_construct():
    assert(all_construct("abcdef", ["ab", "cd", "ef", "abc", "def"]) == [["ab","cd","ef"], ["abc","def"]])
    assert(all_construct("abcdef", ["a", "b", "c", "bc", "cd", "cde"]) == [[]])