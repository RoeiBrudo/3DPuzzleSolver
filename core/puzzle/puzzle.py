from core.puzzle.puzzle_instance import PuzzleInstance



class Puzzle:
    def __init__(self, puzzle_space, cubie_repr):
        self.puzzle_space = puzzle_space
        self.cubie_repr = cubie_repr

    def get_instance(self, init_state=None):
        state = self.puzzle_space.solved_state if init_state is None else init_state
        return PuzzleInstance(self, init_state=state)
