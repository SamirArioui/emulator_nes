from typing import List

KB = 1024


class Ram:
    def __init__(self):
        # TODO bytes vs int
        self.memory = [0] * KB * 2  # type: List[int]
        x = 1

    def get_byte(self, position):
        return self.memory[position]

    def set_byte(self, position, byte):
        self.memory[position] = byte
