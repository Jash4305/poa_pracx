def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)  

    for i, process in enumerate(processes):
        worst_index = -1
        max_size = -1  
        for j, block in enumerate(blocks):
            if block >= process and allocation[j] == -1:
                if block > max_size:
                    worst_index = j
                    max_size = block
        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= process  

    return allocation

def main():
    processes = [212, 417, 112, 426]  
    blocks = [100, 200, 300, 400]  

    allocation = worst_fit(blocks, processes)

    print("Process No. \t Process Size \t Block No.")
    for i in range(len(processes)):
        print(i+1, "\t\t", processes[i], "\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == "__main__":
    main()
