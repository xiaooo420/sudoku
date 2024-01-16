import time


def find_empty(board: list[list[int]]) -> list:
    empty_cell = []
    for row, cells in enumerate(board):
        for col, cell in enumerate(cells):
            if cell == 0:
                empty_cell.append((row, col))
    return empty_cell


def get_possible_number(board: list[list[int]], cell: list) -> list:
    full_number = [cell for cell in range(0, 10)]
    miss_number = []
    for cell_row, cell_col in cell:
        board_row = board[cell_row]
        board_col = [board[row][cell_col] for row in range(len(board))]
        board_block = [board[row][col] for row in range((cell_row // 3) * 3, (cell_row // 3) * 3 + 3)
                       for col in range((cell_col // 3) * 3, (cell_col // 3) * 3 + 3)]
        miss_cell_number = [cell for cell in full_number if cell not in board_row+board_col+board_block]
        miss_number.append(miss_cell_number)
    return miss_number


def solver(board: list[list[int]]) -> bool:
    cell = find_empty(board)
    choices = get_possible_number(board, cell)
    len_choices = [len(choice) for choice in choices]
    try:
        min_pos = len_choices.index(min(len_choices))
        for choice in choices[min_pos]:
            board[cell[min_pos][0]][cell[min_pos][1]] = choice
            is_solver = solver(board)
            if is_solver:
                return True
        board[cell[min_pos][0]][cell[min_pos][1]] = 0
        return False
    except ValueError:
        return True


def print_table(table: list[list]) -> None:
    for row in table:
        for cell in row:
            print(f"{cell} | ", end="")
        print("\t")


def main():
    tic = time.perf_counter_ns()
    board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
             [6, 0, 0, 1, 9, 5, 0, 0, 0],
             [0, 9, 8, 0, 0, 0, 0, 6, 0],
             [8, 0, 0, 0, 6, 0, 0, 0, 3],
             [4, 0, 0, 8, 0, 3, 0, 0, 1],
             [7, 0, 0, 0, 2, 0, 0, 0, 6],
             [0, 6, 0, 0, 0, 0, 2, 8, 0],
             [0, 0, 0, 4, 1, 9, 0, 0, 5],
             [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solver(board)
    toc = time.perf_counter_ns()
    print_table(board)
    print(toc-tic)
    pass


if __name__ == "__main__":
    main()
