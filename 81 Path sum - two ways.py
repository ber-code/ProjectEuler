f = open("81_matrix.txt", "r")
matrix = []
for line in f:
    matrix.append([int(ele) for ele in line.strip(" /n/t").split(",")])
f.close()


num_rows = len(matrix)
for idx in range(1, num_rows):
    matrix[0][idx] += matrix[0][idx - 1]
    matrix[idx][0] += matrix[idx - 1][0]
for row in range(1, num_rows):
    for idx in range(1, num_rows):
        matrix[row][idx] += min(matrix[row - 1][idx], matrix[row][idx - 1])
print(matrix[-1][-1])
