ret = 0
for number in range(1001):
    ret += (number ** number) % 10 ** 10
    ret %= 10 ** 10
print(ret)
