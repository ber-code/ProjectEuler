def nth_prime(n):
    primes = [2]
    check = 3
    while len(primes) < n:
        rootcheck = check ** 0.5
        for i in primes:
            if i > rootcheck:
                primes.append(check)
                break
            if check % i == 0:
                break
        check += 2
    return primes.pop()


print(nth_prime(10001))
