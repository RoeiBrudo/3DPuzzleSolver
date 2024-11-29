



class PuzzleState:
    def __init__(self, puzzle_space, solved_state_dict, pieces_to_arr_ind):
        self.puzzle_space = puzzle_space
        self.solved_state_dict = solved_state_dict
        self.pieces_to_arr_ind = pieces_to_arr_ind

    def translate_arr_to_dict(self, arr_repr):
        dict_repr = {}
        for c, ind in self.pieces_to_arr_ind.items():
            true_ind = [arr_repr[i - 1] for i in ind]
            dict_repr[c] = [self.puzzle_space.solved_state[t_i - 1] for t_i in true_ind]

        return dict_repr
