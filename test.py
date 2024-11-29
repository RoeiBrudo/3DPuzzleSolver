
from core.puzzle.space import PuzzleSpace
from core.puzzle.cubie_repr import CubiePuzzleRepresentation
from core.puzzle.puzzle import Puzzle

from cubes.cube_2x2x2.space import RC2, SOLVED_STATE_ARRAY, MOVES_DICT
from cubes.cube_2x2x2.state import SOLVED_STATE_DICT, PIECES, PIECES_TO_STATE_IND


puzzle_space = PuzzleSpace(RC2, SOLVED_STATE_ARRAY, MOVES_DICT)
cubie_puzzle_repr = CubiePuzzleRepresentation(PIECES, SOLVED_STATE_DICT, PIECES_TO_STATE_IND, SOLVED_STATE_ARRAY)

PuzzleObj = Puzzle(puzzle_space, cubie_puzzle_repr)
puzzle = PuzzleObj.get_instance()
print(puzzle)
puzzle.move('R1')
print(puzzle)



