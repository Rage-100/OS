pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3,
         0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

capacity = 3

def FIFO():
    frames = []
    pointer = 0
    faults = 0
    hits = 0

    print("\nFIFO PAGE REPLACEMENT")
    print("Page\tFrames\t\tStatus")

    for page in pages:
        if page in frames:
            hits += 1
            status = "Hit"
        else:
            faults += 1

            if len(frames) < capacity:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % capacity

            status = "Fault"

        print(page, "\t", frames, "\t", status)

    print("Total Page Faults:", faults)
    print("Total Page Hits:", hits)
    print("Hit Ratio:", hits / len(pages))


def LRU():
    frames = []
    last_used = {}
    faults = 0
    hits = 0

    print("\nLRU PAGE REPLACEMENT")
    print("Page\tFrames\t\tStatus")

    for time, page in enumerate(pages):
        if page in frames:
            hits += 1
            status = "Hit"
        else:
            faults += 1

            if len(frames) < capacity:
                frames.append(page)
            else:
                least_used = min(frames, key=lambda x: last_used[x])
                frames[frames.index(least_used)] = page

            status = "Fault"

        last_used[page] = time
        print(page, "\t", frames, "\t", status)

    print("Total Page Faults:", faults)
    print("Total Page Hits:", hits)
    print("Hit Ratio:", hits / len(pages))


FIFO()
LRU()
