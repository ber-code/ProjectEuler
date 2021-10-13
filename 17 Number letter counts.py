single_digits = [
    len("one"),
    len("two"),
    len("three"),
    len("four"),
    len("five"),
    len("six"),
    len("seven"),
    len("eight"),
    len("nine"),
]
teens = [
    len("ten"),
    len("eleven"),
    len("twelve"),
    len("thirteen"),
    len("fourteen"),
    len("fifteen"),
    len("sixteen"),
    len("seventeen"),
    len("eighteen"),
    len("nineteen"),
]
tens = [
    len("twenty"),
    len("thirty"),
    len("forty"),
    len("fifty"),
    len("sixty"),
    len("seventy"),
    len("eighty"),
    len("ninety"),
]
hundreds = len("hundred")
thousands = len("thousand")
and_ = len("and")


def letter_count(n):
    count = 0
    if n in range(1, 10):
        count += single_digits[n - 1]
        return count
    if n in range(10, 20):
        count += teens[n - 10]
        return count
    if n in range(20, 100):
        j = n // 10
        if j in range(2, 10):
            count += tens[j - 2]
            n -= 10 * j
            if n in range(1, 10):
                count += single_digits[n - 1]
        return count
    if n in range(100, 1000):
        k = n // 100
        count += single_digits[k - 1] + hundreds
        n = n - 100 * k
        if n in range(1, 10):
            count += single_digits[n - 1] + and_
        if n in range(10, 20):
            count += teens[n - 10] + and_
        if n in range(20, 100):
            j = n // 10
            count += and_ + tens[j - 2]
            n = n - 10 * j
            if n > 0:
                count += single_digits[n - 1]
        return count
    if n == 1000:
        count += 3 + thousands
        return count


answer = 0
for i in range(1, 1001):
    answer += letter_count(i)
print(answer)
