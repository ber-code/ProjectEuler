import itertools

answer = 0


def sub_string_divisible(perm):
    if perm[0] == "0":
        return
    primes = [2, 3, 5, 7, 11, 13, 17]
    for counter, prime in enumerate(primes):
        if int(perm[counter + 1 : counter + 4]) % prime != 0:
            return
    return True


for perm in itertools.permutations(range(0, 10), 10):
    string_perm = "".join(map(str, perm))
    if sub_string_divisible(string_perm):
        answer += int(string_perm)
print(answer)
