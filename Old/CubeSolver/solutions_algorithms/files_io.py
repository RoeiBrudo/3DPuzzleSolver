import os
import pickle


def read_pickle(pkl_path):
    if os.path.exists(pkl_path):
        return pickle.load(open(pkl_path, "rb"))
    else:
        raise FileNotFoundError


def write_pickle(obj, pkl_path):
    pickle.dump(obj, open(pkl_path, 'wb'))
