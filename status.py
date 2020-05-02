class Status:
    """
            status register :
            7  bit  0
            ---- ----
            NVss DIZC
            |||| ||||
            |||| |||+- Carry
            |||| ||+-- Zero
            |||| |+--- Interrupt Disable
            |||| +---- Decimal
            ||++------ No CPU effect, see: the B flag
            |+-------- Overflow
            +--------- Negative
    """

    def __init__(self):
        self.negative_bit = False  # type: bool
        self.overflow_bit = False  # type: bool
        self.decimal_bit = False  # type: bool
        self.interrupt_bit = True  # type: bool
        self.zero_bit = False  # type: bool
        self.carry_bit = False  # type: bool
