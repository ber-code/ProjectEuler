def nth_digit_permutation(n):
    n -= 1
    digits = "0123456789"
    nthpermuation = ""
    factoradic = ""

    for number in range(1, 11):
        factoradic += str(n % int(number))
        n //= int(number)
    factoradic = factoradic[::-1]

    for factorial in factoradic:
        remove = digits[int(factorial)]
        nthpermuation += remove
        digits = digits.replace(remove, "")
    return nthpermuation


print(nth_digit_permutation(1000000))
