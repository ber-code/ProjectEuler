f = open("67_triangle.txt", "r")
matrix = []
for line in f:
    matrix.append([int(ele) for ele in line.strip(" \n\t").split(" ")])
f.close()

for row in reversed(range(len(matrix) - 1)):
    for idx in range(row + 1):
        matrix[row][idx] += max(matrix[row + 1][idx], matrix[row + 1][idx + 1])
print(matrix[0][0])
