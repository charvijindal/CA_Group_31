import random

class Cache:
    def __init__(self, cache_size=4):
        self.cache_size = cache_size
        self.cache_memory = {}

    def add_to_cache(self, addr, value):
        # Check if cache is full
        if len(self.cache_memory) >= self.cache_size:
            # If cache is full, remove a random item
            self.remove_random()
        self.cache_memory[addr] = value

    def remove_random(self):
        # Find and remove a random item from the cache
        if self.cache_memory:
            random_key = random.choice(list(self.cache_memory.keys()))
            del self.cache_memory[random_key]

    def get_from_cache(self, addr):
        # Get value from cache if present, otherwise return None
        return self.cache_memory.get(addr, None)

class Core:
    def __init__(self, id: int) -> None:
        self.cache = Cache()
        self.id = id

    def set_invalid(self, inst, memory, directory):
        self.cache.add_to_cache(inst[2], memory.get_value(inst[2]))
        sharer_list = [0, 0]
        sharer_list[self.id] = 1
        directory.set_dir(inst[2], "S", self.id, "".join(sharer_list))

    def execute(self, inst, core, memory, directory):
        dir_res = directory.get_dir(inst[2])
        state = dir_res[0]
        owner = dir_res[1]
        sharer_list = dir_res[2]

        if inst[1] == "LS":

            if state == "M":
                
            elif state == "S":
                
            elif state == "I":
                self.set_invalid(inst, memory, directory)

            else:
                print("Invalid state")
                return

        elif inst[1] == "LM":
            if state == "M":
                
            elif state == "S":
                
            elif state == "I":
                self.set_invalid(inst, memory, directory)

            else:
                print("Invalid state")
                return
            
        elif inst[1] == "IN":
            if state == "M":
                
            elif state == "S":
            
            elif state == "I":
                self.set_invalid(inst, memory, directory)
            else:
                print("Invalid state")
                return

        elif inst[1] == "ADD":
            if state == "M":
                
            elif state == "S":
            
            elif state == "I":
                self.set_invalid(inst, memory, directory)
            else:
                print("Invalid state")
                return
            
        else:
            print("Invalid instruction semantic")

    