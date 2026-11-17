# CPU Scheduling: Round Robin and Priority

processes = [
    ("P1", 10, 3),
    ("P2", 1, 1),
    ("P3", 2, 4),
    ("P4", 1, 5),
    ("P5", 5, 2)
]

# Round Robin Scheduling
def round_robin(processes, quantum):

    remaining = {p[0]: p[1] for p in processes}
    completion = {}
    gantt = []
    queue = [p[0] for p in processes]
    time = 0

    while queue:
        p = queue.pop(0)

        start = time
        execute = min(quantum, remaining[p])

        time += execute
        remaining[p] -= execute

        gantt.append((p, start, time))

        if remaining[p] > 0:
            queue.append(p)
        else:
            completion[p] = time

    print("\nROUND ROBIN SCHEDULING")
    print("Gantt Chart:")

    for p, start, end in gantt:
        print("|", p, end=" ")
    print("|")

    print("0", end="")
    for p, start, end in gantt:
        print("    ", end)
    print()

    display_results(processes, completion)


# Priority Scheduling (Non-Preemptive)
def priority_scheduling(processes):

    order = sorted(processes, key=lambda x: x[2])

    time = 0
    completion = {}
    gantt = []

    for p, bt, priority in order:

        start = time
        time += bt

        completion[p] = time
        gantt.append((p, start, time))

    print("\nPRIORITY SCHEDULING")
    print("Gantt Chart:")

    for p, start, end in gantt:
        print("|", p, end=" ")
    print("|")

    print("0", end="")
    for p, start, end in gantt:
        print("    ", end)
    print()

    display_results(processes, completion)


# Display CT, TAT and WT
def display_results(processes, completion):

    total_wt = 0
    total_tat = 0

    print("\nProcess\tBT\tCT\tTAT\tWT")

    for p, bt, priority in processes:

        ct = completion[p]
        tat = ct
        wt = tat - bt

        total_tat += tat
        total_wt += wt

        print(f"{p}\t{bt}\t{ct}\t{tat}\t{wt}")

    n = len(processes)

    print("\nAverage Waiting Time:", total_wt / n)
    print("Average Turnaround Time:", total_tat / n)


# Execute both algorithms
round_robin(processes, 3)
priority_scheduling(processes)
