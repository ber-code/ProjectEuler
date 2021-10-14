import math


def n_select_r(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


answer = 0
for n in range(1, 101):
    for r in range(n + 1):
        if n_select_r(n, r) > 1000000:
            answer += 1
print(answer)
