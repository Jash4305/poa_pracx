def best_fit(blocks, processes):
    allocation = [-1] * len(processes)  # Initialize allocation list with -1 (unallocated)

    for i, process in enumerate(processes):
        best_index = -1
        min_size = float('inf')  # Initialize minimum size to infinity
        for j, block in enumerate(blocks):
            if block >= process and block < min_size and allocation.count(j) == 0:
                best_index = j
                min_size = block
        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= process  # Update block size

    return allocation

def main():
    processes = [212, 417, 112, 426]  # Processes to be allocated
    blocks = [100, 200, 300, 400]  # Available memory blocks

    allocation = best_fit(blocks, processes)

    print("Process No. \t Process Size \t Block No.")
    for i in range(len(processes)):
        print(i+1, "\t\t", processes[i], "\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == "__main__":
    main()
