import itertools

primes = [2]


def prime_generator(num):
    if num % 2 == 0:
        return False
    root_num = num ** 0.5
    for prime in primes:
        if prime > root_num:
            break
        if num % prime == 0:
            return False
    primes.append(num)
    return True


def is_prime(num):
    if num % 2 == 0:
        return False
    for denom in range(3, int(num ** 0.5) + 1, 2):
        if num % denom == 0:
            return False
    return True


for num in range(3, 56003 + 1, 2):
    prime_generator(num)


def find_prime_digit_replacement_family_of_size(prime, size):
    digit_idx = list(range(len(str(prime))))
    family = []
    for num_digis_replaced in range(1, len(str(prime))):
        for digis_replaced in itertools.combinations(digit_idx, num_digis_replaced):
            for num in range(10):
                test = list(str(prime))
                for digi in digis_replaced:
                    test[digi] = str(num)
                test = int("".join(i for i in test))
                if len(str(test)) == digit_idx[-1] + 1 and is_prime(test):
                    family.append(test)
                    if len(family) == size:
                        return family
            family = []


check = 56005
smallest_family = None
while not smallest_family:
    if prime_generator(check):
        smallest_family = find_prime_digit_replacement_family_of_size(check, 8)
    check += 2
print(smallest_family[0])
