import random
from update_memory import read_memory, write_memory, inspect_memory

class CacheSet:
    def __init__(self) -> None:
        self.cache_lines = [None, None]  # 2-way set associative
        self.order = []  # 0th index least recently used

    def find(self, tag):
        for i in range(len(self.cache_lines)):
            if self.cache_lines[i] is not None and self.cache_lines[i]['tag'] == tag:
                self.order.remove(i)
                self.order.append(i)
                print("order: ", self.order)
                return i
        print("find:" ,self.cache_lines)
        print("order: ", self.order)
        return -1

    def update(self, index, tag, data):
        if self.cache_lines[index] is None:
            if len(self.order) >= len(self.cache_lines):
                evict_idx = self.order.pop(0)
                self.cache_lines[evict_idx] = None
            self.order.append(index)
        else:
            self.order.remove(index)
            self.order.append(index)
        self.cache_lines[index] = {'tag': tag, 'data': data}
        print("update", self.cache_lines)
        print("order: ", self.order)
        

class L1Cache:
    def __init__(self, sets) -> None:
        self.sets = [CacheSet() for _ in range(sets)]
        self.hits = 0
        self.access = 0

    def read(self, addr):
        self.access += 1
        ind = addr % len(self.sets)
        tag = addr // len(self.sets)

        cache_set = self.sets[ind]
        line_index = cache_set.find(tag)

        if line_index != -1:  # Cache hit
            self.hits += 1
            return cache_set.cache_lines[line_index]['data']
        else:  # Cache miss
            # Simulate fetching data from lower memory (not implemented)
            # data = f"Data from address {addr} in main memory"
            
            data = read_memory(addr) #TODO update main memory to global main

            # Update cache with the fetched data using LRU policy
            line_index = self.get_lru_index(cache_set)
            print("lru addr: ", line_index)
            cache_set.update(line_index, tag, data)
            return data

    def write(self, addr, data):
        self.access += 1
        ind = addr % len(self.sets)
        tag = addr // len(self.sets)

        cache_set = self.sets[ind]
        line_index = cache_set.find(tag)

        if line_index != -1:  # Cache hit
            cache_set.cache_lines[line_index]['data'] = data
            # Simulate writing through to main memory
            self.hits+=1
            #TODO make main memory global
            
            write_memory(addr, data)  # Write to main memory immediately
        else:  # Cache miss
            # Simulate fetching data from lower memory (not implemented)
            # Update cache with the fetched data using LRU policy
            line_index = self.get_lru_index(cache_set)
            cache_set.update(line_index, tag, data)
            # Simulate writing through to main memory
            write_memory(addr, data)  # Write to main memory immediately

    def get_lru_index(self, cache_set):
        if len(cache_set.order) > 0:
            if len(cache_set.order) == 1:
                return 1
            else:
                return cache_set.order[0]
        return 0  # Default to index 0 if order is empty

class L1CacheController:
    def __init__(self, cache):
        self.cache = cache

    def read(self, addr):
        return self.cache.read(addr)

    def write(self, addr, data):
        self.cache.write(addr, data)

# cache = L1Cache(2)

# # Create an instance of L1CacheController
# cache_controller = L1CacheController(cache)

# # Read and write operations for testing
# for i in range(20):
#     address = random.randint(0, 63)
#     data = random.randint(0, 256)
#     print(f"Performing read from address {address}:")
#     print("Data read:", cache_controller.read(address))
#     print("Main: ", inspect_memory())
#     print()
#     print(f"Performing write to address {address}:")
#     cache_controller.write(address, data)
#     print("Main after write: ", inspect_memory())
#     print()
# # Access cache hits and misses directly through the cache instance
# print("Cache hits:", cache.hits)
# print("Cache access:", cache.access)
# print("Cache misses:", cache.access - cache.hits)
