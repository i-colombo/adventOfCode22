from pathlib import Path

path = Path(__file__).with_name('input.txt')

class SortedList:
    list = []
    top = 3
    len = 0
    def __init__(self, defaultList = [], top = 3):
        defaultList.sort(reverse = True)
        self.list = defaultList
        self.top = top
        self.len = len(defaultList)
    
    def add(self, number):
        if self.len < self.top:
            self.list.append(number)
            self.len += 1
            self.list.sort(reverse = True)
        elif self.list[2] < number:
            self.list[2] = number
            self.list.sort(reverse = True)
        
    def total(self):
        return sum(self.list)


max_carrying = 0
top_elves_max_carrying = SortedList([], 3)
with path.open() as file:
    elf_carrying = 0
    for line in file:
        strippedLine = line.strip()
        if strippedLine == "":
            if elf_carrying > max_carrying:
                max_carrying = elf_carrying
            top_elves_max_carrying.add(elf_carrying)
            elf_carrying = 0
        else:
            carrying = int(strippedLine)
            elf_carrying += carrying


print(f"Most carrying Elf is carrying: {max_carrying}")
print(f"Top 3 most carrying Elves are carrying: {top_elves_max_carrying.list} with total of: {top_elves_max_carrying.total()}")
