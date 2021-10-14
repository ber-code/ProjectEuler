def is_pentagonal(n):
    return 0 == (1 + (1 + 24 * n) ** 0.5) % 6


def is_hexagonal(n):
    return 0 == (1 + (1 + 8 * n) ** 0.5) % 4


def triangler(n):
    return n * (n + 1) // 2


n = 286
answer = 0
while answer == 0:
    triangle = triangler(n)
    if is_hexagonal(triangle) and is_pentagonal(triangle):
        answer = triangle
    n += 1
print(answer)
