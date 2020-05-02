from abc import ABC, abstractmethod


class Instruction(ABC):
    def __init__(self):
        pass

    def __str__(self):
        return "{} : Identifier bytes: {}".format(self.__class__.__name__,
                                                  self.identifier_byte)

    @property
    def identifier_byte(self) -> bytes:
        return None

    @property
    def name(self):
        return "Undefined"

    @property
    def instruction_length(self):
        return 1

    @abstractmethod
    def execute(self, *args):
        print(self.__str__())


class LDAInstruction(Instruction):
    instruction_length = 2
    identifier_byte = bytes.fromhex("A9")

    def execute(self):
        super().execute()


class SEIInstruction(Instruction):
    instruction_length = 1
    identifier_byte = bytes.fromhex("78")

    def execute(self, cpu):
        super().execute()

        # set the interrupt flag to 1
        cpu.status_reg.interrupt_bit = True


class CLDInstruction(Instruction):
    instruction_length = 1
    identifier_byte = bytes.fromhex("D8")

    def execute(self):
        super().execute()
