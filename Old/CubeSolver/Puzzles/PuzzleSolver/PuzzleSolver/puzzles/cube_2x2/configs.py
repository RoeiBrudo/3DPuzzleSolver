from itertools import product


_CORNERS = ['DRB', 'DLF', 'DLB', 'DRF', 'URF', 'URB', 'ULF', 'ULB']
_FACES = ["U", "D", "F", "B", "R", "L"]
_DIRECTIONS = ["1", "2", "'"]


PIECES = {'corners': _CORNERS}
MOVES = ["".join(list(p)) for p in product(_FACES, _DIRECTIONS)]

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


def move_u(state):
    ...


# def move_d(state):
#     ...


def move(state, move):
    ...


