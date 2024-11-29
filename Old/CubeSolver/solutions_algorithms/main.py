import os

from files_io import read_pickle, write_pickle
from core.solver import explore_meta_pattern, generate_solution_graph
from viz.inner_viz import visualize_graph


from cubes.cube_2x2.cube_2x2_config import Cube2x2Config
from cubes.cube_2x2.algorithms_config import Alg1MetaPatternConfig

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def get_meta_pattern(main_solution_path, cube_config, alg_config):
    initial_patterns_pkl_path = os.path.join(main_solution_path, 'initial_patterns.pkl')

    try:
        return read_pickle(initial_patterns_pkl_path)
    except FileNotFoundError as e:
        print('Creating meta pattern...')

    meta_pattern = explore_meta_pattern(cube_config, alg_config)
    write_pickle(meta_pattern, initial_patterns_pkl_path)

    return meta_pattern



def get_solutions(main_solution_path, meta_pattern, cube_config, alg_config, visualize):
    solutions_graph_pkl_path = os.path.join(main_solution_path, 'solutions_graphs.pkl')

    try:
        return read_pickle(solutions_graph_pkl_path)
    except FileNotFoundError as e:
        print('generating solution...')

    solutions = {}
    i = 0
    for sol, ind in generate_solution_graph(meta_pattern.sub_patterns, cube_config, alg_config['search_alg'], alg_config['depth'], main_solution_path):
        if sol not in solutions.values():
            i += 1
            solutions[ind] = sol
            print(i, ind, sol.score)

        write_pickle(solutions, solutions_graph_pkl_path)

        ind_s = '_'.join([str(i) for i in ind])
        if visualize:
            visualize_graph(sol, os.path.join(main_solution_path,'graphs_images', f'algorithm_graph_{ind_s}.jpg'))

    return solutions


def main(cube_config, alg_config, solution_path):

    meta_pattern = get_meta_pattern(solution_path, cube_config, alg_config)
    solutions = get_solutions(solution_path, meta_pattern, cube_config, alg_config, visualize=True)

if __name__ == '__main__':
    alg_solution_path = os.path.join('results', 'cube_2x2', 'alg1')
    os.makedirs(alg_solution_path, exist_ok=True)
    os.makedirs(os.path.join(alg_solution_path, 'graphs_images'), exist_ok=True)

    # p = os.path.join(main_solution_path, 'graphs_images')
    # os.makedirs(p, exist_ok=True)

    main(Cube2x2Config, Alg1MetaPatternConfig, alg_solution_path)



