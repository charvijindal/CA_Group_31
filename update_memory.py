from memory import memory_array

def read_memory(location):
    return memory_array[location]

def write_memory(location, value):
    memory_array[location] = value

def inspect_memory():
    return memory_array

