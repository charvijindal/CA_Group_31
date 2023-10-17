import random

class Cache:
    def __init__(self, cache_size=4):
        self.cache_size = cache_size
        self.cache_memory = {}

    def add_to_cache(self, addr, state, value):
        # Check if cache is full
        if len(self.cache_memory) >= self.cache_size:
            # If cache is full, remove a random item
            self.remove_random()
        self.cache_memory[addr] = [state, value]

    def remove_random(self):
        # Find and remove a random item from the cache
        if self.cache_memory:
            random_key = random.choice(list(self.cache_memory.keys()))
            del self.cache_memory[random_key]

    def get_from_cache(self, addr):
        # Get value from cache if present, otherwise return None
        return self.cache_memory.get(addr, None)
    
    def change_state(self, addr, state):
        #change the state of the cache address
        if addr in self.cache_memory:
            curr = self.cache_memory[addr]
            new_val = [state, curr[1]]
            self.cache_memory[addr] = new_val
        else:
            self.cache_memory[addr] = [state, 0]
    

class Core:
    def __init__(self, id: int) -> None:
        self.cache = Cache()
        self.id = id

    def execute(self, inst, core, memory, directory):
        dir_res = directory.get_dir(inst[2])
        state = dir_res[0]
        owner = dir_res[1]
        sharer_list = dir_res[2]

        if inst[1] == "LS":

            if state == "M":

                if sharer_list[self.id] == 1:
                    #pull from current core cache #if self, no need to change state in cache.
                    value = self.cache.get_from_cache(inst[2])
                else:
                    #pull from other core cache #directory state will be M, core cache will be S
                    value = core.cache.get_from_cache(inst[2])
                    self.cache.add_to_cache(inst[2], "S", value)

            elif state == "S":
                if sharer_list[self.id] == 1:
                    #pull from current core cache #if self, no need to change state in cache.
                    value = self.cache.get_from_cache(inst[2])
                else:
                    #pull from other core cache
                    value = core.cache.get_from_cache(inst[2])
                    self.cache.add_to_cache(inst[2], "S", value)
                    sharer_list = sharer_list[:self.id] + "1" + sharer_list[self.id+1:] #update the sharer list on directory
                    directory.set_dir(inst[2], "S", str(self.id), sharer_list)

            elif state == "I":
                value = memory.get_value(int(inst[2]))
                sharer_list = "10" if self.id == "0" else "01"
                directory.set_dir(inst[2], "S", str(self.id), sharer_list)
                self.cache.add_to_cache(inst[2], "S", value)

            else:
                print("Invalid state")
                return

        elif inst[1] == "LM":
            if state == "M":
                if sharer_list.index("1") == self.id:
                    value = self.core.get_from_cache()
                    memory.set_value(int(inst[2]), int(value))
                else:
                    value = core.get_from_cache()
                    memory.set_value(int(inst[2]), int(value))
                    self.cache.add_to_cache()
                sharer_list = "10" if self.id == "0" else "01"
                directory.set_dir(inst[2], "M", str(self.id), sharer_list)

            elif state == "S":
                for i, c in enumerate(sharer_list):
                    if c == "1" and i != self.id:
                        core.cache.change_state(inst[2], "I")
                self.cache.change_state(inst[2], "M")
                sharer_list = sharer_list[:self.id] + "1" + sharer_list[self.id+1:]
                directory.set_dir(inst[2], "M", str(self.id), sharer_list)

            elif state == "I":
                self.cache.change_state(inst[2], "M")
                sharer_list = sharer_list[:self.id] + "1" + sharer_list[self.id+1:]
                directory.set_dir(inst[2], "M", str(self.id), sharer_list) 

            else:
                print("Invalid state")
                return
            
        elif inst[1] == "IN":
            if state == "M":
                if sharer_list.index("1") == self.id:
                    value = self.core.get_from_cache()
                    memory.set_value(int(inst[2]), int(value))
                else:
                    value = core.get_from_cache()
                    memory.set_value(int(inst[2]), int(value))
                    self.cache.add_to_cache()

                directory.set_dir(inst[2], "I", str(self.id), "00")
                
            elif state == "S":
                directory.set_dir(inst[2], "I", str(self.id), "00")
            
            elif state == "I":
                directory.set_dir(inst[2], "I", str(self.id), "00")
                
            else:
                print("Invalid state")
                return

        elif inst[1] == "ADD":
            if state == "M":
                if sharer_list.index("1") == self.id:
                    value = self.core.get_from_cache()
                    memory.set_value(int(inst[2]), int(value)+int(inst[3])) # Make this change for all saves
                else:
                    value = core.get_from_cache()
                    memory.set_value(int(inst[2]), int(value))
                    self.cache.add_to_cache()
                sharer_list = "10" if self.id == "0" else "01"
                directory.set_dir(inst[2], "M", str(self.id), sharer_list)

            elif state == "S":
                for i, c in enumerate(sharer_list):
                    if c == "1" and i != self.id:
                        core.cache.change_state(inst[2], "I")
                self.cache.change_state(inst[2], "M")
                sharer_list = sharer_list[:self.id] + "1" + sharer_list[self.id+1:]
                directory.set_dir(inst[2], "M", str(self.id), sharer_list)

            elif state == "I":
                self.cache.change_state(inst[2], "M")
                sharer_list = sharer_list[:self.id] + "1" + sharer_list[self.id+1:]
                directory.set_dir(inst[2], "M", str(self.id), sharer_list) 

            else:
                print("Invalid state")
                return
            
        else:
            print("Invalid instruction semantic")

    