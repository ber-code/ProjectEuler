coefficients = range(-999, 1000)
constants = range(-1000, 1001)
consecutive = 0
answer = 0
coefficient_a = 0
constant_b = 0


def quadratic(n):
    return n ** 2 + a * n + b


def isprime(q):
    check = 3
    pfactors = []
    if q <= 0:
        return False
    if q == 2:
        return True
    if q % 2 == 0:
        return False
    while check <= q ** 0.5:
        if q % check == 0:
            return False
        check += 2
    return True


for a in coefficients:
    for b in constants:
        n = 0
        while isprime(quadratic(n)) == True:
            if n >= consecutive:
                consecutive = n
                answer = a * b
                coefficient_a = a
                constant_b = b
            n += 1
print(
    "The answer is "
    + str(answer)
    + ". The coefficient is "
    + str(coefficient_a)
    + " and the constant is "
    + str(constant_b)
    + ". The number of consecutive primes is "
    + str(consecutive)
    + "."
)
