from abc import ABC


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

    def execute(self, cpu, data_bytes):
        # TODO turn this into somathing that can change the byte into correct format
        print(self.__str__())


# data instructions
class LdaImmInstruction(Instruction):
    instruction_length = 2
    identifier_byte = bytes.fromhex("A9")

    def execute(self, cpu, data_bytes):
        # load value into accumulator register
        cpu.a_reg = data_bytes[0]


class StaAbsInstruction(Instruction):
    instruction_length = 3
    identifier_byte = bytes.fromhex("8D")

    def execute(self, cpu, data_bytes):
        # take value from a_reg and put it memory
        memory_address = int.from_bytes(data_bytes, byteorder="little")
        val_to_store = cpu.a_reg
        memory_owner = cpu.get_memory_owner(memory_address)
        memory_owner.set(memory_address, val_to_store)


# status register instruction
class SEIInstruction(Instruction):
    instruction_length = 1
    identifier_byte = bytes.fromhex("78")

    def execute(self, cpu, data_bytes):
        # set the interrupt flag to 1
        cpu.status_reg.interrupt_bit = True


class CLDInstruction(Instruction):
    instruction_length = 1
    identifier_byte = bytes.fromhex("D8")

    def execute(self, cpu, data_bytes):
        # set the decimal flag to 0
        cpu.status_reg.decimal_bit = False
