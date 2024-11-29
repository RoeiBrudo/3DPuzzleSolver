from dataclasses import dataclass
from typing import Any



class AlgorithmConfig:
    def __init__(self, correct_pieces, placed_pieces, puzzle_config):
        self.correct_pieces = correct_pieces
        self.placed_pieces = placed_pieces
        self.puzzle_config = puzzle_config

        self.base_pattern = ...


    def generate_mid_patterns(self):
        ...
        # for placed_piece in self.placed_pieces:
            # placed_piece_correct = self.
            # for orientations in range(len()):
            #     ...








"""
        # self.start_pattern = start_pattern
        # self.end_pattern = end_pattern
        # self.changed_pieces = [k for k in end_pattern.keys()
        #                        if end_pattern[k] != start_pattern[k]]
        # self.fixed_pieces = [k for k in end_pattern.keys()
        #                      if end_pattern[k] == start_pattern[k] and start_pattern[k] != '*']
        # self.free_pieces = [k for k in end_pattern.keys()
        #                     if end_pattern[k] == start_pattern[k] and start_pattern[k] == '*']

        # print(self.start_pattern)
        # print(self.end_pattern)
        # print(self.changed_pieces)
        # print(self.free_pieces)
        # print(self.fixed_pieces)

"""