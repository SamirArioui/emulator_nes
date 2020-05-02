import argparse
from cpu import CPU
from rom import Rom
from instruction import Instruction, LDAInstruction

# set up command line argument parser
parser = argparse.ArgumentParser(description='NES emulator')
parser.add_argument('rom_path',
                    type=str,
                    metavar="R",
                    help='path to rom')
args = parser.parse_args()

# load rom
with open(args.rom_path, "rb") as file:
    rom_content = file.read()
rom = Rom(rom_content)

# create cpu
cpu = CPU()
cpu.start_up()
cpu.run_rom(rom)
