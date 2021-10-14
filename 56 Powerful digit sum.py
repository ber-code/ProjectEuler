def power_digit_sum(base, power):
    def digits_sum(number):
        digit_sum = 0
        for digi in str(number):
            digit_sum += int(digi)
        return digit_sum

    def trim_ending_zeroes(number):
        while number % 10 == 0:
            number //= 10
        return number

    working_power, temp_num = 2, int(base)
    while working_power <= power:
        temp_num *= base
        trim_ending_zeroes(temp_num)
        working_power += 1

    return digits_sum(temp_num)


answer = 0
for a in range(1, 100):
    for b in range(1, 100):
        trial_sum = power_digit_sum(a, b)
        if trial_sum > answer:
            answer = trial_sum
print(answer)
