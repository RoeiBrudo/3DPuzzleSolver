from copy import deepcopy
from itertools import permutations, product, combinations

from core.utils import get_perm
from core.infra.cube_state import CubeState



class CubeMetaPattern:
    def __init__(self, cube_config, metta_pattern_config):

        self.cube_config = cube_config
        self.fixed_cubies_dict = metta_pattern_config['fixed_cubies_dict']
        self.COI = metta_pattern_config['coi']
        self.free_target_cubies = metta_pattern_config['free_target_cubies']

        self.all_hosts = []
        groups = cube_config.get_all_cubies_groups()
        for k in groups:
            self.all_hosts.extend(groups[k])

        self.sub_patterns = {}

    def generate_sub_patterns(self):
        free_hosts = [c for c in self.all_hosts if c not in self.fixed_cubies_dict.keys()]
        coi_targets = self.COI[0]

        if self.COI[1] == 'all':
            i = 0
            for picked_free_hosts in combinations(free_hosts, len(coi_targets)):
                for free_target_perm in permutations(coi_targets):
                    all_perms = [[p for p in permutations(c)] for c in free_target_perm]

                    for p in product(*all_perms):
                        added_fixed = {host: ''.join(p[i]) for i, host in enumerate(list(picked_free_hosts))}
                        fixed_copy = deepcopy(self.fixed_cubies_dict)
                        fixed_copy.update(added_fixed)
                        pattern = CubePattern(self.cube_config, fixed_copy, {}, self.free_target_cubies,
                                              f'S_{i}', added_fixed)

                        if pattern.is_solved_pattern():
                            pattern.name = 'T'

                        yield pattern
                        i += 1

        elif self.COI[1] == 'placement':
            i = 0
            fixed_copy = deepcopy(self.fixed_cubies_dict)

            for picked_free_hosts in combinations(free_hosts, len(coi_targets)):
                for free_target_perm in permutations(coi_targets):
                    orient_free_dict = {picked_free_host: free_target for picked_free_host, free_target in zip(picked_free_hosts, free_target_perm)}
                    pattern = CubePattern(self.cube_config, fixed_copy, orient_free_dict, self.free_target_cubies,
                                          f'S_{i}', f"perm {i}")

                    if pattern.is_solved_pattern():
                        pattern.name = 'T'

                    yield pattern
                    i += 1


class CubePattern:
    def __init__(self, cube_config, fixed_cubies, orient_free_cubie, free_targets_cubie, name, pattern_identifier):
        self.cube_config = cube_config
        self.fixed_cubies_dict = fixed_cubies
        self.orient_free_cubies_dict = orient_free_cubie
        self.free_targets_cubies_list = free_targets_cubie

        self.all_hosts = []
        groups = cube_config.get_all_cubies_groups()
        for k in groups:
            self.all_hosts.extend(groups[k])
        self.free_hosts_list = [c for c in self.all_hosts if (c not in self.fixed_cubies_dict.keys()) and (c not in self.orient_free_cubies_dict.keys())]

        self.name = name
        self.pattern_identifier = pattern_identifier

        self.states = []

    def is_solved_pattern(self):
        for host, value in self.fixed_cubies_dict.items():
            if host != value.upper():
                return False

        for host, value in self.orient_free_cubies_dict.items():
            if host != value.upper():
                return False

        return True

    def is_state_match(self, state):
        state_dict = deepcopy(state.dict_repr)
        for host in self.fixed_cubies_dict.keys():
            if self.fixed_cubies_dict[host] != state_dict[host]:
                return False

        for host in self.orient_free_cubies_dict.keys():
            is_perm, _ =  get_perm(self.orient_free_cubies_dict[host], state_dict[host])
            if not is_perm:
                return False

        return True


    def __repr__(self):
        return f"fixed: {self.fixed_cubies_dict} \n" + f"orient: {self.orient_free_cubies_dict} \n" + f"free: {self.free_targets_cubies_list}"

    def generate_states(self):
        base_state = {c: "***" for c in self.all_hosts}
        for c in self.all_hosts:
            if c in self.fixed_cubies_dict.keys():
                base_state[c] = self.fixed_cubies_dict[c]

        states = self.fill_free_cubies(base_state)
        for i, s in enumerate(states):
            state = CubeState(self.cube_config, dict_repr=s)
            if state.is_legal_state():
                yield state



    def fill_free_cubies(self, state):
        state_cp = deepcopy(state)
        for i, free_target_perm in enumerate(permutations(self.free_targets_cubies_list)):
            p_dict = {self.free_hosts_list[i]: free_target_perm[i] for i in range(len(self.free_targets_cubies_list))}
            p_dict.update(self.orient_free_cubies_dict)
            for s in CubePattern.fill_helper(state_cp, p_dict):
                yield s


    @staticmethod
    def fill_helper(state, p_dict):
        if p_dict == {}:
            yield state
        else:
            p_dict_cp = deepcopy(p_dict)

            cur_host = list(p_dict_cp.keys())[0]
            for i, p in enumerate(permutations(p_dict_cp[cur_host])):
                state_cp = deepcopy(state)
                state_cp[cur_host] = ''.join(p)
                for final_state in CubePattern.fill_helper(state_cp, {k: v for k, v in p_dict_cp.items() if k != cur_host}):
                    yield final_state




