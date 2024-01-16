#table = list[list]
import argparse
from copy import copy, deepcopy


def set_table(table: list[list]) -> None:
    table[0][0] = 4
    table[0][3] = 1
    table[0][4] = 5
    table[0][5] = 7
    table[0][7] = 3
    table[0][8] = 2
    table[1][0] = 2
    table[1][8] = 5
    table[2][2] = 3
    table[2][6] = 1
    table[2][7] = 9
    table[3][0] = 5
    table[3][6] = 9
    table[4][2] = 9
    table[4][4] = 3
    table[4][5] = 1
    table[4][6] = 2
    table[4][7] = 5
    table[4][8] = 7
    table[5][0] = 8
    table[5][3] = 5
    table[5][4] = 4
    table[5][7] = 1
    table[6][2] = 2
    table[6][3] = 4
    table[6][4] = 1
    table[6][5] = 5
    table[6][8] = 8
    table[7][1] = 8
    table[7][3] = 7
    table[7][4] = 6
    table[7][5] = 3
    table[7][6] = 4
    table[7][8] = 9
    table[8][3] = 9
    table[8][4] = 2
    table[8][5] = 8
    table[8][7] = 6


def recursive_sudoku(table: list[list], row_number: int, col_number: int, val: int, insert_table: list[list],
                     miss_table_val: list[list]) -> None | bool:
    table_row = table[row_number]
    table_col = [table[row][col_number] for row in range(len(table))]
    table_block = [table[row][col] for row in range((row_number//3)*3, (row_number//3)*3+3)
                   for col in range((col_number//3)*3, (col_number//3)*3+3)]

    if row_number == 8 and 0 not in table_row:
        print("Success!")
        print_table(table)
        return True

    if insert_table[row_number][col_number]:
        new_val = miss_table_val[row_number][val]
        if new_val in table_row or new_val in table_col or new_val in table_block:
            print("Failed insertion")
            print_table(table)
            return False

        table[row_number][col_number] = new_val
        val += 1

    try:
        col_number += 1
        return recursive_sudoku(table, row_number, col_number, val, insert_table, miss_table_val)
    except IndexError:
        row_number += 1
        val = 0
        return recursive_sudoku(table, row_number, 0, val, insert_table, miss_table_val)


def print_table(table: list[list]) -> None:
    for row in table:
        for cell in row:
            print(f"{cell} | ", end="")
        print("\t")


def main():
    table = [[0]*9 for _ in range(9)]
    set_table(table)
    insert_table = [[cell == 0 for cell in row] for row in table]
    print("Row table!")
    print_table(table)

    miss_table_val = []
    full_row = [cell for cell in range(1, 10)]
    for row in range(len(table)):
        miss_row = [cell for cell in table[row] if cell != 0]
        diff_row = [cell for cell in full_row if cell not in miss_row]
        miss_table_val.append(diff_row)

    right_miss_val = [[9, 6, 8],
                      [1, 8, 3, 9, 6, 7, 4],
                      [7, 5, 2, 8, 4, 6],
                      [3, 1, 6, 7, 2, 8, 4],
                      [6, 4, 8],
                      [2, 7, 9, 6, 3],
                      [9, 6, 3, 7],
                      [1, 5, 2],
                      [3, 7, 4, 5, 1]
                      ]

    recursive_sudoku(table, 0, 0, 0, insert_table, right_miss_val)


if __name__ == "__main__":
    main()
