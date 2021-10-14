def count_right_triangles(perimeter):
    ret = 0
    for a in range(1, int(perimeter / 4) + 1):
        for b in range(a, int(perimeter / 2) + 1):
            if a ** 2 + b ** 2 == (perimeter - a - b) ** 2:
                ret += 1
    return ret


answer = 0
int_solutions = 0
for i in range(1001):
    check = count_right_triangles(i)
    if check > int_solutions:
        int_solutions = check
        answer = i

print(answer)
