# CPU Scheduling: FCFS and SJF

processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3),
    ("P5", 4, 4)
]


# Function to calculate scheduling results
def calculate(process_list, algorithm):

    if algorithm == "FCFS":
        order = sorted(process_list, key=lambda x: x[1])

    else:
        pending = sorted(process_list, key=lambda x: x[1])
        order = []
        ready = []
        time = 0

        while pending or ready:

            while pending and pending[0][1] <= time:
                ready.append(pending.pop(0))

            if not ready:
                time = pending[0][1]
                continue

            shortest = min(ready, key=lambda x: x[2])
            ready.remove(shortest)
            order.append(shortest)
            time += shortest[2]

    # Calculate CT, TAT and WT
    time = 0
    results = {}
    gantt = []

    for name, at, bt in order:

        if time < at:
            time = at

        start = time
        time = time + bt
        ct = time
        tat = ct - at
        wt = tat - bt

        results[name] = (ct, tat, wt)
        gantt.append((name, start, time))

    # Display Gantt Chart
    print("\n", algorithm, "Gantt Chart")

    for name, start, end in gantt:
        print(f"|  {name}  ", end="")
    print("|")

    print("0", end="")
    for name, start, end in gantt:
        print(f"      {end}", end="")
    print()

    # Display process table
    print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

    for name, at, bt in process_list:
        ct, tat, wt = results[name]
        print(f"{name}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    avg_wt = sum(r[2] for r in results.values()) / len(results)
    avg_tat = sum(r[1] for r in results.values()) / len(results)

    print("\nAverage Waiting Time:", avg_wt)
    print("Average Turnaround Time:", avg_tat)


# Execute both algorithms
calculate(processes, "FCFS")
calculate(processes, "SJF")
