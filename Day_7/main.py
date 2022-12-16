from pathlib import Path
from functools import reduce
from shell import Shell

path = Path(__file__).with_name('input.txt')
shell = Shell()
with path.open() as file:
    for line in file:
        command = line.strip()
        shell.command(command)

main_dir = shell.main_dir
    
all_dirs = main_dir.getAllSubdirs()
light_dirs = [dir for dir in all_dirs if dir.getSize() <=  100000]
total_light_dir_sizes = reduce(lambda total_size, dir: total_size + dir.getSize(), light_dirs, 0)
print(f"Part 1 :: Total size of light subdirs: {total_light_dir_sizes}") 

######################  PART 2 ###################################
total_space_used = main_dir.getSize()
free_space = 70000000 - total_space_used
free_space_needed = 30000000 - free_space
print(f"Part 2 :: Total space used: {total_space_used}")
print(f"Part 2 :: Current free space: {free_space}")
print(f"Part 2 :: Need to free: {free_space_needed}")

nominated_to_delete = [dir.getSize() for dir in all_dirs if dir.getSize() >= free_space_needed]
print(f"Part 2 :: Smallest dir nominated to be deleted: {min(nominated_to_delete)}")
