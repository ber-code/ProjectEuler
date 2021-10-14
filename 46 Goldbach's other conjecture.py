primes = [2]
check = 3
answer = 0
while not answer:
    root_check = check ** 0.5
    check_is_prime = True
    for prime in primes:
        if prime > root_check:
            break
        if check % prime == 0:
            check_is_prime = False
            break
    if check_is_prime:
        primes.append(check)
    else:
        is_goldbach = False
        for prime in primes:
            if (((check - prime) / 2) ** 0.5) % 1 == 0:
                is_goldbach = True
                break
        if not is_goldbach:
            answer = check
    check += 2

print(answer)
