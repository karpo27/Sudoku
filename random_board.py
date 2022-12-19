# Scripts
from constants import *

# Modules
from random import sample


# pattern for a baseline valid solution
def pattern(r, c):
    return (BASE * (r % BASE) + r // BASE + c) % SIDE


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s):
    return sample(s, len(s))


def produce_random_board():
    rows = [g * BASE + r for g in shuffle(R_BASE) for r in shuffle(R_BASE)]
    cols = [g * BASE + c for g in shuffle(R_BASE) for c in shuffle(R_BASE)]
    nums = shuffle(range(1, BASE * BASE + 1))

    # produce board using randomized baseline pattern
    random_board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    empties = SQUARES * 3 // 4   # Remove 60 squares

    for i in sample(range(SQUARES), empties):
        random_board[i // SIDE][i % SIDE] = 0

    num_size = len(str(SIDE))
    for line in random_board:
        print(*(f"{n or '.':{num_size}} " for n in line))


produce_random_board()

