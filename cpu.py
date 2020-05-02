from instruction import Instruction


class CPU:
    def __init__(self):
        # TODO: proper register
        self.registers = []

    def process_instruction(self, instruction: Instruction):
        # TODO: process instructions
        instruction.process()
