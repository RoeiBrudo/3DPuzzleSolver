from itertools import combinations

from core.graphs_algorithms import get_minimal_undirected_edges


class PatternTransition:
    def __init__(self, start_node, end_node, moves):
        self.start_node = start_node
        self.end_node = end_node
        self.moves = moves
        self.weight = len(moves)

    def __str__(self):
        return f'edge from {self.start_node} to {self.end_node}, moves: {self.moves}, length: {self.weight}'

    def __eq__(self, other):
        if (self.start_node == other.start_node) and (self.end_node == other.end_node) and (self.moves == other.moves):
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.start_node + self.end_node + str(self.moves))


class PatternNode:
    def __init__(self, pattern_name, pattern_obj):
        self.pattern_name = pattern_name
        self.pattern_obj = pattern_obj

    def __hash__(self):
        return hash(self.pattern_name)


class PatternGraph:
    def __init__(self, v, e_list):
        self.V = v
        self.E_pool = e_list


    def get_solutions(self):

        for edges_subset, ind in self.edges_subset_generator():
            ...

            # undirected_full_graph = generate_graph(self.V, edges_subset)
            # mst = undirected_full_graph.min_spanning_tree()
            # if mst:
            #     solution_graph = SolutionGraph(self, mst)
            #     yield solution_graph, ind


    def edges_subset_generator(self):
        T_edges_raw = [e for e in self.E_pool if e.end_node == 'T']
        non_T_edges_raw = [e for e in self.E_pool if e not in T_edges_raw]

        T_edges = get_minimal_undirected_edges(T_edges_raw)
        non_T_edges = get_minimal_undirected_edges(non_T_edges_raw)

        for i in range(1, 4):
            for j, t_comb in enumerate(combinations(T_edges, i)):
                i_j_t_edges = list(t_comb)

                i_j_non_t_edges = [e for e in non_T_edges if (e[0] in [e_i_j[0] for e_i_j in i_j_t_edges]) and (e[1] in [e_i_j[1] for e_i_j in i_j_t_edges])]
                i_j_non_t_pool = [e for e in non_T_edges if e not in i_j_non_t_edges]

                W = sorted(list(set([e[2] for e in i_j_non_t_pool])))
                for w in W:
                    i_j_non_t_others = [e for e in i_j_non_t_pool if e[2] <= w]

                    edges = i_j_t_edges + i_j_non_t_edges + i_j_non_t_others

                    yield edges, (i, j, w)


class SolutionGraph:
    def __init__(self, pattern_graph, undirected_solution_graph):
        self.V = pattern_graph.V
        self.E = []
        self.score = sum([e_triplet[2] for e_triplet in undirected_solution_graph])


    def __eq__(self, other):
        if set(self.V) != set(other.V):
            return False
        if set(self.E) != set(other.E):
            return False

        return True


