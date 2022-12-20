# Scripts
from board import *
from constants import *
from random_board import *

# Modules
import time


av_options = []
p_choice = []
for p in range(0, 81):
    p_choice.append("")


def start():
    print("\n"
          "Welcome to Sudoku game!\n"
          "")
    rules = input("If you already know the rules press any key to continue, otherwise type 'help'. ")

    if rules in ['help', 'HELP', 'Help']:
        print("\n"
              "1. Sudoku is a 9-by-9 grid puzzle in which the grid is divided into 3-by-3 boxes.\n"
              "2. Every row, column and box must contain the numbers 1 through nine 9, no repeats.\n"
              "3. Most sudoku puzzles come with a few of the boxes already filled in, so you can use those freebie "
              "clues as a jumping off point for solving and work backwards.\n"
              "The fewer numbers already filled in, the more difficult it will be.\n"
              "4. The only hard and fast rule is not to repeat numbers:\n"
              "» Each row should have numbers 1-9, no repeats.\n"
              "» Each column should have numbers 1-9, no repeats.\n"
              "» Each 3x3 box should have numbers 1-9, no repeats.\n"
              "5. For picking a number in the grid you must follow this order:\n"
              "First choose a box. Grid is divided in 1-9 boxes.\n"
              f"{example_board_box}"
              "Then choose a cell in the box. Box is divided in 1-9 cells.\n"
              f"{example_board_grid}"
              "And finally select which number 1-9 you want yo put in each cell.\n"
              "Example: 1 3 8\n"
              f"{board.format(*EXAMPLE)}")

    select_name()


def select_name():
        global name_p1
        name_p1 = input("\n"
                        "Player 1 please enter your name: ")
        if name_p1 == "":
            name_p1 = "Mysterious Guy"

        print(f"\n"
              f"Hello {name_p1}!")

        select_game_mode()


def select_game_mode():
    global game_mode
    game_mode = input("\n"
                      "Please select the game mode:\n"
                      "1- Easy\n"       # 41 empties
                      "2- Medium\n"     # 50 ?
                      "3- Hard\n")      # 60 empties

    if game_mode not in ["1", "2", "3"]:
        print("Please select a valid option ")
        select_game_mode()
    else:
        global game
        game = produce_random_board(game_mode)
        print(f"{board.format(*game)}")

        for i in range(len(game)):
            if game[i].isdigit():
                av_options.append("X")
            else:
                av_options.append(" ")

        play_player()


def play_player():
    p_choice_input = input("\n"
                           "Choose an empty cell from the grid: ")

    p_choice_list = list(p_choice_input)
    p_choice_val = []
    for i in range(len(p_choice_list)):
        if p_choice_list[i].isdigit():
            if p_choice_list[i] != "0":
                p_choice_val.append(p_choice_list[i])

    print(p_choice_val)
    if len(p_choice_val) != 3:
        print("Please select a valid option ")
        play_player()

    for i in range(len(p_choice_val)):
        if i == 0:
            # Rows 1-3:
            if 1 <= int(p_choice_val[0]) <= 3 and 1 <= int(p_choice_val[1]) <= 3:
                position = 3 * (int(p_choice_val[0]) - 1) + (int(p_choice_val[1]) - 1)
            elif 1 <= int(p_choice_val[0]) <= 3 and 4 <= int(p_choice_val[1]) <= 6:
                position = 9 + 3 * (int(p_choice_val[0]) - 1) + (int(p_choice_val[1]) - 4)
            elif 1 <= int(p_choice_val[0]) <= 3 and 7 <= int(p_choice_val[1]) <= 9:
                position = 9 * 2 + 3 * (int(p_choice_val[0]) - 1) + (int(p_choice_val[1]) - 7)

            # Rows 4-6:
            elif 4 <= int(p_choice_val[0]) <= 6 and 1 <= int(p_choice_val[1]) <= 3:
                position = 9 * 3 + 3 * (int(p_choice_val[0]) - 4) + (int(p_choice_val[1]) - 1)
            elif 4 <= int(p_choice_val[0]) <= 6 and 4 <= int(p_choice_val[1]) <= 6:
                position = 9 * 4 + 3 * (int(p_choice_val[0]) - 4) + (int(p_choice_val[1]) - 4)
            elif 4 <= int(p_choice_val[0]) <= 6 and 7 <= int(p_choice_val[1]) <= 9:
                position = 9 * 5 + 3 * (int(p_choice_val[0]) - 4) + (int(p_choice_val[1]) - 7)

            # Rows 7-9:
            elif 7 <= int(p_choice_val[0]) <= 9 and 1 <= int(p_choice_val[1]) <= 3:
                position = 9 * 3 + 3 * (int(p_choice_val[0]) - 4) + (int(p_choice_val[1]) - 1)
            elif 7 <= int(p_choice_val[0]) <= 9 and 4 <= int(p_choice_val[1]) <= 6:
                position = 9 * 4 + 3 * (int(p_choice_val[0]) - 4) + (int(p_choice_val[1]) - 4)
            elif 7 <= int(p_choice_val[0]) <= 9 and 7 <= int(p_choice_val[1]) <= 9:
                position = 9 * 5 + 3 * (int(p_choice_val[0]) - 4) + (int(p_choice_val[1]) - 7)


    print(position)
    p_choice.pop(position - 1)
    p_choice.insert(position - 1, p_choice_val[2])

    '''
    if p_choice in av_options:
        pass
        
        av_options.remove(p_choice)
        game.pop(int(p_choice) - 1)
        game.insert(int(p_choice) - 1, )
    else:
        print("Please select a valid option ")
        play_player()

    time.sleep(0.1)
    print(board.format(*game))

    play_player()'''


if __name__ == '__main__':
    start()


