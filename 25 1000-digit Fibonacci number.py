def nth_index_fibonacci(n):
    answer = 1
    a = 0
    b = 1
    while len(str(b)) < n:
        answer += 1
        c = a + b
        a = b
        b = c
    return answer


print(nth_index_fibonacci(1000))
