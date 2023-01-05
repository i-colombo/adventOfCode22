class DivisorReliefCalculator():
    def __init__(self, divisor: int):
        self.__divisor = divisor

    def relief(self, item: int) -> int:
        return item // self.__divisor

class ModulusReliefCalculator():
    def __init__(self, modulus: int):
        self.__modulus = modulus

    def relief(self, item: int) -> int:
        return item % self.__modulus

class Monkey():
    monkeys = []

    def __init__(self, name: str, items: list, worry_operation: str, test_worry_operation: int, worried_target_monkey: int, calmed_target_monkey: int):
        self.__name = name
        self.__items = items
        self.__worry_operation = worry_operation
        self.__test_worry_operation = test_worry_operation
        self.__worried_target_monkey = worried_target_monkey
        self.__calmed_target_monkey = calmed_target_monkey
        self.__inspected_items_count = 0

    def __repr__(self):
        return f'Name: {self.__name} \n- Items: {self.__items} \n- Worry Op: {self.__worry_operation} \n- Test Op: {self.__test_worry_operation} \n- Worried Monkey: {self.__worried_target_monkey} \n- Calmed Monkey: {self.__calmed_target_monkey} \n- Inspected items count: {self.__inspected_items_count}'

    def throwItems(self, relief_calculator):
        self.__inspected_items_count += len(self.__items)
        for _ in range(len(self.__items)):
            item = self.__items.pop(0)
            new_worry_level = relief_calculator.relief(self.humanWorryOfItem(item))
            self.throwItem(new_worry_level)
    
    def humanWorryOfItem(self, item: int) -> int:
        operation = self.__worry_operation.split(" ")
        operator = operation[0]
        term = operation[1]
        if term == "old":
            return self.calculate(operator, item, item)
        else:
            return self.calculate(operator, item, int(term))

    def calculate(self, operator: str, left_term: int, right_term: int) -> int:
        if operator == "+":
            return left_term + right_term
        elif operator == "-":
            return left_term - right_term
        elif operator == "*":
            return left_term * right_term
        elif operator == "/":
            return int(left_term / right_term)
        else:
            raise Exception("Unknown operator")
    
    def throwItem(self, item: int):
        if self.isHumanWorried(item):
            self.throwItemToMonkey(item, self.__worried_target_monkey)
        else:
            self.throwItemToMonkey(item, self.__calmed_target_monkey)
    
    def isHumanWorried(self, item: int) -> bool:
        return item % self.__test_worry_operation == 0

    def throwItemToMonkey(self, item: int, target_monkey_order: int):
        target_monkey = Monkey.monkeys[target_monkey_order]
        target_monkey.receive(item)

    def receive(self, item: int):
        self.__items.append(item)

    def getInspectedItemsCount(self) -> int:
        return self.__inspected_items_count

    def getTestWorryOperation(self):
        return self.__test_worry_operation

class MonkeyBuilder():
    def __init__(self, name: str = "", items: list = [], worry_operation: str = "", test_worry_operation: int = 1, worried_target_monkey: int = 0, calmed_target_monkey: int = 0):
        self.__name = name
        self.__items = items
        self.__worry_operation = worry_operation
        self.__test_worry_operation = test_worry_operation
        self.__worried_target_monkey = worried_target_monkey
        self.__calmed_target_monkey = calmed_target_monkey

    def setItems(self, items: list):
        self.__items = items
    
    def setWorryOperation(self, worry_operation: str):
        self.__worry_operation = worry_operation

    def setTestWorryOperation(self, test_worry_operation: int):
        self.__test_worry_operation = test_worry_operation

    def setWorriedTargetMonkey(self, worried_target_monkey: int):
        self.__worried_target_monkey = worried_target_monkey

    def setCalmedTargetMonkey(self, calmed_target_monkey: int):
        self.__calmed_target_monkey = calmed_target_monkey

    def build(self) -> Monkey:
        return Monkey(self.__name, self.__items.copy(), self.__worry_operation, self.__test_worry_operation, self.__worried_target_monkey, self.__calmed_target_monkey)
