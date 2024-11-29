



class PuzzleInstance:
    def __init__(self, puzzle, init_state):
        self.puzzle = puzzle
        self.state_arr_repr = init_state


    def __str__(self):
        s = 'State \n'
        s += 'Array Repr: '
        s += str(self.state_arr_repr)
        s += '\nDict Repr: '
        s += str(self.puzzle.cubie_repr.translate_arr_to_dict(self.state_arr_repr))
        return s

    def move(self, move_str):
        self.state_arr_repr = self.puzzle.puzzle_space.move(self.state_arr_repr, move_str)
