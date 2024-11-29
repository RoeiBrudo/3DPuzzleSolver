#
# class DisjointSet:
#     def __init__(self, nodes):
#         self.sets = {n: [n] for n in nodes}
#
#     def find(self, node):
#         for k, k_nodes in self.sets.items():
#             if node in k_nodes:
#                 return k
#
#     def union(self, node1, node2):
#         k1, k2 = self.find(node1), self.find(node2)
#         if k1 != k2:
#             self.sets[k1].extend(self.sets[k2])
#             del self.sets[k2]
#             return True
#         return False
#
#
# class DisjointGraph:
#     def __init__(self, v, e):
#         self.V = v
#         self.E = sorted(e, key=lambda x:x[2])
#
#         self.solution_set = []
#
#     def is_solution(self):
#         solution_edges = []
#         d = DisjointSet(self.V)
#
#         for e in self.E:
#             is_used = d.union(e[0], e[1])
#             if is_used:
#                 solution_edges.append(e)
#
#         if len(d.sets.keys()) == 1:
#             self.solution_set = solution_edges
#             return True
#
#         else:
#             return False
#
#     def get_paths(self):
#         start_nodes = [v for v in self.V if v != 'T']
#         paths = {}
#         for s in start_nodes:
#             p = self.simple_bfs(s, 'T')
#             if p is not None:
#                 paths[s] = p
#             else:
#                 return {}
#
#         return paths
#
#     def simple_bfs(self, start_node, end_node):
#         SimpleBFSNode = namedtuple("SimpleBFSNode", "v path_from_root")
#
#         q = [SimpleBFSNode(start_node, [])]
#         visited = []
#         while q:
#             cur = q.pop()
#             if cur.v not in visited:
#                 visited.append(cur.v)
#
#                 if cur.v == end_node:
#                     return cur.path_from_root
#
#                 neighbors = list(
#                     set([e[1] for e in self.solution_set if e[0] == cur.v] + [e[0] for e in self.solution_set if e[1] == cur.v]))
#                 for n in neighbors:
#                     p = cur.path_from_root + [(cur.v, n)]
#                     new_n = SimpleBFSNode(n, p)
#                     q.append(new_n)
#
#     @staticmethod
#
# """
#     def is_solution(self):
#         disjoint_edges = DisjointGraph.generate_disjoint_edges(self.E_pool)
#         disjoint_graph = DisjointGraph([v.pattern_name for v in self.V], disjoint_edges)
#         if disjoint_graph.is_solution():
#             ...
#
#
#
#             # disjoint_paths = disjoint_graph.get_paths()
#             # self.solution_edges = self.solution_edges_from_disjoint_paths(disjoint_paths)
#             #
#             # score = 0
#             # for e in self.solution_edges:
#             #     score += e.weight
#             # self.score = score
#             # print('found solution', self.score)
#             #
#             # return True
#
#         return False
#
#
#     def generate_joint_graphs(self):
#         ...
#
#     def solution_edges_from_disjoint_paths(self, disjoint_paths):
#         disjoint_edges, solution_edges = [], []
#         for s, p in disjoint_paths.items():
#             solution_edges.extend(p)
#         solution_edges = list(set(solution_edges))
#
#         for edge in solution_edges:
#             e = [e for e in self.E_pool if (e.start_node == edge[0]) and (e.end_node == edge[1])]
#             sorted_e = sorted(e, key=lambda x: x.weight)
#             disjoint_edges.append(sorted_e[0])
#
#         return disjoint_edges
# """