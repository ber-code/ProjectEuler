from decimal import *

getcontext().prec = 982 * 2  # only because I know the max length.
digits = range(1, 1000)
maximum = 0
answer = 0
for number in digits:
    test = str(Decimal(1) / Decimal(number))
    test = test[2:]
    lengthtest = len(test)
    halfway = lengthtest // 2
    for startpoint in range(halfway):
        for length in range(1, halfway + 1):
            if (
                test[startpoint : startpoint + length]
                == test[startpoint + length : startpoint + 2 * length]
            ):
                if length > maximum:
                    maximum = length
                    answer = number
                break
print(
    "Longest recurring string is "
    + str(maximum)
    + " digits long. The number is "
    + str(answer)
    + "."
)
