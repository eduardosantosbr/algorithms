# greedy algorithms of maximum allocation

def maximumAllocation(programs, space, maxStorage):
    programs = sorted(programs, key=lambda x: space[x])

    programsAllocated = []
    i = 0
    while i < len(programs):
        if (maxStorage >= space[programs[i]]):
            programsAllocated.append(programs[i])
            maxStorage -= space[programs[i]]
        i += 1
    return programsAllocated


def main():
    programs = ["a", "b", "c", "d", "e"]
    space = {"a": 90, "b": 25, "c": 15, "d": 10, "e": 5}
    maxStorage = 100
    programsAllocated = maximumAllocation(
        programs, space, maxStorage)
    print("Programs added to disk: " +
          str(len(programsAllocated))+": "+str(programsAllocated))


if __name__ == "__main__":
    main()
