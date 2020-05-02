import argparse
from cpu import CPU
from rom import Rom
from memory import Ram
from ppu import PPU


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

# create ram
ram = Ram()

# create ppu
ppu = PPU()

# create cpu
cpu = CPU(ram, ppu)
cpu.start_up()
cpu.run_rom(rom)
