def largest_palindrome_product(n):
    answer = 0
    for i in range(10 ** (n - 1), 10 ** n - 1):
        for j in range(i, 10 ** n - 1):
            product = i * j
            if product > answer:
                text = str(product)
                if text == text[::-1]:
                    answer = product
    return answer


print(largest_palindrome_product(3))
