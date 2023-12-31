from update_memory import read_memory, write_memory, inspect_memory

class Interconnect:
    def __init__(self, directory_controller, cores) -> None:
        self.directory_controller = directory_controller
        self.cores = cores
        self.directory_memory_dump = []
        self.main_memory_dump = []
        self.curr_dir_updates = 0
        self.dir_updates = [0]   

        for core in cores:
            core.setInterconnect(self)

    def read_from_memory(self, addr):
        return read_memory(addr)
    
    def write_to_memory(self, addr, val):
        write_memory(addr, val)

    def core_dump(self):
        return inspect_memory()

    def get_directoryLine(self, addr):
        return self.directory_controller.get_line(addr)
    
    def set_directoryLine(self, line, addr):
        self.directory_controller.set_line(line, addr)
        
    def getValueFromCore(self, addr, owner):
        value= self.cores[owner].cache_controller.read(addr, 1)
        from_core = 1
        if value is None:
            value = self.read_from_memory(addr)
            from_core = 0
        return value, from_core
    
    def make_directory_dump(self, dump_inst, addr):
        self.directory_memory_dump.append([dump_inst, self.directory_controller.get_line(addr)])
    
    def make_main_memory_dump(self, addr):
        self.main_memory_dump.append([addr, self.read_from_memory(addr)])
    # def test(self):
    #     return self.cores[1].cache_controller.read(2)


