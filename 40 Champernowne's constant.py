length = 0
nth_digits = 1
exponent = 0
answer = 1
while length < 1000001:
    for digit in str(nth_digits):
        length += 1
        if length % (10 ** exponent) == 0:
            answer *= int(digit)
            exponent += 1
    nth_digits += 1

print(answer)
