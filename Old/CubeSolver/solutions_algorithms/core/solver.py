import os
from core.infra.solution_graph import PatternNode, PatternGraph
from core.infra.patterns import CubeMetaPattern
from core.search import generate_edges_bfs
from files_io import read_pickle, write_pickle


def explore_meta_pattern(cube_config, alg_config):
    meta_pattern = CubeMetaPattern(cube_config, alg_config)
    for i, sub_pattern in enumerate(meta_pattern.generate_sub_patterns()):
        states = [s for s in sub_pattern.generate_states()]
        if len(states) != 0:
            sub_pattern.states = states
            meta_pattern.sub_patterns[sub_pattern.name] = sub_pattern

        print('subpattern', i, len(states))

    return meta_pattern




def generate_edges(patterns_dict, cube_config, method, max_depth):
    if method == 'bfs':
        for e_list in generate_edges_bfs(patterns_dict, cube_config, max_depth):
            yield e_list

    elif method == 'generate_moves':
        ...
    else:
        raise NotImplemented




def generate_solution_graph(patterns_dict, cube_config, method, max_depth, main_solution_path):
    edge_pkl_path = os.path.join(main_solution_path, f'pattern_transitions_{method}_{max_depth}.pkl')
    try:
        E =  read_pickle(edge_pkl_path)
    except FileNotFoundError:
        E = []
        for e_list in generate_edges(patterns_dict, cube_config, method, max_depth):
            E.extend(e_list)
        write_pickle(E, edge_pkl_path)

    V = [PatternNode(v, pattern) for v, pattern in patterns_dict.items()]

    pattern_graph = PatternGraph(V, E)
    for solution_graph, ind in pattern_graph.get_solutions():
        yield solution_graph, ind

