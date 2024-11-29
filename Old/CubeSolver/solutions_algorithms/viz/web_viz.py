import json

import pandas as pd

from solver.utils import get_perm

COLORS_REF = ['r', 'l', 'u', 'd', 'f', 'b']
ALL_GREY = ["#808080", "#808080", "#808080", "#808080", "#808080", "#808080"]
ALL_COLORS = ["#2986cc", "#6aa84f", "#ffffff", "#ffd966", "#eb2e2f", "#e69138"]



def create_dict_for_web(G, pos, summary_path):
    pos_dict = {}
    colors_dict = {}
    pos_dict_new = custom_pos_range(pos)
    for v in G.V:
        pos_dict[v.pattern_name] = pos[v.pattern_name]

        d = {}
        for c, val in v.pattern_obj.fixed_cubies_dict.items():
            col_colors = ALL_GREY.copy()
            for h, v_i in zip(c, val):
                col_colors[COLORS_REF.index(h.lower())] = ALL_COLORS[COLORS_REF.index(v_i)]
            d[c] = col_colors

        for c in ['DRB', 'DLF', 'DLB', 'DRF', 'URF', 'URB', 'ULF', 'ULB']:
            if c not in d.keys():
                d[c] = ALL_GREY

        colors_dict[v.pattern_name] = d

    merged = {k : {'pos': pos_dict_new[k], 'colors': colors_dict[k]} for k in [v.pattern_name for v in G.V]}

    E = [[k[0], k[1], ' | '.join(v.moves)] for k, v in G.E.items()]
    json.dump({'V': merged, 'E': E}, open(summary_path, "w"))




def fix_range(x, a, b, c, d):
    v = c + ((x-a)/(b-a)) * (d-c)
    return int(v)


ranges = [[0, 1400], [0, 1000]]
def custom_pos_range(pos_dict):
    pos_df = pd.DataFrame.from_dict(pos_dict, orient='index')
    for i, col in enumerate(list(pos_df.columns)):
        a, b = pos_df[col].min(), pos_df[col].max()
        c, d = ranges[i][0], ranges[i][1]
        pos_df[col] = pos_df[col].apply(lambda x: fix_range(x, a, b, c, d))
    pos_d = pos_df.to_dict(orient='index')
    for k in pos_d.keys():
        pos_d[k] = list(pos_d[k].values())

    return pos_d
