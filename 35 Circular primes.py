def rotate(number):
    ret = str(number)
    ret = ret[1:] + ret[0]
    return ret


def is_prime(n):
    if n != 2 and n % 2 == 0:
        return False
    check = 3
    while check <= n ** (1 / 2):
        if n % check == 0:
            return False
        check += 2
    return True


def count_circular_prime_below(cap):
    if cap < 2:
        return 0
    count = 1
    check = 3
    while check < cap:
        rotation = 0
        j = check
        while is_prime(int(j)) and rotation < len(str(check)):
            j = rotate(j)
            rotation += 1
        if rotation == len(str(check)):
            count += 1
        check += 2
    return count


print(count_circular_prime_below(1000000))
