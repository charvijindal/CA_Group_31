from L1Cache import L1Cache, L1CacheController

class Core:
    def __init__(self, interconnect) -> None:
        self.cache_controller = L1CacheController(interconnect)

    def interpret_instruction(self, instruction):
        print(instruction)


