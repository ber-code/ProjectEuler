def sum_square_diff(n):
    square_sum = 0
    sum_square = 0
    for i in range(1, n + 1):
        sum_square += i ** 2
        square_sum += i
    return (square_sum ** 2) - sum_square


print(sum_square_diff(100))
