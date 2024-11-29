# from collections import namedtuple
#
# from sage.graphs.graph import Graph


def get_minimal_undirected_edges(solution_edges_dict):
    temp_dict = {}
    for e_i in solution_edges_dict:
        e_key = (e_i.start_node, e_i.end_node)
        e_key_inv = (e_i.end_node, e_i.start_node)
        if (e_key in temp_dict.keys()) and (e_i.weight < temp_dict[e_key]):
            temp_dict[e_key] = e_i.weight
        elif (e_key_inv in temp_dict.keys()) and (e_i.weight < temp_dict[e_key_inv]):
            temp_dict[e_key_inv] = e_i.weight
        else:
            temp_dict[e_key] = e_i.weight

    undirected_edges = [(k[0], k[1], w) for k, w in temp_dict.items()]
    return undirected_edges











"""

# self.E = get_solution_edges_from_undirected_graph(pattern_graph.E_pool, undirected_solution_graph)

def get_solution_edges_from_undirected_graph(V, E_pool, mst):
    start_nodes = [v.pattern_name for v in V if v.pattern_name != 'T']
    solution_edges = {}

    for s in start_nodes:
        p = simple_bfs(mst, s, 'T')

        if p is None:
            return []

        for edge_tuple in p:
            edges = [e for e in E_pool if (e.start_node == edge_tuple[0]) and (e.end_node == edge_tuple[1])]
            sorted_e = sorted(edges, key=lambda x: x.weight)
            edge = sorted_e[0]
            solution_edges[(edge.start_node, edge.end_node)] = edge

    solution_edges_list = [e for e in solution_edges.values()]
    return solution_edges_list


def simple_bfs(spanning_tree_edges, start_node, end_node):
    SimpleBFSNode = namedtuple("SimpleBFSNode", "v path_from_root")

    q = [SimpleBFSNode(start_node, [])]
    visited = []
    while q:
        cur = q.pop()
        if cur.v not in visited:
            visited.append(cur.v)

            if cur.v == end_node:
                return cur.path_from_root

            neighbors = list(
                set([e[1] for e in spanning_tree_edges if e[0] == cur.v] + [e[0] for e in spanning_tree_edges if e[1] == cur.v]))
            for n in neighbors:
                p = cur.path_from_root + [(cur.v, n)]
                new_n = SimpleBFSNode(n, p)
                q.append(new_n)


def generate_sage_graph(v, undirected_edges):

    G = Graph()
    for e in undirected_edges:
        G.add_edge(e)

    temp_v =  G.vertices()
    for v_i in v:
        if v_i.pattern_name not in temp_v:
            G.add_vertex(v_i.pattern_name)

    G.weighted(True)

    return G

"""
