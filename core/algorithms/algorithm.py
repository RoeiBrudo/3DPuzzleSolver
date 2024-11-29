#
#
#
# class StepAlgorithm:
#     def __init__(self, puzzle, start_pattern, end_pattern):
#         self.puzzle = puzzle
#         self.start_pattern = start_pattern
#         self.end_pattern = end_pattern
#         self.cubies = list(self.start_pattern.keys())
#
#     def generate_sub_patterns(self):
#         fixed_cubies = [c for c in self.cubies
#                         if self.start_pattern[c] == self.end_pattern[c] and "*" not in self.start_pattern[c]]1
#         targets = [self.end_pattern[c] for c in self.cubies
#                    if self.start_pattern[c] != self.end_pattern[c] and "*" not in self.end_pattern[c]]
#
#         targets = [t[:-1] if "*" in t else t for t in targets]
#
#
#
#
