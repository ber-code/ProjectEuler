def is_prime(n):
    if n == 1:
        return False
    if n != 2 and n % 2 == 0:
        return False
    check = 3
    while check <= n ** (1 / 2):
        if n % check == 0:
            return False
        check += 2
    return True


def len_natural(natural):
    if natural == 0:
        return
    return len(str(natural))


def truncate_left(l):
    l %= 10 ** (len_natural(l) - 1)
    return l


def truncate_right(r):
    r //= 10
    return r


count = 0
ret = 0
trunc = 23
while count < 11:
    l = r = trunc
    while len_natural(l) and is_prime(l) and is_prime(r):
        l = truncate_left(l)
        r = truncate_right(r)
    if not len_natural(l):
        ret += trunc
        count += 1
    trunc += 2

print(ret)
