class Memory:
    def __init__(self) -> None:
        self.main_memory = {}
        for i in range(32):
            self.main_memory[i] = 0

    def get_value(self, address: int) -> int:
        return self.main_memory[address]

    def set_value(self, address: int, value: int) -> None:
        self.main_memory[address] = value
