# main_program.py

from module1 import read_memory, write_memory
from module2 import inspect_memory, clear_memory

# Access and modify shared memory using module1
write_memory(3, 42)
print(read_memory(3))  # Output: 42

# Access shared memory using module2
print(inspect_memory())  # Output: [0, 0, 0, 42, 0, ...]

# Modify shared memory using module2
clear_memory()
print(inspect_memory())  # Output: [0, 0, 0, 0, 0, ...]

write_memory(1, 1000)
print(inspect_memory())
