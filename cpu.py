from instruction import LDAInstruction, SEIInstruction, CLDInstruction
from rom import Rom
from collections import defaultdict
from status import Status


class CPU:
    def __init__(self):
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
            LDAInstruction(),
            SEIInstruction(),
            CLDInstruction()
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

            # we have a valid instruction
            instruction.execute(self)

            self.pc_reg += instruction.instruction_length
