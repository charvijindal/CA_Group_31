from L1Cache import L1Cache, L1CacheController

class Core:
    def __init__(self, interconnect, num) -> None:
        self.cache_controller = L1CacheController(interconnect)
        self.num = num

    def interpret_instruction(self, instruction):
        # print(instruction)
        
        type_instruction = instruction[0]
        address =instruction[1]
        add_im = 0
        
        if type_instruction == "LS":
            #GetShared
            
        elif type_instruction == "LM":
            #GetModified
            
        elif type_instruction == "IN":
            #PutInvalid
        
        elif type_instruction == "ADD":
            add_im = instruction[2]
            #GetModified
            
        else:
            print("Invalid Instruction, moving on")
        
        


