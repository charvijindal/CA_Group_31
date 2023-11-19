class Directory:
    def __init__(self) -> None:
        self.dir = [{"state": 2, "owner": 0, "sharer_list": [0 for _ in range(4)]} for _ in range(64)]

class DirectoryController:
    def __init__(self) -> None:
        self.directory = Directory()

    # def get_state(self, addr):
    #     return self.dir[addr]['state']
    
    # def get_owner(self, addr):
    #     return self.dir[addr]['owner']
    
    # def get_sharer_list(self, addr):
    #     return self.dir[addr]['sharer_list']

    # def set_state(self, addr, state):
    #     self.dir[addr]['state'] = state

    # def set_owner(self, addr, owner):
    #     self.dir[addr]['owner'] = owner
    
    # def set_sharer_list(self, addr, sharer_list):
    #     self.dir[addr]['sharer_list'] = sharer_list
    
    def get_line(self, addr):
        return self.directory.dir[addr]
    
    def set_line(self, line, addr):
        self.directory.dir[addr] = line

