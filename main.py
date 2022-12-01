# Scripts
from board import *
from constants import *
from random_board import *

# Modules
import time

game_options = []
while len(game_options) <= 81:
    game_options.append("")

av_options = []


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
              "Example:\n")

    select_name()


def select_name():
        global name_p1
        name_p1 = input("\n"
                        "Player 1 please enter your name: ")
        if name_p1 == "":
            name_p1 = "Mysterious Guy"
        else:
            pass
            # insert_player_name(name_p1)

        print(f"\n"
              f"Hello {name_p1}!")

        select_game_mode()


def select_game_mode():
    global game_mode
    game_mode = input("\n"
                      "Please select the game mode:\n"
                      "1- Easy\n" # 41 faltantes
                      "2- Medium\n"
                      "3- Hard\n")

    if game_mode not in ["1", "2", "3"]:
        print("Please select a valid option ")
        select_game_mode()
    else:
        create_board(game_mode)


def create_board(difficulty):
    if difficulty == "1":
        pass

    print(board.format(*game_options))
    play_player()


def play_player():
    p_choice = input("\n"
                     f"Choose an empty cell from the grid {av_options}: ")

    if p_choice in av_options:
        pass
        '''
        av_options.remove(p_choice)
        game_options.pop(int(p_choice) - 1)
        game_options.insert(int(p_choice) - 1, )'''
    else:
        print("Please select a valid option ")
        play_player()

    time.sleep(0.1)
    print(board.format(*game_options))

    play_player()


if __name__ == '__main__':
    start()


