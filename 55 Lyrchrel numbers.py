def reverse_add(num):
    return num + int((str(num))[::-1])


def is_palindrome(num):
    return num == int((str(num))[::-1])


answer = 0
for num in range(10001):
    check = reverse_add(num)
    test = 1
    while not is_palindrome(check) and test < 51:
        check = reverse_add(check)
        test += 1
    if test == 51:
        answer += 1

print(answer)
