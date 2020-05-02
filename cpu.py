from instruction import LdaImmInstruction, SEIInstruction, CLDInstruction, StaAbsInstruction
from rom import Rom
from memory import Ram
from ppu import PPU
from collections import defaultdict
from status import Status

RAM_START_INCLUSIVE = int.from_bytes(bytes.fromhex('0000'), byteorder="big")
RAM_END_INCLUSIVE = int.from_bytes(bytes.fromhex('1FFF'), byteorder="big")

PPU_START_INCLUSIVE = int.from_bytes(bytes.fromhex('2000'), byteorder="big")
PPU_END_INCLUSIVE = int.from_bytes(bytes.fromhex('2007'), byteorder="big")


class CPU:
    def __init__(self, ram: Ram, ppu: PPU):
        self.ram = ram
        self.ppu = ppu

        # status registers : store a single byte
        self.status_reg = None  # type: Status

        # counter registers: store a single byte
        self.pc_reg = None  # program counter register
        self.sp_reg = None  # stack pointer register

        # data registers: store a single byte
        self.x_reg = None  # x register
        self.y_reg = None  # y register
        self.a_reg = None  # accumulator register

        # program counter stores current execution
        self.rom = None
        self.running = True
        self.instructions = [
            LdaImmInstruction(),
            SEIInstruction(),
            CLDInstruction(),
            StaAbsInstruction(),
        ]
        self.instruction_mapping = defaultdict()
        for instruction in self.instructions:
            self.instruction_mapping[instruction.identifier_byte] = instruction

    def start_up(self):
        """
        set the initial value of cpu registers
        status register : 0011 0100 (IRQ disable)
        a, x, y register: 0000 0000
        stack pointer register : 1111 1101
        $4017: 0 (frame IRQ disabled)
        $4015: 0 (sound channels disabled)
        $4000-$400f: 0 (sound register)
        $4010-$4013: 0 (delta modulation register)
        """
        # TODO hex vs binary
        self.pc_reg = 0
        self.status_reg = Status()
        self.sp_reg = bytes.fromhex('FD')

        self.x_reg = 0
        self.y_reg = 0
        self.a_reg = 0

        # TODO implement memory sets
    def get_memory_owner(self, location: int):
        """
        return rhe owner memory location
        """
        if RAM_START_INCLUSIVE <= location <= RAM_END_INCLUSIVE:
            return self.ram
        elif PPU_START_INCLUSIVE <= location <= PPU_END_INCLUSIVE:
            # pass off to the ppu register manager
            return self.ppu

    def run_rom(self, rom: Rom):
        # load rom
        self.rom = rom
        self.pc_reg = self.rom.header_size

        # run program
        while self.running:
            # get the current byte at program counter
            identifier_byte = self.rom.get_bytes(self.pc_reg)

            # turn the byte into Instruction
            instruction = self.instruction_mapping.get(identifier_byte, None)
            if instruction is None:
                raise Exception("Instruction does not exist")

            # get the correct amount of data bytes
            num_data_bytes = instruction.instruction_length - 1
            data_bytes = rom.get_bytes(self.pc_reg + 1, num_data_bytes)

            # we have a valid instruction
            instruction.execute(self, data_bytes)

            self.pc_reg += instruction.instruction_length
