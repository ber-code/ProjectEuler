from math import ceil

powers, exponent, check = set(), 1, 1
while check < 10:
    for base in range(check, 10):
        if len(str(base ** exponent)) == exponent:
            powers.add(base ** exponent)
    check = ceil(10 ** (exponent / (exponent + 1)))
    exponent += 1
print(len(powers))
