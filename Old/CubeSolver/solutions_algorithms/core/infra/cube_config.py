from abc import abstractmethod


class CubeConfig:
    @staticmethod
    @abstractmethod
    def get_solved_state_array():
        pass

    @staticmethod
    @abstractmethod
    def get_solved_targets_arr():
        pass


    @staticmethod
    @abstractmethod
    def get_corners_cubies_ind_mapping():
        pass

    @staticmethod
    @abstractmethod
    def get_cube_group():
        pass

    @staticmethod
    @abstractmethod
    def get_all_cubies_groups():
        pass


    @staticmethod
    @abstractmethod
    def move(in_state, move_str):
        pass

    @staticmethod
    @abstractmethod
    def get_next_moves(state, previous_moves):
        pass

    @staticmethod
    @abstractmethod
    def get_opposite_moves_sequence(moves_sequence):
        pass
