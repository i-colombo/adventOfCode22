from pathlib import Path

def isOdd20Divisor(value: int) -> bool:
    divisor = value / 20
    return divisor.is_integer() and divisor % 2 != 0

def accumulated_strength(current_strength: int, cycle: int, x_value: int) -> int:
    if cycle <= 220 and isOdd20Divisor(cycle):
        strength = cycle * x_value
        return current_strength + strength
    else:
        return current_strength

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

print(f"Number of cycles: {cycle}")
print(f"Value of X: {x}")
print(f"Total Strength: {total_strength}")
