def first_triangle_number_with_over_n_factors(n):
    triangle = 1
    step = 2
    while True:
        count = 2
        for j in range(3, int(triangle ** 0.5) + 1):
            if triangle % j == 0:
                if j == (triangle ** 0.5):
                    count += 1
                else:
                    count += 2
            if count > n:
                return triangle
        triangle += step
        step += 1


print(first_triangle_number_with_over_n_factors(500))
