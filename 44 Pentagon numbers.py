def pentagoner(n):
    return int(n * (3 * n - 1) / 2)


def is_pentagonal(n):
    return 0 == (1 + (1 + 24 * n) ** 0.5) % 6


pentagon_numbers = [1]
n = 2
difference = 0
while difference == 0:
    new_pentagon = pentagoner(n)
    for pentagon in reversed(pentagon_numbers):
        if is_pentagonal(new_pentagon + pentagon) and is_pentagonal(
            new_pentagon - pentagon
        ):
            difference = new_pentagon - pentagon
            break
    pentagon_numbers.append(new_pentagon)
    n += 1

print(difference)
