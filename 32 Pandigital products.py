import itertools

answer = set()
master_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def tu_num(tu):
    l = [str(i) for i in tu]
    s = "".join(l)
    return int(s)


"""
max length of product is 4 digits -> multiplicand and multiplier can only be (1 & 4) or (2 & 3) digits
"""
for perm in master_digits:
    it_digits = [i for i in master_digits if i != perm]
    for perm2 in itertools.permutations(it_digits, 4):
        it_digits2 = [i for i in it_digits if i not in perm2]
        for perm3 in itertools.permutations(it_digits2, 4):
            if perm * tu_num(perm2) == tu_num(perm3):
                answer.add(tu_num(perm3))

for perm in itertools.permutations(master_digits, 2):
    it_digits = [i for i in master_digits if i not in perm]
    for perm2 in itertools.permutations(it_digits, 3):
        it_digits2 = [i for i in it_digits if i not in perm2]
        for perm3 in itertools.permutations(it_digits2, 4):
            if tu_num(perm) * tu_num(perm2) == tu_num(perm3):
                answer.add(tu_num(perm3))

print(sum(answer))
