def sum_of_digits(number):
    text = str(number)
    answer = 0
    for character in text:
        answer += int(character)
    return answer


print(sum_of_digits(2 ** 1000))
