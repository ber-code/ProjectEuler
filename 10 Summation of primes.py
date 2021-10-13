def sum_of_primes_below(n):
    if n < 2:
        return 0
    primes_list = [2]
    check = 3
    while check < n:
        for prime in primes_list:
            if prime > check ** 0.5:
                primes_list.append(check)
                break
            if check % prime == 0:
                break
        check += 2
    return sum(primes_list)


print(sum_of_primes_below(2000000))
