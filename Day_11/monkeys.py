class Monkey():
    def __init__(self, name: str = "", items: list = [], worry_operation: str = "", test_worry_operation: int = 1, worried_target_monkey: int = 0, calmed_target_monkey: int = 0):
        self.__name = name
        self.__items = items
        self.__worry_operation = worry_operation
        self.__test_worry_operation = test_worry_operation
        self.__worried_target_monkey = worried_target_monkey
        self.__calmed_target_monkey = calmed_target_monkey

    def __repr__(self):
        return f'Name: {self.__name} \n- Items: {self.__items} \n- Worry Op: {self.__worry_operation} \n- Test Op: {self.__test_worry_operation} \n- Worried Monkey: {self.__worried_target_monkey} \n- Calmed Monkey: {self.__calmed_target_monkey}'
    
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
