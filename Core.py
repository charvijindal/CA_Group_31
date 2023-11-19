from L1Cache import L1Cache, L1CacheController

class Core:
    def __init__(self, interconnect) -> None:
        self.interconnect = interconnect
        self.cache = L1Cache(2)
        self.cache_controller = L1CacheController(self.cache)

    def interpret_instruction(self, instruction):
        print(instruction)


