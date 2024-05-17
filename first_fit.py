def first_fit(blocks, processes):
    allocation = [-1] * len(processes)  # Initialize allocation list with -1 (unallocated)

    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i] and allocation[i] == -1:
                allocation[i] = j  # Allocate process i to block j
                break

    return allocation

def main():
    processes = []
    blocks = []
    # Get user inputs for number of blocks and processes
    num_blocks = int(input("Enter the number of blocks: "))
    num_processes = int(input("Enter the number of processes: "))

    for i in range(num_blocks):
        block_size = int(input(f"Enter the size of block {i+1}: "))
        blocks.append(block_size)

    for i in range(num_processes):
        process_size = int(input(f"Enter the size of process {i+1}: "))
        processes.append(process_size)

    # Call the first_fit function and get the allocation result
    allocation = first_fit(blocks, processes)

    print("Process No. \t Process Size \t Block No.")
    for i in range(len(processes)):
        print(i+1, "\t\t", processes[i], "\t\t", end="")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")

if __name__ == "__main__":
    main()
