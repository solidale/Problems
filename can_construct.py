from datetime import datetime
# "Haus" ("Ha", "u", "zum", "s")
# "haus" ("hu", "as")
def can_construct(target: str, word_bank: list[str]) -> bool:
    if target == "": return True

    for word in word_bank:
        if target.startswith(word):
            sub_target = target[len(word):]
            if can_construct(sub_target, word_bank):
                return True
           
    return False

def can_construct_dyn(target: str, word_bank: list[str], memo = {}) -> bool:
    if target in memo: return memo[target]
    
    for word in word_bank:
        if target.startswith(word):
            sub_target = target[len(word):]
            if can_construct(sub_target, word_bank):
                memo[target] = True
                return True

    memo[target] = False
    return False

def test_can_construct():
    assert can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
    assert can_construct("skateboard", ["bo","rd","ate","t","ska","sk","boar"]) == False
    assert can_construct("eeeeeeeeeeeeeeef", ["e"]) == False
    
def test_can_construct_dyn():
    assert can_construct_dyn("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
    assert can_construct_dyn("skateboard", ["bo","rd","ate","t","ska","sk","boar"]) == False
    assert can_construct_dyn("eeeeeeeeeeeeeeef", ["e"]) == False


start = datetime.now()
can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee"])
print(f"unoptimized version takes: {datetime.now() - start}")

start = datetime.now()
can_construct_dyn("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e","ee","eee","eeee","eeeee"])
print(f"optimized version takes: {datetime.now() - start}")


# class MyTest(unittest.TestCase):
#     def test(self):
#         self.assertEqual(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]), True)
#         self.assertEqual(can_construct("skateboard", ["bo","rd","ate","t","ska","sk","boar"]), True)
# test = MyTest()
# test.test()