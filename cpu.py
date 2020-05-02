from instruction import LDAInstruction, SEIInstruction, CLDInstruction
from rom import Rom
from collections import defaultdict


class CPU:
    def __init__(self):
        # TODO: proper register
        self.registers = []
        # program counter stores current execution
        self.program_counter = None
        self.rom = None
        self.running = True
        self.instruction_classes = [
            LDAInstruction,
            SEIInstruction,
            CLDInstruction
        ]
        self.instruction_class_mapping = defaultdict()
        for instruction_class in self.instruction_classes:
            self.instruction_class_mapping[instruction_class.identifier_byte] = instruction_class

    def run_rom(self, rom: Rom):
        # load rom
        self.rom = rom
        self.program_counter = self.rom.header_size

        # run program
        while self.running:
            # get the current byte at program counter
            identifier_byte = self.rom.get_bytes(self.program_counter)

            # turn the byte into Instruction
            instruction_class = self.instruction_class_mapping.get(identifier_byte, None)
            if instruction_class is None:
                raise Exception("Instruction does not exist")

            # we have a valid instruction
            instruction = instruction_class()
            instruction.execute()

            self.program_counter += instruction.instruction_length
