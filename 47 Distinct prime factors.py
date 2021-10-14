primes = [2]


def number_has_target_distinct_prime_factors(number, target):
    working_number = number
    factors = []
    root_number = number ** 0.5
    for prime in primes:
        if working_number < prime:
            break
        if working_number % prime == 0:
            factors.append(prime)
            while working_number % prime == 0:
                working_number //= prime
    if not factors:
        primes.append(number)
        return False
    if len(factors) == target:
        return True
    return False


target_length, check, length, answer = 4, 3, 0, 0

while length < target_length:
    if number_has_target_distinct_prime_factors(check, target_length):
        if length == 0:
            answer = check
        length += 1
    else:
        length = 0
    check += 1

print(answer)
