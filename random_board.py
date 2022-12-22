# Scripts
from constants import *
from board import *

# Modules
from random import sample


# Pattern for a baseline valid solution
def pattern(r, c):
    return (BASE * (r % BASE) + r // BASE + c) % SIDE


# Randomize rows, columns and numbers (of valid base pattern)
def shuffle(s):
    return sample(s, len(s))


def produce_random_board(game_mode):
    rows = [g * BASE + r for g in shuffle(R_BASE) for r in shuffle(R_BASE)]
    cols = [g * BASE + c for g in shuffle(R_BASE) for c in shuffle(R_BASE)]
    nums = shuffle(range(1, BASE * BASE + 1))

    # Produce board using randomized baseline pattern
    random_board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    if game_mode == "1":
        empties = SQUARES * 2 // 4  # Remove 40 squares
    elif game_mode == "2":
        empties = SQUARES * 2 // 3  # Remove 54 squares
    else:
        empties = SQUARES * 3 // 4   # Remove 60 squares

    for i in sample(range(SQUARES), empties):
        random_board[i // SIDE][i % SIDE] = 0

    random_board_list = []
    for i in range(len(random_board)):
        for j in range(len(random_board[i])):
            if random_board[i][j] == 0:
                random_board_list.append(" ")
            else:
                random_board_list.append(str(random_board[i][j]))

    return random_board_list
