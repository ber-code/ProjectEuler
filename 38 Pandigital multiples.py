def pandidital_multiples(num):
    digits = set(str(i) for i in range(1, 10))
    counter = 1
    pandigital = ""
    while digits:
        product = str(num * counter)
        pandigital += product
        for digit in product:
            if digit not in digits:
                return 0
            digits.remove(digit)
        counter += 1
    return int(pandigital)


answer = 0

for num in range(192, 9999):
    test = pandidital_multiples(num)
    if test > answer:
        answer = test

print(answer)
