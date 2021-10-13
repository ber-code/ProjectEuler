def number_spiral_sum(size):
    lastnumber = (size - 1) ** 2
    corner_value, answer, increment = 1, 1, 2
    while corner_value <= lastnumber:
        for corner in range(1, 5):
            corner_value += increment
            answer += corner_value
        increment += 2
    print(answer)


number_spiral_sum(1001)
