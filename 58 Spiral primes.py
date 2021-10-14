def is_prime(number):
    if number % 2 == 0:
        return False
    for denominator in range(3, int(number ** 0.5) + 1, 2):
        if number % denominator == 0:
            return False
    return True


number, corner_count, prime_count, increment = 9, 5, 3, 2
while prime_count / corner_count > 1 / 10:
    corner_count += 4
    increment += 2
    for i in range(3):
        number += increment
        if is_prime(number):
            prime_count += 1
    number += increment
print(increment + 1)
