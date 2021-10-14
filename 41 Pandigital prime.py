import itertools


def is_pandigital(num):
    digits = str(num)
    check = set(str(i) for i in range(1, len(digits) + 1))
    for digit in digits:
        if digit not in check:
            return False
        check.remove(digit)
    return True


def is_prime(num):
    if num % 2 == 0:
        return False
    for denom in range(3, int(num ** 0.5) + 1, 2):
        if num % denom == 0:
            return False
    return True


def largest_pandigital_prime_length_n(n):
    while n > 0:
        for perm in itertools.permutations(reversed(range(1, 1 + n)), n):
            num = int("".join(map(str, perm)))
            if is_pandigital(num) and is_prime(num):
                return num
        n -= 1


print(largest_pandigital_prime_length_n(9))
