check = range(32, 354295)  # (9^5)*6 = 354295, natural maximum
answer = 0
for number in check:
    digits = str(number)
    sumdigits = 0
    for digit in digits:
        sumdigits += int(digit) ** 5
    if sumdigits == number:
        answer += number
print(answer)
