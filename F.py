# Memory Allocation Strategies

partitions = [100, 500, 200, 300, 600]

processes = [212, 417, 112, 426]


# Function for First Fit, Best Fit and Worst Fit
def memory_allocation(strategy):

    allocated = [False] * len(partitions)

    print("\n", strategy, "Allocation")
    print("--------------------------------")

    total_fragmentation = 0

    for i in range(len(processes)):

        process = processes[i]
        index = -1

        # Find suitable memory partition
        for j in range(len(partitions)):

            if not allocated[j] and partitions[j] >= process:

                if strategy == "First Fit":
                    index = j
                    break

                elif strategy == "Best Fit":

                    if index == -1 or partitions[j] < partitions[index]:
                        index = j

                elif strategy == "Worst Fit":

                    if index == -1 or partitions[j] > partitions[index]:
                        index = j

        # Allocate memory
        if index != -1:

            allocated[index] = True

            fragmentation = partitions[index] - process

            total_fragmentation += fragmentation

            print("P", i + 1, "(", process, "KB )",
                  "-> Partition", index + 1,
                  "(", partitions[index], "KB )",
                  "Fragmentation:", fragmentation, "KB")

        else:

            print("P", i + 1, "(", process,
                  "KB ) -> Not Allocated")

    # Display unallocated processes
    print("\nTotal Internal Fragmentation:",
          total_fragmentation, "KB")


# Execute all three strategies
memory_allocation("First Fit")

memory_allocation("Best Fit")

memory_allocation("Worst Fit")
