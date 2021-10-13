factorial = 1
factorial_sum = 0
for i in range(1, 101):
    factorial *= i
for character in str(factorial):
    factorial_sum += int(character)
print(factorial_sum)
