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
                           "Choose a cell from the grid and select a number 1-9 to put in: ")

    p_choice_list = list(p_choice_input)
    p_choice_val = []
    for i in range(len(p_choice_list)):
        if p_choice_list[i].isdigit():
            if p_choice_list[i] != "0":
                p_choice_val.append(p_choice_list[i])

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
                position = 9 * 6 + 3 * (int(p_choice_val[0]) - 7) + (int(p_choice_val[1]) - 1)
            elif 7 <= int(p_choice_val[0]) <= 9 and 4 <= int(p_choice_val[1]) <= 6:
                position = 9 * 7 + 3 * (int(p_choice_val[0]) - 7) + (int(p_choice_val[1]) - 4)
            elif 7 <= int(p_choice_val[0]) <= 9 and 7 <= int(p_choice_val[1]) <= 9:
                position = 9 * 8 + 3 * (int(p_choice_val[0]) - 7) + (int(p_choice_val[1]) - 7)

    if av_options[position] == "X":
        print("Please select a valid option ")
        play_player()

    game.pop(position)
    game.insert(position, p_choice_val[2])

    time.sleep(0.25)
    print(board.format(*game))
    check_win()
    play_player()


def check_win():
    c_1 = 0
    c_2 = 0
    c_3 = 0

    # Row check
    for i in range(0, len(game) + 1, 9):
        if i != 0:
            check_1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for j in range(len(game[i - 9: i])):
                if game[i - 9: i][j] in check_1:
                    check_1.remove(game[i - 9: i][j])
                else:
                    c_1 += 1

    # Column check
    for k in range(len(game[: 9])):
        check_2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for z in range(0, 73, 9):
            if game[k + z] in check_2:
                check_2.remove(game[k + z])
            else:
                c_2 += 1

    # Block check
    for n in range(0, len(game) + 1, 27):
        for m in range(n, n + 9, 3):
            if m < 81:
                check_3 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                for x in range(m, m + 3):
                    for y in range(0, 19, 9):
                        if game[x + y] in check_3:
                            check_3.remove(game[x + y])
                        else:
                            c_3 += 1

    print(c_1)
    print(c_2)
    print(c_3)
    if c_1 + c_2 + c_3 == 0:
        win_message()


def win_message():
    player_win = "\n"\
                 f"Congratulations {name_p1}!, you won the game!"
    print(player_win)

    play_again()


def play_again():
    av_options.clear()

    final_choice = input("\n"
                         "Do you want yo play again?\n"
                         "1- Yes\n"
                         "2- No, thanks!\n"
                         "3- Show my score\n"
                         "")

    '''
    if final_choice == "3":
        show_data(name_p1)
        show_data(name_p2)
        play_again()
            
        else:
            if name_p1 != "Mysterious Guy":
                show_data(name_p1)
                play_again()
            elif name_p1 == "Mysterious Guy":
                print("\n"
                      "If you are playing nameless, you have no stats! ")
                play_again()
    elif final_choice == "1":
        select_game_mode()
    elif final_choice == "2":
        exit()
    else:
        print("\n"
              "Please select a valid option ")
        play_again()'''


if __name__ == '__main__':
    start()


