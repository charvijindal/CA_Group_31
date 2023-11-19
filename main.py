from Core import Core
from Interconnect import Interconnect
from directory import DirectoryController

def main():

    instructions = []

    dir_control = DirectoryController()
    interconnect = Interconnect(dir_control)
    
    cores = [Core(interconnect, i) for i in range(4)]

    with open("instructions.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            val = i.split(" ")
            if len(val) == 3:
                val[2] = val[2][:-1]
            else:
                val[3] = val[3][:-1]
            instructions.append(val)   
    
    for ins in instructions:
        core = int(ins[0])
        print(core)
        cores[core].interpret_instruction(ins[1:])

if __name__ == '__main__':
    main()