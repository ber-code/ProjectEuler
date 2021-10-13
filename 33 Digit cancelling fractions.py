answer = 1
numerators = []
digits = 2


def prime_factors(n):
    check = 3
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    while check <= n:
        while n % check == 0:
            prime_factors.append(check)
            n //= check
        check += 2
    return prime_factors


for numerator in range(10 ** (digits - 1), 10 ** digits - 2):
    for denominator in range(numerator + 1, 10 ** digits - 1):
        if numerator % 10 == 0 and denominator % 10 == 0:
            None
        elif (
            numerator % 10 == denominator % 10
            and denominator // 10 != 0
            and (numerator // 10) / (denominator // 10) == numerator / denominator
        ):
            numerators.append(numerator)
            answer *= denominator
        elif (
            numerator % 10 == denominator // 10
            and denominator % 10 != 0
            and (numerator // 10) / (denominator % 10) == numerator / denominator
        ):
            numerators.append(numerator)
            answer *= denominator
        elif (
            numerator // 10 == denominator % 10
            and denominator // 10 != 0
            and (numerator % 10) / (denominator // 10) == numerator / denominator
        ):
            numerators.append(numerator)
            answer *= denominator
        elif (
            numerator // 10 == denominator // 10
            and denominator % 10 != 0
            and (numerator % 10) / (denominator % 10) == numerator / denominator
        ):
            numerators.append(numerator)
            answer *= denominator

numerator_prime_factors = []
for numerator in numerators:
    numerator_prime_factors += prime_factors(numerator)

for prime_numerator in numerator_prime_factors:
    if answer % prime_numerator == 0:
        answer //= prime_numerator

print(answer)
