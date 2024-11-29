

class Puzzle:
    def __init__(self, pieces, puzzle_state):
        self.pieces = pieces
        self.puzzle_state = puzzle_state

    def get_instance(self, init_state=None):
        state = init_state if init_state else self.puzzle_state.puzzle_space.solved_state
        return PuzzleInstance(self)



class PuzzleInstance:
    def __init__(self, puzzle, init_state):
        self.puzzle = puzzle
        self.state_arr_repr = init_state


    def __str__(self):
        s = 'State \n'
        s += 'Array Repr: '
        s += str(self.state_arr_repr)
        s += '\nDict Repr: '
        s += str(self.puzzle.puzzle_state.translate_arr_to_dict(self.state_arr_repr))
        return s

    def move(self, move_str):
        self.state_arr_repr = self.puzzle_state.puzzle_space.move(self.state_arr_repr, move_str)
