from L1Cache import L1Cache, L1CacheController

class Core:
    def __init__(self, interconnect, num) -> None:
        self.cache_controller = L1CacheController(interconnect, num)
        self.num = num

    def setInterconnect(self, interconnect):
        self.cache_controller.setCacheControllerInterconnect(interconnect)
        
    def interpret_instruction(self, instruction):
        print(instruction)
        
        type_instruction = instruction[0]
        address = int(instruction[1])
        add_im = 0
        
        if type_instruction == "LS":
            #GetShared
            value = self.cache_controller.getShared(address)
            print(value)
            
        elif type_instruction == "LM":
            #GetModified
            value = self.cache_controller.getModified(address)
            print(value)
            
        elif type_instruction == "IN":
            #PutInvalid
            value = self.cache_controller.putInvalid(address)
            print(value)
        
        elif type_instruction == "ADD":
            add_im = int(instruction[2])
            #GetModified
            value = self.cache_controller.getModified(address,add_im)
            print(value)
            
        else:
            print("Invalid Instruction, moving on")
        
        


