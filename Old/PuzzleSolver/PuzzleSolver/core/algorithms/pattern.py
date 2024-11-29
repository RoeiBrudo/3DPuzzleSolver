from functools import partial

def reorder_from_idx(idx, a):
    return a[idx:] + a[:idx]

def cyclic_perm(a):
    return [partial(reorder_from_idx, i) for i in range(len(a))]



class Pattern:
    def __init__(self, correct_pieces, placed_pieces, puzzle_config):
        self.correct_pieces = correct_pieces
        self.placed_pieces = placed_pieces
        self.puzzle_config = puzzle_config

        self.base_dict = {}
        for correct_piece in self.correct_pieces:
            self.base_dict[correct_piece] = self.puzzle_config.solved_states['dict'][correct_pieces]

    def generate_states(self):
        for placed_piece in self.placed_pieces:
            l = len(self.puzzle_config.solved_states['dict'][placed_piece])
            for i in range(l):
                ...
            


