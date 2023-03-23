def parseCratesInitialState(crateRows: list):
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
    for crateRow in crateRows:
        updateStacks(crateStacks, crateRow)
    return crateStacks


def updateStacks(crateStacks, crateRow):
    for stackIndex, columnIndex in enumerate(range(1, len(crateRow), 4)):
        crateChar = crateRow[columnIndex]
        isStartOfNewStack = stackIndex + 1 > len(crateStacks)
        if isStartOfNewStack:
            if crateChar == ' ':
                crateStacks.append('')
                continue
            crateStacks.append(crateChar)
            continue
        if crateChar == ' ':
            continue
        crateStacks[stackIndex] += crateChar


def executeMovesFromLines(lines, crateStacks, moveCratesAllAtOnce=False):
    """
    execute moves on columns of crates, and return the altered crates' state.
    :param lines:
    :param crateStacks:
    :return:
    """
    for line in lines:
        if line == '\n':
            continue
        spaceDelineatedMove = line.split(' ')
        quantity = spaceDelineatedMove[1]
        fromColumn = spaceDelineatedMove[3]
        toColumn = spaceDelineatedMove[5].strip('\n')
        executeMove(crateStacks, int(quantity), int(fromColumn), int(toColumn), moveCratesAllAtOnce)
    return crateStacks


def executeMove(crateStacks: list, quantity: int, fromColumn: int, toColumn: int, moveAllAtOnce=False):
    movedCrates = crateStacks[fromColumn - 1][:quantity]
    length = len(crateStacks[fromColumn - 1])
    crateStacks[fromColumn - 1] = crateStacks[fromColumn - 1][quantity:]
    if not moveAllAtOnce:
        movedCrates = movedCrates[::-1]
    crateStacks[toColumn - 1] = movedCrates + crateStacks[toColumn - 1]


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
    moves = []
    for line in data:
        moves.append(line)
    executeMovesFromLines(moves, crateStacks)
    stackTops = ''
    for stackIndex, crateStack in enumerate(crateStacks):
        if len(crateStack) > 0:
            stackTops += crateStack[0]
            print("Top of stack ", str(stackIndex + 1), ":", crateStack[0])
    print(stackTops)
    data.close()


def part2():
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
    moves = []
    for line in data:
        moves.append(line)
    executeMovesFromLines(moves, crateStacks, True)
    stackTops = ''
    for stackIndex, crateStack in enumerate(crateStacks):
        if len(crateStack) > 0:
            stackTops += crateStack[0]
            print("Top of stack ", str(stackIndex + 1), ":", crateStack[0])
    print(stackTops)
    data.close()


part1()

part2()