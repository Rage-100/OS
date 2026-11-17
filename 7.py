# Banker's Algorithm for Deadlock Avoidance

# Number of processes and resources
n = 5
m = 3

# Allocation Matrix
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Maximum Matrix
maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

# Available Resources
available = [3, 3, 2]

# Calculate Need Matrix
need = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

print("Need Matrix:")
for i in range(n):
    print("P", i, ":", need[i])


# Safety Algorithm
def safety(alloc, need, avail):

    work = avail.copy()
    finish = [False] * n
    safe_sequence = []

    while len(safe_sequence) < n:

        found = False

        for i in range(n):

            if not finish[i]:

                if all(need[i][j] <= work[j]
                       for j in range(m)):

                    for j in range(m):
                        work[j] += alloc[i][j]

                    safe_sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            break

    if all(finish):
        return True, safe_sequence
    else:
        return False, safe_sequence


# Check system safety
safe, sequence = safety(allocation, need, available)

if safe:
    print("\nSystem is in SAFE state")
    print("Safe Sequence:",
          " -> ".join("P" + str(i) for i in sequence))
else:
    print("\nSystem is NOT in SAFE state")


# Resource Request by P1
process = 1
request = [1, 0, 2]

print("\nRequest by P1:", request)

# Check request conditions
if all(request[j] <= need[process][j] for j in range(m)):

    if all(request[j] <= available[j] for j in range(m)):

        # Temporarily allocate resources
        for j in range(m):
            available[j] -= request[j]
            allocation[process][j] += request[j]
            need[process][j] -= request[j]

        # Check safety after allocation
        safe, new_sequence = safety(
            allocation, need, available
        )

        if safe:
            print("Request CAN be granted immediately.")
            print("New Safe Sequence:",
                  " -> ".join(
                      "P" + str(i) for i in new_sequence
                  ))
        else:
            print("Request CANNOT be granted.")
            
            # Rollback allocation
            for j in range(m):
                available[j] += request[j]
                allocation[process][j] -= request[j]
                need[process][j] += request[j]

    else:
        print("Request cannot be granted: Resources unavailable.")

else:
    print("Request exceeds the process's Need.")
