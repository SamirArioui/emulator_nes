from typing import List

KB_BLOCK = 1024


class Rom(object):
    memory_start_location = 0x4020
    memory_end_location = 0xFFFF

    def __init__(self, rom_bytes: bytes):
        self.header_size = 16
        # TODO: unhardcode pull from header
        self.num_prg_blocks = 2

        # program data start after header
        # and last for a set number of 16KB blocks
        self.rom_bytes = rom_bytes
        self.prg_bytes = rom_bytes[self.header_size:self.header_size + 16 * KB_BLOCK * self.num_prg_blocks]

    def get_memory(self) -> List[bytes]:
        return self.rom_bytes

    def get(self, position: int, size: int = 1) -> bytes:
        """
        get bytes at given position
        """
        return self.get_memory()[position:position + size]
