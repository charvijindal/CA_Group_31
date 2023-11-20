from L1Cache import L1Cache, L1CacheController

class Core:
    def __init__(self, interconnect, num) -> None:
        self.cache_controller = L1CacheController(interconnect, num)
        self.num = num
        self.cache_memory_dump = []

    def setInterconnect(self, interconnect):
        self.cache_controller.setCacheControllerInterconnect(interconnect)
        
    def interpret_instruction(self, instruction):
        
        type_instruction = instruction[0]
        address = int(instruction[1])
        add_im = 0

        dump_inst = [self.num] + instruction
        
        if type_instruction == "LS":
            #GetShared
            print(f"Transaction made for address {address} : getShared")
            value = self.cache_controller.getShared(address)
            self.cache_memory_dump.append(self.cache_controller.getCacheMemoryDump(dump_inst))
            self.cache_controller.interconnect.make_directory_dump(dump_inst, address)
            self.cache_controller.interconnect.make_main_memory_dump(address)
            print(f"Response value: {value}")
            # print(value)
            
        elif type_instruction == "LM":
            #GetModified
            print(f"Transaction made for address {address} : getModified")
            value = self.cache_controller.getModified(address)
            self.cache_memory_dump.append(self.cache_controller.getCacheMemoryDump(dump_inst))
            self.cache_controller.interconnect.make_directory_dump(dump_inst, address)
            self.cache_controller.interconnect.make_main_memory_dump(address)
            print(f"Response value: {value}")
            # print(value)
            
        elif type_instruction == "IN":
            #PutInvalid
            print(f"Transaction made for address {address} : putInvalid")
            value = self.cache_controller.putInvalid(address)
            self.cache_memory_dump.append(self.cache_controller.getCacheMemoryDump(dump_inst))
            self.cache_controller.interconnect.make_directory_dump(dump_inst, address)
            self.cache_controller.interconnect.make_main_memory_dump(address)
            print(f"Response value: {value}")
            # print(value)
        
        elif type_instruction == "ADD":
            add_im = int(instruction[2])
            #GetModified
            value = self.cache_controller.getModified(address,add_im)
            self.cache_memory_dump.append(self.cache_controller.getCacheMemoryDump(dump_inst))
            self.cache_controller.interconnect.make_directory_dump(dump_inst, address)
            self.cache_controller.interconnect.make_main_memory_dump(address)
            # print(value)
            
        else:
            print("Invalid Instruction, moving on")
        
        


