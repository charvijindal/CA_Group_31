# module1.py

# Import the shared memory array from the memory module
from memory import memory_array

# Access and modify the shared memory array
def read_memory(location):
    return memory_array[location]

def write_memory(location, value):
    memory_array[location] = value
