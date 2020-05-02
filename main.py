import argparse
from cpu import CPU
from instruction import Instruction, LDAInstruction


# set up command line argument parser
parser = argparse.ArgumentParser(description='NES emulator')
parser.add_argument('rom_path',
                    type=str,
                    metavar="R",
                    help='path to rom')
args = parser.parse_args()

# TODO: validate rom path is correct
print(args.rom_path)

# load rom
with open(args.rom_path, "rb") as file:
    rom_content = file.read()

# create cpu
cpu = CPU()

