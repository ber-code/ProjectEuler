def lcm_of_range(n):
    if n == 1:
        return 0
    answer = 2
    prime_factors = [2]
    for i in range(3, n + 1):
        for j in prime_factors:
            if i % j == 0:
                i //= j
        if i != 1:
            prime_factors.append(i)
            answer *= i
    return answer


print(lcm_of_range(20))
