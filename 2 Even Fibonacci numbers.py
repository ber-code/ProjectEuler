def sum_even_fibs(n):
    answer = 0
    a = 0
    b = 1
    while b < n:
        if b % 2 == 0:
            answer += b
        c = a + b
        a = b
        b = c
    return answer


print(sum_even_fibs(4000000))
