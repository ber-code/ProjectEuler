def largest_prime_factor(n):
    check = 3
    prime_factors = []
    if n % 2 == 0:
        prime_factors.append(2)
        while n % 2 == 0:
            n //= 2
    while check <= n:
        if n % check == 0:
            prime_factors.append(check)
            while n % check == 0:
                n //= check
        check += 2
    return prime_factors[-1]


print(largest_prime_factor(600851475143))
