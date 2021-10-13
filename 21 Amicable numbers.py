def sum_of_divisors(n):
    ret = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret += i + n // i
            if i == n // i:
                ret -= i
    return ret


answer = 0

for i in range(2, 10001):
    check = sum_of_divisors(i)
    if sum_of_divisors(check) == i and i != check:
        answer += i

print(answer)
