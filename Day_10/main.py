from pathlib import Path
from crtfunc import *

path = Path(__file__).with_name('input.txt')
cycle = 0
x = 1
total_strength = 0
with path.open() as file:
    for line in file:
        instruction = line.strip()
        cycle += 1
        total_strength = accumulated_strength(total_strength, cycle, x)

        if instruction[:4] == 'addx':
            cycle += 1
            total_strength = accumulated_strength(total_strength, cycle, x)
            x += int(instruction[5:])

print(f"Part 1 :: Total Strength: {total_strength}")

######################  PART 2 ###################################

cycle = 0
sprite_pos = 1
total_strength = 0
screen = []
with path.open() as file:
    for line in file:
        instruction = line.strip()
        cycle += 1
        refreshScreen(screen, cycle, sprite_pos)

        if instruction[:4] == 'addx':
            cycle += 1
            refreshScreen(screen, cycle, sprite_pos)
            sprite_pos += int(instruction[5:])

print("Part 2 :: Screen output:")
for screen_row in screen:
    print(screen_row)
