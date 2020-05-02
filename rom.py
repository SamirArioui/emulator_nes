KB_BLOCK = 1024


class Rom:
    def __init__(self, rom_bytes: bytes):
        self.header_size = 16
        # TODO: unhardcode pull from header
        self.num_prg_blocks = 2

        # program data start after header
        # and last for a set number of 16KB blocks
        self.rom_bytes = rom_bytes
        self.prg_bytes = rom_bytes[self.header_size:self.header_size + 16 * KB_BLOCK * self.num_prg_blocks]

    def get_bytes(self, position: int) -> bytes:
        """
        get byte at a given position
        """
        return self.rom_bytes[position:position + 1]
