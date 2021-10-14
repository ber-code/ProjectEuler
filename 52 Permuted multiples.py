def permuted_digits_multiple(num, multiple):
    digi_dict = {}
    for digi in str(num):
        if digi not in digi_dict:
            digi_dict[digi] = 1
        else:
            digi_dict[digi] += 1
    for digi in str(num * multiple):
        if digi in digi_dict:
            digi_dict[digi] -= 1
            if digi_dict[digi] < 0:
                return False
        else:
            return False
    return True


check, test = 2, False
max_multiple = 6
while test == False:
    for num in range(10 ** (check - 1) + 1, 10 ** check // 6):
        count = 0
        for multiple in range(1, max_multiple + 1):
            if not permuted_digits_multiple(num, multiple):
                break
            else:
                count += 1
        if count == max_multiple:
            test = True
            print(num)
            break
    check += 1
