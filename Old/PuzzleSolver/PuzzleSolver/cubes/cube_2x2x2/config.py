from itertools import product
from sage.all import SymmetricGroup

from core.puzzle.puzzle import PuzzleArrayConfig, PuzzleDictConfig, PuzzleConfig


########### Array Notation


S24 = SymmetricGroup(24)
SOLVED_STATE_ARRAY = [i for i in range(1, 25)]

MOVES_ACTIONS = {
    "R": S24("(13, 14, 16, 15)(10, 2, 19, 22)(12, 4, 17, 24)"),
    "L": S24("(5, 6, 8, 7)(3, 11, 23, 18)(1, 9, 21, 20)"),

    "U": S24("(1, 2, 4, 3)(9, 5, 17, 13)(10, 6, 18, 14)"),
    "D": S24("(21, 22, 24, 23)(11, 15, 19, 7)(12, 16, 20, 8)"),

    "F": S24("(9, 10, 12, 11)(3, 13, 22, 8)(4, 15, 21, 6)"),
    "B": S24("(17, 18, 20, 19)(1, 7, 24, 14)(2, 5, 23, 16)")
}

RC2 = S24.subgroup([
    MOVES_ACTIONS["R"], MOVES_ACTIONS["U"], MOVES_ACTIONS["F"],
    MOVES_ACTIONS["L"], MOVES_ACTIONS["D"], MOVES_ACTIONS["B"]
])


########### Dict Notation
_CORNERS = ['RB', 'LF', 'LB', 'RF']

PIECES = {'corners': _CORNERS}


SOLVED_STATE_DICT = {
    'URF': 'urf',
    'URB': 'urb',
    'ULF': 'ulf',
    'ULB': 'ulb',

    'DRF': 'drf',
    'DRB': 'drb',
    'DLF': 'dlf',
    'DLB': 'dlb',
}


########### Notation transitions



PIECES_TO_STATE_IND = {
    "ULB": [1, 5, 18],
    "ULF": [3, 6, 9],
    "URB": [2, 14, 17],
    "URF": [4, 13, 10],
    "DLB": [23, 7, 20],
    "DLF": [21, 8, 11],
    "DRB": [24, 16, 19],
    "DRF": [22, 15, 12],
}


########### Moves


_FACES = ["U", "D", "F", "B", "R", "L"]
_DIRECTIONS = ["1", "2", "'"]

def get_move_by_str(move_str):
    move_edge, move_direction = move_str[0], move_str[1]
    move_raw = MOVES_ACTIONS[move_edge]
    if move_direction == "1":
        move = move_raw
    elif move_direction == "2":
        move = move_raw * move_raw
    elif move_direction == "'":
        move = move_raw.inverse()
    else:
        raise NotImplemented

    return move

MOVES_DICT = {m: get_move_by_str(m) for m in ["".join(list(p)) for p in product(_FACES, _DIRECTIONS)]}


C2_array_repr = PuzzleArrayConfig(RC2, MOVES_ACTIONS, SOLVED_STATE_ARRAY)
C2_dict_repr = PuzzleDictConfig(PIECES, SOLVED_STATE_DICT)
C2_PUZZLE_CONFIG = PuzzleConfig(C2_array_repr, C2_dict_repr, PIECES_TO_STATE_IND, MOVES_DICT)


