def isOdd20Divisor(value: int) -> bool:
    divisor = value / 20
    return divisor.is_integer() and divisor % 2 != 0

def accumulated_strength(current_strength: int, cycle: int, x_value: int) -> int:
    if cycle <= 220 and isOdd20Divisor(cycle):
        strength = cycle * x_value
        return current_strength + strength
    else:
        return current_strength

######################  PART 2 ###################################

def getCRTRow(screen: list, cycle: int) -> str:
    current_high_pos = getCRTColumn(cycle)
    if len(screen) < current_high_pos + 1:
        return ""
    else:
        return screen[current_high_pos]

def getCRTColumn(cycle: int) -> int:
    column_number = cycle / 40
    if column_number.is_integer():
        return int(column_number) - 1
    else:
        return int(column_number)

def getDrawingChar(cycle: int, sprite_pos: int) -> str:
    if cycle in range(sprite_pos, sprite_pos + 3):
        return "#"
    else:
        return "."

def draw(screen_row: str, sprite_pos: int) -> str:
    drawing_char = getDrawingChar(len(screen_row) + 1, sprite_pos)
    return screen_row + drawing_char

def display(screen: list, screen_row: str, cycle: int):
    current_high_pos = getCRTColumn(cycle)
    if len(screen) < current_high_pos + 1:
        screen.append(screen_row)
    else:
        screen[current_high_pos] = screen_row

def refreshScreen(screen: list, cycle: int, sprite_pos: int):
    screen_row = getCRTRow(screen, cycle)
    new_screen_row = draw(screen_row, sprite_pos)
    display(screen, new_screen_row, cycle)
