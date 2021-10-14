f = open("81_matrix.txt", "r")
matrix = []
for line in f:
    matrix.append([int(ele) for ele in line.split(",")])
f.close()


def dp(row, col):
    def get_val(row, col):
        if row in range(len(matrix)):
            return matrix[row][col]
        return float("inf")

    yes_dp = min(get_val(row - 1, col), get_val(row, col + 1))
    no_dp = get_val(row + 1, col)
    if yes_dp <= no_dp:
        matrix[row][col] += yes_dp
    else:
        temp_row = row + 1
        while no_dp < yes_dp:
            down, right = get_val(temp_row + 1, col), get_val(temp_row, col + 1)
            yes_dp = min(yes_dp, no_dp + right)
            if right <= down:
                no_dp += right
                matrix[row][col] += min(no_dp, yes_dp)
                return
            no_dp += down
            temp_row += 1
        matrix[row][col] += yes_dp


for col in reversed(range(len(matrix[0]) - 1)):
    for row in range(len(matrix)):
        dp(row, col)

print(min([row[0] for row in matrix]))
