from update_memory import read_memory, write_memory, inspect_memory

class Interconnect:
    def __init__(self) -> None:
        pass

    def read_from_memory(self, addr):
        return read_memory(addr)
    
    def write_to_memory(self, addr, val):
        write_memory(addr, val)

    def core_dump(self):
        return inspect_memory()


