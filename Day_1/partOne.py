from pathlib import Path

path = Path(__file__).with_name('input.txt')
max_carrying = 0
with path.open() as file:
    elf_carrying = 0
    for line in file:
        strippedLine = line.strip()
        if strippedLine == "":
            if elf_carrying > max_carrying:
                max_carrying = elf_carrying
            elf_carrying = 0
        else:
            carrying = int(strippedLine)
            elf_carrying += carrying

print(f"Most carrying Elf is carrying: {max_carrying}")
