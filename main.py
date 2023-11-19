from Core import Core
from Interconnect import Interconnect

def main():

    instructions = []
    interconnect = Interconnect()
    cores = [Core(interconnect) for _ in range(4)]

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