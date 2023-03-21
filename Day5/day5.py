

def parseCratesInitialState(crateRows:list):
    """
    :param crateRows: list of string representations of the state of a row of crates
    e.g. [N]     [F] [M]     [D] [V] [R] [N]
    where N is the crate in row 1, no crate exists in row two, F is in row three, and so on.
    :return: a list of strings, with each string representing the STACK of crates in ascending order from ground up.
    """
    # The formula for finding the length of a row given the number of crates is length = s*n-1, where n is the number of crates
    # and "s" is the size of the crate representation, including the space between it and the preceding crate. In our case, 4
    # so the formula for finding the number of crates given the n = (length +1)/s
    crateRepresentationSize = 4
    crateStacksCount = (len(crateRows[0])) / crateRepresentationSize
    crateStacks = []
    for crateIndex, crateRow in enumerate(crateRows):
        crateRow = crateRows[crateIndex]
        for stackIndex, columnIndex in enumerate(range(1, len(crateRow), 4)):
            crateChar = crateRow[columnIndex]
            isStartOfNewStack = stackIndex+1 > len(crateStacks)
            if isStartOfNewStack:
                if crateChar == ' ':
                    crateStacks.append('')
                    continue
                crateStacks.append(crateChar)
                continue
            crateStacks[stackIndex] += crateChar
    return crateStacks




def part1():
    data = open("Day5/data.txt", "r")

    print("part 1:")
    # Every item in the range is a tuple of a low and high range.
    # Need to look at each pair, and see if one is a superset of the other.

    crateRows = []
    for line in data:
        crateIndexLineReached = line[1] == '1'
        if crateIndexLineReached:
            break
        crateRows.append(line)
    crateStacks = parseCratesInitialState(crateRows)

    print("number of superset pairs:")

    data.close()


part1()
