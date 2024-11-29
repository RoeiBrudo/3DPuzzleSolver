

def translate_arr_to_dict(puzzle_config, arr_repr):
    dict_repr = {}
    for c, ind in puzzle_config.pieces_to_ind_repr.items():
        true_ind = [arr_repr[i - 1] for i in ind]
        dict_repr[c] = [puzzle_config.solved_states['arr'][t_i - 1] for t_i in true_ind]

    return dict_repr


class PuzzleInstance:
    def __init__(self, puzzle_config, state=None):
        self.puzzle_config = puzzle_config
        self.state = state if state else self.puzzle_config.solved_states['arr']


    def __str__(self):
        s = 'State \n'
        s += 'Array Repr: '
        s += str(self.state)
        s += '\nDict Repr: '
        s += str(translate_arr_to_dict(self.puzzle_config, self.state))
        return s

    def move(self, move_str):

        new_arr_repr = [None] * len(self.state)

        move_f = self.puzzle_config.moves[move_str]
        for i, s in enumerate(self.state):
            new_ind = move_f(i + 1) - 1
            new_arr_repr[new_ind] = s

        self.state = new_arr_repr





# def translate_dict_to_arr(self, dict_repr):
#     # solved = self.cube_config.get_solved_state_array()
#     # state = [f"x_{i}" for i in solved]
#     # for hosts_cubie, hosts_ind in self.cube_config.get_corners_cubies_ind_mapping().items():
#     #     target_cubie_permuted = dict_repr[hosts_cubie].upper()
#     #     for target_cubie_true, true_cubie_ind in dict_repr.items():
#     #         is_perm, perm = get_perm(target_cubie_permuted, target_cubie_true)
#     #
#     #         if is_perm:
#     #             targets_ind = [self.cube_config.get_corners_cubies_ind_mapping()[target_cubie_true][p] for p in perm]
#     #             for host_ind, target_ind in zip(hosts_ind, targets_ind):
#     #                 state[host_ind - 1] = target_ind
#
#
#     return []

