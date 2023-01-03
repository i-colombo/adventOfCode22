from pathlib import Path
from monkeys import MonkeyBuilder

path = Path(__file__).with_name('input.txt')
monkeys = []
current_monkey_builder = None
with path.open() as file:
    for line in file:
        instruction = line.strip()
        if instruction[:6] == "Monkey":
            if current_monkey_builder != None:
                monkeys.append(current_monkey_builder.build())
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

[print(monkey) for monkey in monkeys]

