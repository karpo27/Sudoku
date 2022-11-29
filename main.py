# Scripts
from board import *


def start():
    print("\n"
          "Welcome to Sudoku game!\n"
          "")
    rules = input("If you already know the rules press any key to continue, otherwise type 'help'. ")

    if rules in ['help', 'HELP', 'Help']:
        print("\n"
              "1. Sudoku is a 9-by-9 grid puzzle in which the grid is divided into 3-by-3 boxes.\n"
              "2. Every row, column and box must contain the numbers one (1) through nine (9), no repeats.\n"
              "3. Most sudoku puzzles come with a few of the boxes already filled in, so you can use those freebie "
              "clues as a jumping off point for solving and work backwards.\n"
              "The fewer numbers already filled in, the more difficult it will be.\n"
              "4. The only hard and fast rule is not to repeat numbers:\n"
              "» Each row should have numbers 1-9, no repeats.\n"
              "» Each column should have numbers 1-9, no repeats.\n"
              "» Each 3x3 box should have numbers 1-9, no repeats.\n"
              "5. For playing you must follow this order:\n"
              "You can choose every box with numbers 1-9.\n"
              f"{example_board_box}"
              "And every cell with numbers 1-9, then selecting which number you want yo put in each cell.\n"
              f"{example_board_grid * 3}")


if __name__ == '__main__':
    start()

a = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(board.format("1", "2", "3", "4", "5", "6", "7", "8", "9"))
