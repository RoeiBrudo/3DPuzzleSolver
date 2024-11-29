from cubes.cube_2x2x2.config import PIECES, C2_PUZZLE_CONFIG
from core.algorithms.algorithm import AlgorithmConfig


ALL_CORNERS = list(PIECES['corners'])



CORRECT_PIECES = []
PLACED_PIECES = []
ALG_1_CONFIG = AlgorithmConfig(CORRECT_PIECES, PLACED_PIECES, C2_PUZZLE_CONFIG)

