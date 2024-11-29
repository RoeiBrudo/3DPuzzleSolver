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


