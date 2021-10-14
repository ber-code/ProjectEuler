def mirror(num):
    num = str(num)
    num = num[::-1]
    return num


def double_base_below(cap):
    ret = 0
    for i in range(cap):
        if i == int(mirror(i)):
            binary_string = "{0:b}".format(i)
            if binary_string == mirror(binary_string):
                ret += i
        i += 1
    return ret


print(double_base_below(1000000))
