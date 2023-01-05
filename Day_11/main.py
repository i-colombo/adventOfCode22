from pathlib import Path
from monkeys import *
from functools import reduce

path = Path(__file__).with_name('input.txt')
current_monkey_builder = None
monkeys_part_two = []
with path.open() as file:
    for line in file:
        instruction = line.strip()
        if instruction[:6] == "Monkey":        
            current_monkey_builder = MonkeyBuilder(name = instruction[7:])
        elif instruction[:15] == "Starting items:":
            items = [int(item) for item in instruction[15:].split(",")]
            current_monkey_builder.setItems(items)
        elif instruction[:10] == "Operation:":
            operation = instruction[21:].strip()
            current_monkey_builder.setWorryOperation(operation)
        elif instruction[:5] == "Test:":
            test_operation = int(instruction[19:].strip())
            current_monkey_builder.setTestWorryOperation(test_operation)
        elif instruction[:8] == "If true:":
            worried_target_monkey = int(instruction[25:])
            current_monkey_builder.setWorriedTargetMonkey(worried_target_monkey)
        elif instruction[:9] == "If false:":
            calmed_target_monkey = int(instruction[26:])
            current_monkey_builder.setCalmedTargetMonkey(calmed_target_monkey)
            Monkey.monkeys.append(current_monkey_builder.build())
            monkeys_part_two.append(current_monkey_builder.build())

number_of_rounds = 20
divisor = 3
for _ in range(number_of_rounds):
    for monkey in Monkey.monkeys:
        monkey.throwItems(DivisorReliefCalculator(divisor))

inspected_counts = [monkey.getInspectedItemsCount() for monkey in Monkey.monkeys]
inspected_counts.sort(reverse=True)
print(f"Part 1 :: Inspected counts: {inspected_counts}")

monkey_business = inspected_counts[0] * inspected_counts[1]
print(f"Part 1 :: Monkey business: {monkey_business}")


# :::::::::::::: PART TWO :::::::::::::::::::::

Monkey.monkeys.clear()
Monkey.monkeys.extend(monkeys_part_two)

number_of_rounds = 10000
modulus = reduce(lambda total_modulus, monkey: total_modulus * monkey.getTestWorryOperation(), Monkey.monkeys, 1)

for _ in range(number_of_rounds):
    for monkey in Monkey.monkeys:
        monkey.throwItems(ModulusReliefCalculator(modulus))

inspected_counts = [monkey.getInspectedItemsCount() for monkey in Monkey.monkeys]
inspected_counts.sort(reverse=True)
print(f"Part 2 :: Inspected counts: {inspected_counts}")

monkey_business = inspected_counts[0] * inspected_counts[1]
print(f"Part 2 :: Monkey business: {monkey_business}")
