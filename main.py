from Core import Core
from Interconnect import Interconnect
from directory import DirectoryController
import matplotlib.pyplot as plt

def main():

    instructions = []

    dir_control = DirectoryController()
    
    cores = [Core(None, i) for i in range(4)]
    
    interconnect = Interconnect(dir_control, cores)

    with open("instructions.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            val = i.split(" ")
            if len(val) == 3:
                val[2] = val[2][:-1]
            else:
                val[3] = val[3][:-1]
            instructions.append(val)   
    
    print("-"*50)
    print("Starting execution")
    print("-"*50)

    for ins in instructions:
        core = int(ins[0])
        # print(core)
        cores[core].interpret_instruction(ins[1:])
    
    print("-"*50)
    print("Execution complete")
    print("-"*50)

    cache_informations = [] #access, hits, miss

    for i in range(4):
        file_name = f"core_dump/cache_dump_core_{i}"
        curr_core = cores[i]
        cache_informations.append([
            curr_core.cache_controller.cache.access, 
            curr_core.cache_controller.cache.hits, 
            curr_core.cache_controller.cache.access - curr_core.cache_controller.cache.hits
            ])
        core_dump = curr_core.cache_memory_dump
        with open(file_name, 'w') as file:
            for dump in core_dump:
                file.write(str(dump) + "\n")
        print(f"Core dump for core {i} created at {file_name}")

    # print(cache_informations)

    dir_dump = open("core_dump/dir_dump_normal", "w")
    dir_dump_bin = open("core_dump/dir_dump_bin", "w")
    convert = {0:"00", 1:"01", 2:"10", 3:"11"}

    for dump in interconnect.directory_memory_dump:
        state = convert[dump[1]['state']]
        owner = convert[dump[1]['owner']]
        sharer_list = ''.join([str(item) for item in dump[1]['sharer_list']])
        line = state + owner + sharer_list
        dir_dump.write(str(dump) + "\n")
        dir_dump_bin.write(line + "\n")

    print(f"Core dump for directory created at core_dump/dir_dump_normal")
    print(f"Core dump for directory (binary) created at core_dump/dir_dump_bin")
    dir_dump.close()
    dir_dump_bin.close()

    with open("core_dump/main_mem_dump", "w") as file:
        for main_dump in interconnect.main_memory_dump:
            file.write(str(main_dump) + "\n")
    print("Core dump for main memory created at: core_dump/main_mem_dump")

    miss_penalty = 2
    hit_time = 1

    miss_rates = []
    access_latency = []
    
    for core_info in cache_informations:
        accesses, hits, misses = core_info
        miss_rate = misses / accesses
        miss_rates.append(miss_rate)
        
        latency = (hits * hit_time + misses * miss_penalty * hit_time) / accesses
        access_latency.append(latency)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.bar(range(len(miss_rates)), miss_rates)
    plt.xlabel('Cores')
    plt.ylabel('Miss Rate')
    plt.title('Miss Rates for Each Core')

    plt.subplot(1, 2, 2)
    plt.bar(range(len(access_latency)), access_latency)
    plt.xlabel('Cores')
    plt.ylabel('Average Memory Access Latency')
    plt.title('Average Memory Access Latency for Each Core')

    plt.tight_layout()
    plt.savefig('plots/memory_metrics.png') 
    plt.close()
    print("Plot for Average Memory Access Latency for Each Core saved at plots/memory_metrics.png")

    directory_updates = interconnect.dir_updates 
    time = list(range(len(directory_updates)))

    plt.figure(figsize=(8, 5))
    plt.plot(time, directory_updates, marker='o', linestyle='-')
    plt.xlabel('Time (Clock Cycles)')
    plt.ylabel('Number of Directory Updates')
    plt.title('Directory Updates Over Time')
    plt.grid(True)
    plt.savefig('plots/dir_updates.png') 
    plt.close()
    print("Plot for Directory Updates Over Time saved at plots/dir_updates.png")
        
if __name__ == '__main__':
    main()