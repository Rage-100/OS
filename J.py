pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]


def optimal(capacity):
    frames = []
    faults = 0
    hits = 0

    print("\nOPTIMAL PAGE REPLACEMENT")
    print("Number of Frames:", capacity)
    print("Page\tFrames\t\tStatus")

    for i in range(len(pages)):
        page = pages[i]

        if page in frames:
            hits += 1
            status = "Hit"

        else:
            faults += 1

            if len(frames) < capacity:
                frames.append(page)

            else:
                future = pages[i + 1:]

                replace_page = -1
                farthest = -1

                for p in frames:
                    if p not in future:
                        replace_page = p
                        break

                    else:
                        next_use = future.index(p)

                        if next_use > farthest:
                            farthest = next_use
                            replace_page = p

                frames[frames.index(replace_page)] = page

            status = "Fault"

        print(page, "\t", frames, "\t", status)

    print("\nTotal Page Faults:", faults)
    print("Total Page Hits:", hits)
    print("Hit Ratio:", hits / len(pages))
    print("Hit Ratio (%):", (hits / len(pages)) * 100)


# Simulation for 3 frames
optimal(3)

# Simulation for 4 frames
optimal(4)
