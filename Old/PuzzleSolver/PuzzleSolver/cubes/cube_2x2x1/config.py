from itertools import product
from sage.all import SymmetricGroup

from core.puzzle.puzzle import PuzzleArrayConfig, PuzzleDictConfig, PuzzleConfig


########### Array Notation


S16 = SymmetricGroup(16)
SOLVED_STATE_ARRAY = [i for i in range(1, 17)]

MOVES_ACTIONS = {
    "R": S16("(2, 6)(4, 8)(9, 10)"),
    "L": S16("(1, 5)(3, 7)(11, 12)"),

    "F": S16("(1, 8)(2, 7)(13, 14)"),
    "B": S16("(3, 6)(4, 5)(15, 16)")
}

RC221 = S16.subgroup([
    MOVES_ACTIONS["R"], MOVES_ACTIONS["F"],
    MOVES_ACTIONS["L"], MOVES_ACTIONS["B"]
])


########### Dict Notation
_CORNERS = ['RB', 'LF', 'LB', 'RF']

PIECES = {'corners': _CORNERS}


SOLVED_STATE_DICT = {'RB':'rbud',
                     'RF':'rfud',
                     'LF':'lfud',
                     'LB':'lbud'
                     }


########### Notation transitions



PIECES_TO_STATE_IND = {
    'RB':[10, 15, 6, 4],
    'RF':[9, 14, 8, 2],
    'LF':[12, 13, 7, 1],
    'LB':[11, 16, 5, 3]
}


########### Moves


_FACES = ["F", "B", "R", "L"]
_DIRECTIONS = ["1", "'"]

def get_move_by_str(move_str):
    move_edge, move_direction = move_str[0], move_str[1]
    move_raw = MOVES_ACTIONS[move_edge]
    if move_direction == "1":
        move = move_raw
    elif move_direction == "'":
        move = move_raw.inverse()
    else:
        raise NotImplemented

    return move

MOVES_DICT = {m: get_move_by_str(m) for m in ["".join(list(p)) for p in product(_FACES, _DIRECTIONS)]}


C221_array_repr = PuzzleArrayConfig(RC221, MOVES_ACTIONS, SOLVED_STATE_ARRAY)
C221_dict_repr = PuzzleDictConfig(PIECES, SOLVED_STATE_DICT)
C221_PUZZLE_CONFIG = PuzzleConfig(C221_array_repr, C221_dict_repr, PIECES_TO_STATE_IND, MOVES_DICT)


