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

    def get_lru_index(self, cache_set):
        if len(cache_set.order) > 0:
            if len(cache_set.order) == 1:
                return 1
            else:
                return cache_set.order[0]
        return 0  # Default to index 0 if order is empty

class L1CacheController:
    def __init__(self, interconnect, num):
        self.cache = L1Cache(2)
        self.interconnect = interconnect
        self.num = num
        
    def setCacheControllerInterconnect(self, interconnect):
        self.interconnect = interconnect
    
    def getDirectory(self, addr):
        return self.interconnect.get_directoryLine(addr)
    
    def read(self, addr, token = 0):
        self.cache.access += 1
        ind = addr % len(self.cache.sets)
        tag = addr // len(self.cache.sets)

        cache_set = self.cache.sets[ind]
        line_index = cache_set.find(tag)

        if line_index != -1:  # Cache hit
            self.cache.hits += 1
            return cache_set.cache_lines[line_index]['data']
        elif token == 1:
            return None
        else:  # Cache miss
            # Simulate fetching data from lower memory (not implemented)
            # data = f"Data from address {addr} in main memory"
            
            data = self.interconnect.read_from_memory(addr) 

            # Update cache with the fetched data using LRU policy
            line_index = self.cache.get_lru_index(cache_set)
            print("lru addr: ", line_index)
            cache_set.update(line_index, tag, data)
            return data
        
    def write(self, addr, data):
        self.cache.access += 1
        ind = addr % len(self.cache.sets)
        tag = addr // len(self.cache.sets)

        cache_set = self.cache.sets[ind]
        line_index = cache_set.find(tag)

        if line_index != -1:  # Cache hit
            cache_set.cache_lines[line_index]['data'] = data
            # Simulate writing through to main memory
            self.cache.hits+=1
            #TODO make main memory global
            
            self.interconnect.write_to_memory(addr,  data)  # Write to main memory immediately
        else:  # Cache miss
            # Simulate fetching data from lower memory (not implemented)
            # Update cache with the fetched data using LRU policy
            line_index = self.cache.get_lru_index(cache_set)
            cache_set.update(line_index, tag, data)
            # Simulate writing through to main memory
            self.interconnect.write_to_memory(addr,  data)  # Write to main memory immediately
        return data

    def getShared(self, addr):
        line = self.getDirectory(addr)
        state = line['state']
        owner = line['owner']
        sharer_list = line['sharer_list']
        # print(line)
        # self.interconnect.test()
        if state != 2 and owner == self.num:
            return self.read(addr)
        
        elif state == 2:
            line['state'] = 1
            line['sharer_list'] = [0,0,0,0]
            line['sharer_list'][self.num] = 1
            self.interconnect.set_directoryLine(line)
            value = self.interconnect.read_from_memory(addr)
            return self.write(addr, value)
            
        elif state == 1:
            sharer = line['sharer_list'].index(1)
            value, from_core = self.interconnect.getValueFromCore(addr, sharer)
            line['sharer_list'][self.num] = 1
            self.interconnect.set_directoryLine(line)
            return self.write(addr, value)
            
        elif state == 0:
            value,from_core = self.interconnect.getValueFromCore(addr,owner)
            line['state'] = 3
            line['sharer_list'][self.num] = 1
            self.interconnect.set_directoryLine(line)
            return self.write(addr, value)

        elif state == 3:
            value,from_core = self.interconnect.getValueFromCore(addr,owner)
            line['sharer_list'][self.num] = 1
            self.interconnect.set_directoryLine(line)
            return self.write(addr, value)
            

    def getModified(self, addr, immediate = None):
        pass
    
    def putInvalid(self, addr):
        line = self.getDirectory(addr)
        line['state'] = 2
        line['sharer_list'] = [0,0,0,0]
        self.interconnect.set_directoryLine(line, addr)
    
    
    