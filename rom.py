from typing import List

HEADER_SIZE = 16
KB_BLOCK = 1024


class Rom:
    def __init__(self, rom_bytes: List[int]):
        # TODO: unhardcode pull from header
        self.num_prg_blocks = 2

        # program data start after header
        # and last for a set number of 16KB blocks
        self.data_bytes = rom_bytes[HEADER_SIZE:HEADER_SIZE + 16 * KB_BLOCK * self.num_prg_blocks]
