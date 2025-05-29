from datetime import datetime

def count_construct(target: str, word_bank: list[str]) -> int:
    if target == "": return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            count_ways_for_rest = count_construct(suffix, word_bank)
            total_count += count_ways_for_rest

    return total_count

def count_construct_dyn(target: str, word_bank: list[str], memo = {}) -> int:
    if target in memo: return memo[target]
    if target == "": return 1

    total_count = 0

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            count_ways_for_rest = count_construct(suffix, word_bank)
            total_count += count_ways_for_rest

    memo[target] = total_count
    return total_count


def test_count_construct():
    assert(count_construct("abcdef",  ["a","b","ab","cde","f"]) == 2)
    assert(count_construct("abcdef", ["a","b", "ab", "c", "cd", "cde", "abcde"]) == 0)
    assert(count_construct_dyn("abcdef",  ["a","b","ab","cde","f"]) == 2)
    assert(count_construct_dyn("abcdef", ["a","b", "ab", "c", "cd", "cde", "abcde"]) == 0)

start = datetime.now()
print(count_construct("abcdef",  ["a","b","ab","cde","f"]))
print(count_construct("abcdef", ["a","b", "ab", "c", "cd", "cde", "abcde"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee","eeeeeee"]))
print(f"unoptimized solution took: {datetime.now() - start}")

start = datetime.now()
print(count_construct_dyn("abcdef",  ["a","b","ab","cde","f"]))
print(count_construct_dyn("abcdef", ["a","b", "ab", "c", "cd", "cde", "abcde"]))
print(count_construct_dyn("eeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee","eeeeeee"]))
print(f"unoptimized solution took: {datetime.now() - start}")
