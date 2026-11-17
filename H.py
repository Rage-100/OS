n = 4
m = 3

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 3],
    [2, 1, 1]
]

maximum = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 6],
    [2, 2, 2]
]

available = [3, 3, 2]

# Calculate Need Matrix
need = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(maximum[i][j] - allocation[i][j])
    need.append(row)

print("NEED MATRIX")
for i in range(n):
    print("P", i, ":", need[i])


# Safety Algorithm
def safety(alloc, need, avail):
    work = avail.copy()
    finish = [False] * n
    sequence = []

    while len(sequence) < n:
        found = False

        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):

                    for j in range(m):
                        work[j] += alloc[i][j]

                    sequence.append(i)
                    finish[i] = True
                    found = True

        if not found:
            break

    if all(finish):
        return True, sequence
    else:
        return False, sequence


# Check Initial Safe State
safe, seq = safety(allocation, need, available)

print("\nINITIAL STATE")

if safe:
    print("System is SAFE")
    print("Safe Sequence:",
          " -> ".join("P" + str(i) for i in seq))
else:
    print("System is UNSAFE")


# Resource Request Algorithm
def request_resources(process, request):

    print("\nRequest by P" + str(process), ":", request)

    # Check request <= Need
    if not all(request[j] <= need[process][j] for j in range(m)):
        print("DENIED: Request exceeds the process Need.")
        return

    # Check request <= Available
    if not all(request[j] <= available[j] for j in range(m)):
        print("DENIED: Resources are not available.")
        return

    # Temporarily allocate resources
    for j in range(m):
        available[j] -= request[j]
        allocation[process][j] += request[j]
        need[process][j] -= request[j]

    # Check safety after temporary allocation
    safe, seq = safety(allocation, need, available)

    if safe:
        print("GRANTED: System remains SAFE.")
        print("New Safe Sequence:",
              " -> ".join("P" + str(i) for i in seq))
    else:
        print("DENIED: Request makes the system UNSAFE.")

        # Rollback the temporary allocation
        for j in range(m):
            available[j] += request[j]
            allocation[process][j] -= request[j]
            need[process][j] += request[j]


# Test each request independently
request_resources(1, [1, 0, 2])
request_resources(0, [0, 2, 0])
request_resources(2, [4, 0, 1])
