f = open("96_sudoku.txt", "r")
sudokus = []
for idx, line in enumerate(f):
    if idx % 10 != 0:
        new_line = str(line.strip(" \n\t"))
        sudokus.append([int(char) for char in new_line])


def solver(sudoku):
    row_dict, col_dict, square_dict = {}, {}, {}
    unvisited = []
    ret = 0
    for idx in range(9):
        row_dict[idx], col_dict[idx], square_dict[idx] = set(), set(), set()
        for col in range(9):
            unvisited.append((idx, col))

    for row_idx, row in enumerate(sudoku):
        for col_idx, num in enumerate(row):
            if num:
                unvisited.remove((row_idx, col_idx))
                row_dict[row_idx].add(num)
                col_dict[col_idx].add(num)
                square_dict[3 * (row_idx // 3) + col_idx // 3].add(num)

    def brute(unvisited):
        nonlocal ret

        def can_be(cord):
            return (
                num not in row_dict[cord[0]]
                and num not in col_dict[cord[1]]
                and num not in square_dict[3 * (cord[0] // 3) + cord[1] // 3]
            )

        def update():
            sudoku[unvisited[0][0]][unvisited[0][1]] = num
            row_dict[unvisited[0][0]].add(num)
            col_dict[unvisited[0][1]].add(num)
            square_dict[3 * (unvisited[0][0] // 3) + unvisited[0][1] // 3].add(num)

        def undo_update():
            sudoku[unvisited[0][0]][unvisited[0][1]] = 0
            row_dict[unvisited[0][0]].remove(num)
            col_dict[unvisited[0][1]].remove(num)
            square_dict[3 * (unvisited[0][0] // 3) + unvisited[0][1] // 3].remove(num)

        if not unvisited:
            ret += 100 * sudoku[0][0] + 10 * sudoku[0][1] + sudoku[0][2]
            return

        for num in range(1, 10):
            if can_be(unvisited[0]):
                update()
                brute(unvisited[1:])
                undo_update()

        return ret

    return brute(unvisited)


answer = 0
for idx in range(50):
    sudoku = sudokus[9 * idx : (idx + 1) * 9]
    answer += solver(sudoku)
print(answer)
