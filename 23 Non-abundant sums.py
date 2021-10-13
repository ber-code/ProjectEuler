def sum_of_divisors(n):
    ret = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ret += i + n // i
            if i == n // i:
                ret -= i
    return ret


abundant_numbers = set()

for i in range(12, 28123 + 1):
    if sum_of_divisors(i) > i:
        abundant_numbers.add(i)

non_abundant_sum = 0

for k in range(1, max + 1):
    if not any((k - j) in abundant_numbers for j in abundant_numbers):
        non_abundant_sum += k

print(non_abundant_sum)
