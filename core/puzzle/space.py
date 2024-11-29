
class PuzzleSpace:
    def __init__(self, space, solved_state, moves_dict):
        self.space = space
        self.solved_state = solved_state
        self.moves_dict = moves_dict

    def move(self, state, move_str):
        new_arr_repr = [None] * len(state)
        move_f = self.moves_dict[move_str]
        for i, s in enumerate(state):
            new_ind = move_f(i + 1) - 1
            new_arr_repr[new_ind] = s

        return new_arr_repr


