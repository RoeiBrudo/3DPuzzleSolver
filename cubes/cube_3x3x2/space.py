from itertools import product
from sage.all import SymmetricGroup


S42 = SymmetricGroup(42)
SOLVED_STATE_ARRAY = [i for i in range(1, 43)]

MOVES_ACTIONS = {
    "R": S42("(13, 14, 16, 15)(10, 2, 19, 22)(12, 4, 17, 24)"),
    "L": S42("(5, 6, 8, 7)(3, 11, 23, 18)(1, 9, 21, 20)"),

    "U": S42("(1, 2, 4, 3)(9, 5, 17, 13)(10, 6, 18, 14)"),
    "D": S42("(21, 22, 24, 23)(11, 15, 19, 7)(12, 16, 20, 8)"),

    "F": S42("(9, 10, 12, 11)(3, 13, 22, 8)(4, 15, 21, 6)"),
    "B": S42("(17, 18, 20, 19)(1, 7, 24, 14)(2, 5, 23, 16)")
}

RC2 = S42.subgroup([
    MOVES_ACTIONS["R"], MOVES_ACTIONS["U"], MOVES_ACTIONS["F"],
    MOVES_ACTIONS["L"], MOVES_ACTIONS["D"], MOVES_ACTIONS["B"]
])


def group_move_from_move_str(move_str):
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

_FACES = ["U", "D", "F", "B", "R", "L"]
_DIRECTIONS = ["1", "2", "'"]

MOVES_DICT = {m: group_move_from_move_str(m) for m in ["".join(list(p)) for p in product(_FACES, _DIRECTIONS)]}
