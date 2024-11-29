Alg1MetaPatternConfig = {
    'fixed_cubies_dict': {'DRB': 'drb', 'DLF': 'dlf', 'DLB': 'dlb'},
    'coi': (['drf'], 'all'),
    'free_target_cubies': ['urf', 'urb', 'ulf', 'ulb'],
    'search_alg': 'bfs',
    "depth": 3
}

Alg2MetaPatternConfig = {
    'fixed_cubies_dict': {'DRB': 'drb', 'DLF': 'dlf', 'DLB': 'dlb', 'DRF': 'drf'},
    'coi': (['urf', 'urb'], 'placement'),
    'free_target_cubies': ['ulf', 'ulb'],
    'search_alg': 'moves',
    "depth": 3
}


