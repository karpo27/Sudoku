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
    r_base = range(BASE)
    rows = [g * BASE + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * BASE + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, BASE * BASE + 1))

    # produce board using randomized baseline pattern
    random_board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    for line in random_board:
        print(line)
