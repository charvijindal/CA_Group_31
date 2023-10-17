class Directory:
    def __init__(self, main_memory) -> None:
        self.dir = {}
        self.main_memory = main_memory

        for i in self.main_memory.main_memory.keys():
            self.dir[i] = "10000" # state (2) | owner (1) | sharer list (2)
        
        print(self.dir)

    def set_dir(self, addr, state: str, owner: str, sharer_list: str) -> None:
        
        final_state = ""
        if state == "M":
            final_state = "00"
        elif state == "S":
            final_state = "01"
        elif state == "I":
            final_state = "10"
        else:
            final_state = "11"            

        self.dir[addr] = final_state + owner + sharer_list
    
    def get_dir(self, addr):
        val = self.dir[int(addr)]
        state = val[:2]
        final_state = ""

        if state == "00":
            final_state = "M"
        elif state == "01":
            final_state = "S"
        elif state == "10":
            final_state = "I"
        else:
            final_state = "O"  

        return [final_state, val[2], val[3:]]