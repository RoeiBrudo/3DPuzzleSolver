import math

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np
from colour import Color


FIXED_MARGIN = 0.1
FIXED_NODES_KEYS_DIST = 0
ARC_RAD = 0.25
LABEL_POS = 0
FONT_SIZE = 8


def get_colors_range(steps):
    return [str(c) for c in list(Color('violet').range_to(Color('green'), steps))]

def get_target_color():
    return 'orange'


def my_draw_networkx_edge_labels(G, pos, edge_labels=None, label_pos=LABEL_POS, font_size=FONT_SIZE, font_color="k",
                                 font_family="sans-serif", font_weight="normal", alpha=None, bbox=None,
                                 horizontalalignment="center", verticalalignment="center", ax=None, rotate=True,
                                 clip_on=True, rad=0):

    if ax is None:
        ax = plt.gca()
    if edge_labels is None:
        labels = {(u, v): d for u, v, d in G.edges(data=True)}
    else:
        labels = edge_labels
    text_items = {}
    for (n1, n2), label in labels.items():
        (x1, y1) = pos[n1]
        (x2, y2) = pos[n2]
        (x, y) = (
            x1 * label_pos + x2 * (1.0 - label_pos),
            y1 * label_pos + y2 * (1.0 - label_pos),
        )
        pos_1 = ax.transData.transform(np.array(pos[n1]))
        pos_2 = ax.transData.transform(np.array(pos[n2]))
        linear_mid = 0.5*pos_1 + 0.5*pos_2
        d_pos = pos_2 - pos_1
        rotation_matrix = np.array([(0,1), (-1,0)])
        ctrl_1 = linear_mid + rad*rotation_matrix@d_pos
        ctrl_mid_1 = 0.5*pos_1 + 0.5*ctrl_1
        ctrl_mid_2 = 0.5*pos_2 + 0.5*ctrl_1
        bezier_mid = 0.5*ctrl_mid_1 + 0.5*ctrl_mid_2
        (x, y) = ax.transData.inverted().transform(bezier_mid)

        if rotate:
            # in degrees
            angle = np.arctan2(y2 - y1, x2 - x1) / (2.0 * np.pi) * 360
            # make label orientation "right-side-up"
            if angle > 90:
                angle -= 180
            if angle < -90:
                angle += 180
            # transform data coordinate angle to screen coordinate angle
            xy = np.array((x, y))
            trans_angle = ax.transData.transform_angles(
                np.array((angle,)), xy.reshape((1, 2))
            )[0]
        else:
            trans_angle = 0.0
        # use default box of white with white border
        if bbox is None:
            bbox = dict(boxstyle="round", ec=(1.0, 1.0, 1.0), fc=(1.0, 1.0, 1.0))
        if not isinstance(label, str):
            label = str(label)  # this makes "1" and 1 labeled the same

        t = ax.text(
            x,
            y,
            label,
            size=font_size,
            color=font_color,
            family=font_family,
            weight=font_weight,
            alpha=alpha,
            horizontalalignment=horizontalalignment,
            verticalalignment=verticalalignment,
            rotation=trans_angle,
            transform=ax.transData,
            bbox=bbox,
            zorder=1,
            clip_on=clip_on,
        )
        text_items[(n1, n2)] = t

    ax.tick_params(
        axis="both",
        which="both",
        bottom=False,
        left=False,
        labelbottom=False,
        labelleft=False,
    )

    return text_items


def draw_nodes(G, pos):
    color_map = [attr for node, attr in nx.get_node_attributes(G, 'color').items()]

    nx.draw_networkx_nodes(G, pos, node_color=color_map, margins=FIXED_MARGIN)
    nx.draw_networkx_labels(G, pos)

    pos_attrs = {node: (coords[0] + FIXED_NODES_KEYS_DIST, coords[1] + FIXED_NODES_KEYS_DIST) for node, coords in pos.items()}
    custom_node_attrs = {node: attr for node, attr in nx.get_node_attributes(G, 'identifier').items()}
    nx.draw_networkx_labels(G, pos_attrs, verticalalignment='bottom', labels=custom_node_attrs)


def draw_edges(G, pos):
    curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
    straight_edges = list(set(G.edges()) - set(curved_edges))
    nx.draw_networkx_edges(G, pos, edgelist=straight_edges)
    nx.draw_networkx_edges(G, pos, edgelist=curved_edges, connectionstyle=f'arc3, rad = {ARC_RAD}')

    edge_weights = nx.get_edge_attributes(G, 'moves')
    curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
    straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
    my_draw_networkx_edge_labels(G, pos, edge_labels=curved_edge_labels, rotate=False, rad=ARC_RAD)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=straight_edge_labels, rotate=False, verticalalignment='top')


def custom_position(nodes_list, edges_list):
    initial = np.zeros([len(nodes_list), 2]) + np.nan
    pos = pd.DataFrame(initial, index=[n[0] for n in nodes_list])

    q = ['T']
    pos.loc['T'] = np.array([0, 0.5])

    while q:
        cur_node = q.pop()
        in_nodes = create_tree_from_base(pos, cur_node, edges_list)
        q.extend(in_nodes)

    pos_d = pos.to_dict(orient='index')
    for k in pos_d.keys():
        pos_d[k] = list(pos_d[k].values())

    return pos_d


def create_tree_from_base(pos, node, edges_list):
    in_edges = [e for e in edges_list if e[1] == node]
    angle = math.pi / (len(in_edges) + 1)
    base_loc = pos.loc[node].values
    for i, e in enumerate(in_edges):
        new_loc = [base_loc[0] + 1, base_loc[1] + len(e[2]['moves'].split("|"))*math.cos(angle*(i+1))]
        pos.loc[e[0]] = new_loc

    return [e[0] for e in in_edges]



def visualize_graph(G, image_path):

    host_state_dict = {}
    for s in G.V:
        pattern_identifier_dict = s.pattern_obj.pattern_identifier
        host = list(pattern_identifier_dict.keys())[0]
        host_state_dict[s.pattern_name]= host

    unique_hosts = list(set(host_state_dict.values()))
    colors_range = get_colors_range(len(unique_hosts))

    nodes_list = []
    for s in G.V:
        s_color = get_target_color() if s.pattern_name == 'T' else colors_range[unique_hosts.index(host_state_dict[s.pattern_name])]
        n = (s.pattern_name, {'identifier': s.pattern_obj.pattern_identifier, 'color': s_color})
        nodes_list.append(n)

    edges_list = []
    for edge in G.E:
        moves_path_s = ' | '.join(edge.moves)
        edges_list.append((edge.start_node, edge.end_node, {'moves': moves_path_s}))

    Graph = nx.DiGraph()
    Graph.add_nodes_from(nodes_list)
    Graph.add_edges_from(edges_list)

    plt.rcParams["figure.figsize"] = (20, 20)

    pos = custom_position(nodes_list, edges_list)
    draw_nodes(Graph, pos)
    draw_edges(Graph, pos)

    plt.savefig(image_path)
    plt.close()

