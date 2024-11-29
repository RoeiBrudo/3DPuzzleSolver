from core.infra.solution_graph import PatternTransition
from copy import deepcopy
import numpy as np


class CubeSearchGraphNode:
    def __init__(self, state_cube, cube_config):
        self.state = state_cube
        self.cube_config = cube_config

        self.path_from_root = []

    def get_match_pattern(self, patterns_dict):
        for p in patterns_dict.keys():
            is_match = patterns_dict[p].is_state_match(self.state)
            if is_match:
                return p
        return None

    def get_possible_moves(self):
        possible_moves = self.cube_config.get_next_moves(self.state, self.path_from_root)
        return possible_moves

    def move(self, move_str):

        self.state = self.cube_config.move(self.state, move_str)
        self.path_from_root.append(move_str)

    def __eq__(self, other):
        return self.state == other.state

    def __str__(self):
        out_str = ''
        out_str += 'Path From Start:\n'
        out_str += str(self.path_from_root) + '\n'
        out_str += 'State\n'
        out_str += str(self.state)
        return out_str



def bfs_pattern_exploration(start_node, patterns_dict, max_depth=np.inf):
    nodes_expanded = 0

    queue, visited_nodes = [start_node], []
    while queue:
        nodes_expanded += 1
        cur_node = queue.pop(0)
        match_p = cur_node.get_match_pattern(patterns_dict)

        if match_p is not None:
            yield cur_node, match_p

        if cur_node.state not in [n.state for n in visited_nodes]:
            visited_nodes.append(cur_node)

            if len(cur_node.path_from_root) < max_depth:
                possible_moves = cur_node.get_possible_moves()

                for move in possible_moves:
                    new_node = deepcopy(cur_node)
                    new_node.move(move)
                    queue.append(new_node)



def generate_edges_bfs(patterns_dict, cube_config, max_depth):
    for pattern_name in list(patterns_dict.keys()):
        print(f"bfs for node {pattern_name}")
        start_node = CubeSearchGraphNode(patterns_dict[pattern_name].states[0], cube_config)
        generator = bfs_pattern_exploration(start_node, patterns_dict, max_depth)
        for (node, match_pattern_name) in generator:
            edges = []
            if pattern_name != match_pattern_name:
                if pattern_name != 'T':
                    edges.append(PatternTransition(pattern_name, match_pattern_name, node.path_from_root))

                if match_pattern_name != 'T':
                    edges.append(PatternTransition(match_pattern_name, pattern_name,
                                                   cube_config.get_opposite_moves_sequence(node.path_from_root)))

            if len(edges) != 0:
                yield edges