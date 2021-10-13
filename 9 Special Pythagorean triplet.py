def special_pythagorean_triplet_with_sum(n):
    a = 1
    while a < n - 2:
        for b in range(1, a):
            c = (a ** 2 + b ** 2) ** 0.5
            if a + b + c == n:
                return a * b * c
        a += 1
    return "There as no answer."


print(special_pythagorean_triplet_with_sum(1000))
