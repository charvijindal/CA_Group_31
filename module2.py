# module2.py

# Import the shared memory array from the memory module
from memory import memory_array

# Access and modify the shared memory array
def inspect_memory():
    return memory_array

# Modify the shared memory array
def clear_memory():
    for i in range(len(memory_array)):
        memory_array[i] = 0
