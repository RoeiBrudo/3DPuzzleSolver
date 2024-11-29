from copy import deepcopy
from sage.all import Permutation

from core.utils import get_perm


class CubeState:
    def __init__(self, cube_config, **kwargs):
        self.cube_config = cube_config

        if 'arr_repr' in kwargs.keys():
            self.arr_repr = kwargs['arr_repr']
            self.dict_repr = self.translate_arr_to_dict(self.arr_repr)

        elif 'dict_repr' in kwargs.keys():
            self.dict_repr = kwargs['dict_repr']
            self.arr_repr = self.translate_dict_to_arr(self.dict_repr)

        else:
            self.arr_repr = self.cube_config.get_solved_state_array()
            self.dict_repr = self.translate_arr_to_dict(self.arr_repr)

    def is_legal_state(self):
        return Permutation(self.arr_repr) in self.cube_config.get_cube_group()

    def set(self, **kwargs):
        if 'arr_repr' in kwargs.keys():
            self.arr_repr = kwargs['arr_repr']
            self.dict_repr = self.translate_arr_to_dict(self.arr_repr)

        elif 'dict_repr' in kwargs.keys():
            self.dict_repr = kwargs['dict_repr']
            self.arr_repr = self.translate_dict_to_arr(self.dict_repr)

    def __repr__(self):
        s = f"arr_repr:\n{self.arr_repr} \ndict_repr:\n"
        for c in self.dict_repr:
            s += f"{c}: {self.dict_repr[c]}\n"
        return s[:-1]

    def __deepcopy__(self, memodict={}):
        return CubeState(deepcopy(self.cube_config), arr_repr=deepcopy(self.arr_repr), dict_repr=deepcopy(self.dict_repr))


    def translate_arr_to_dict(self, arr_repr):
        dict_repr = {}
        for c, ind in self.cube_config.get_corners_cubies_ind_mapping().items():
            true_ind = [arr_repr[i - 1] for i in ind]
            dict_repr[c] = ''.join([self.cube_config.get_solved_targets_arr()[t_i - 1] for t_i in true_ind])

        return dict_repr

    def translate_dict_to_arr(self, dict_repr):
        solved = self.cube_config.get_solved_state_array()
        state = [f"x_{i}" for i in solved]
        for hosts_cubie, hosts_ind in self.cube_config.get_corners_cubies_ind_mapping().items():
            target_cubie_permuted = dict_repr[hosts_cubie].upper()
            for target_cubie_true, true_cubie_ind in dict_repr.items():
                is_perm, perm = get_perm(target_cubie_permuted, target_cubie_true)

                if is_perm:
                    targets_ind = [self.cube_config.get_corners_cubies_ind_mapping()[target_cubie_true][p] for p in perm]
                    for host_ind, target_ind in zip(hosts_ind, targets_ind):
                        state[host_ind - 1] = target_ind

        return state



