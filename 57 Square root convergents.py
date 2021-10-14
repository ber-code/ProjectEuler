def square_root_convergents(iters):
    previous_numerator, previous_denominator, numerator, denominator = 1, 1, 3, 2
    loop, ret = 1, 0
    while loop <= iters:
        if len(str(numerator)) > len(str(denominator)):
            ret += 1
        test_numerator, test_denominator = int(numerator), int(denominator)
        numerator = numerator * 2 + previous_numerator
        denominator = denominator * 2 + previous_denominator
        previous_numerator, previous_denominator = test_numerator, test_denominator
        loop += 1
    return ret


print(square_root_convergents(1000))
