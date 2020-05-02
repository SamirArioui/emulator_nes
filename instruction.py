from abc import ABC, abstractmethod


class Instruction(ABC):
    def __init__(self, identifier_byte: int):
        self.identifier_byte = identifier_byte

    @abstractmethod
    def process(self):
        print("Identifier bytes: {}".format(self.identifier_byte))


class LDAInstruction(Instruction):
    def process(self):
        super().process()
