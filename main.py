from memory import Memory
from core import Core
from directory import Directory

def main():

    memory = Memory()
    core1 = Core(0)
    core2 = Core(1)
    directory = Directory(memory)

    instructions = []
    
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
        if ins[0] == "0":
            core1.execute(ins, core2, memory, directory)
        elif ins[0] == "1":
            core2.execute(ins, core1, memory, directory)
        else:
            print("Invalid instruction")
            
    print(instructions)

if __name__ == "__main__":
    main()