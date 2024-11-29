from dataclasses import dataclass
from typing import Any

@dataclass
class PuzzleArrayConfig:
    group: Any
    actions: Any
    solved_state: Any


@dataclass
class PuzzleDictConfig:
    pieces: Any
    solved_state: Any



class PuzzleConfig:

    def __init__(self, array_config, dict_config, pieces_to_ind_repr, moves):
        self.array_config = array_config
        self.dict_config = dict_config
        self.pieces_to_ind_repr = pieces_to_ind_repr

        self.solved_states = {'arr': self.array_config.solved_state,
                              'dict': self.dict_config.solved_state}

        self.moves = moves


    def __str__(self):
        s = 'Solved State'
        s += 'Array Repr:'
        s += str(self.solved_states['arr'])
        s += ' \nDict Repr '
        s += str(self.solved_states['dict'])

        return s
