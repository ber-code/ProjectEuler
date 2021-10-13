def factorial(number):
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    return factorial


def digi_fact_sum(number):
    ret = 0
    while number != 0:
        ret += factorial(number % 10)
        number //= 10
    return ret


answer = 0
for candidate in range(3, 2540161):  # 2540160 natural maximum 9!*7
    if candidate == digi_fact_sum(candidate):
        answer += candidate

print(answer)
