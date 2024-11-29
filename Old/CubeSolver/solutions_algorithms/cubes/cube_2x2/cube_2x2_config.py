from copy import deepcopy

from itertools import product

from sage.all import SymmetricGroup
from core.infra.cube_config import CubeConfig
from core.infra.cube_state import CubeState

########### Array Notation


S24 = SymmetricGroup(24)
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
SOLVED_STATE_ARRAY = [i for i in range(1, 25)]


########### Dict Notation


ALL_CUBIES_GROUPS = {'corners': ['DRB', 'DLF', 'DLB', 'DRF', 'URF', 'URB', 'ULF', 'ULB']}
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
SOLVED_CORNERS_ARR = "uuuullllffffrrrrbbbbdddd"
CORNERS_CUBIES_IND_MAPPING = {
    "ULB": [1, 5, 18],
    "ULF": [3, 6, 9],
    "URB": [2, 14, 17],
    "URF": [4, 13, 10],
    "DLB": [23, 7, 20],
    "DLF": [21, 8, 11],
    "DRB": [24, 16, 19],
    "DRF": [22, 15, 12],
}

_ALL_FACES = ["U", "D", "F", "B", "R", "L"]
_ALL_DIRECTIONS = ["1", "2", "'"]
ALL_MOVES = ["".join(list(p)) for p in product(_ALL_FACES, _ALL_DIRECTIONS)]


_OPPOSITE_EDGES = {
    "D": "U",
    "L": "R",
    "B": "F",
    "U": "D",
    "R": "L",
    "F": "B",

}
_OPPOSITE_DIRECTIONS = {
    "1": "'",
    "2":"2",
    "'":"1"
}


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


class Cube2x2Config(CubeConfig):

    @staticmethod
    def get_solved_state_array():
        return SOLVED_STATE_ARRAY

    @staticmethod
    def get_solved_targets_arr():
        return SOLVED_CORNERS_ARR

    @staticmethod
    def get_corners_cubies_ind_mapping():
        return CORNERS_CUBIES_IND_MAPPING

    @staticmethod
    def get_cube_group():
        return RC2

    @staticmethod
    def get_all_cubies_groups():
        return ALL_CUBIES_GROUPS

    @staticmethod
    def move(in_state, move_str):
        cp_state = deepcopy(in_state)
        new_arr_repr = [None] * len(cp_state.arr_repr)

        move_f = get_move_by_str(move_str)
        for i, s in enumerate(cp_state.arr_repr):
            new_ind = move_f(i + 1) - 1
            new_arr_repr[new_ind] = s

        new_state = CubeState(Cube2x2Config, arr_repr=new_arr_repr)

        return new_state

    @staticmethod
    def get_next_moves(state, previous_moves):

        if not previous_moves:
            return ALL_MOVES

        previous_move = previous_moves[-1]
        possible_moves = [m for m in ALL_MOVES if m[0] != previous_move[0]]
        if previous_move[0] in _OPPOSITE_EDGES.keys():
            possible_moves = [m for m in possible_moves if m[0] != _OPPOSITE_EDGES[previous_move[0]]]

        return possible_moves

    @staticmethod
    def get_opposite_moves_sequence(moves_sequence):
        reversed_seq = []
        for s in moves_sequence[::-1]:
            opp_move = s[0] + _OPPOSITE_DIRECTIONS[s[1]]
            reversed_seq.append(opp_move)
        return reversed_seq


    def __deepcopy__(self, memodict={}):
        return Cube2x2Config

