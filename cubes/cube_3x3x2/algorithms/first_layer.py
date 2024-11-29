from cubes.cube_2x2x2.state import SOLVED_STATE_DICT

BASE_PATTERN = {
    'URF': '*',
    'URB': '*',
    'ULF': '*',
    'ULB': '*',
}

START_PATTERN = {
    'DRF': '*',
    'DRB': 'drb',
    'DLF': 'dlf',
    'DLB': 'dlb',
}


END_PATTERN = {
    'DRF': 'drf',
    'DRB': 'drb',
    'DLF': 'dlf',
    'DLB': 'dlb',
}

START_PATTERN.update(BASE_PATTERN)
END_PATTERN.update(BASE_PATTERN)

SUBPATTERN = []

