max_carrying = 0
with open("/Users/ignacio.colombo/desarrollo/adventscode/1st/input.txt") as file:
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
