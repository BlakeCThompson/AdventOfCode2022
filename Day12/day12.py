from __future__ import annotations


def countCharsBetweenChars(char1, char2):
    if char1 == char2:
        return 0
    char1, char2 = min(char1, char2), max(char1, char2)
    return len([char for char in range(ord(char1) + 1, ord(char2)) if chr(char).isalpha()])


def getMoveOptions(graph, row, col):
    """
    Given a two-dimensional list representing a graph and a tuple (row, col) representing
    the index of a vertex in the graph, return a list of the values of the vertices that
    are adjacent to the vertex at the given index.
    """
    adjacent_vertices = []
    num_rows = len(graph)
    num_cols = len(graph[0])

    currentChar = graph[row][col]

    # Get the value of the vertex to the left (if it exists)
    if col > 0:
        if countCharsBetweenChars(graph[row][col - 1], currentChar) <= 1:
            adjacent_vertices.append((row, col - 1))

    # Get the value of the vertex above (if it exists)
    if row > 0:
        if countCharsBetweenChars(graph[row - 1][col], currentChar) <= 1:
            adjacent_vertices.append((row - 1, col))

    # Get the value of the vertex to the right (if it exists)
    if col < num_cols - 1:
        if countCharsBetweenChars(graph[row][col + 1], currentChar) <= 1:
            adjacent_vertices.append((row, col + 1))

    # Get the value of the vertex below (if it exists)
    if row < num_rows - 1:
        if countCharsBetweenChars(graph[row + 1][col], currentChar) <= 1:
            adjacent_vertices.append((row + 1, col))

    return adjacent_vertices


def parseGrid(fileName):
    ioStream = open(fileName, 'r')
    rows = []
    endsWithNewline = False
    for line in ioStream:
        currentList = []
        for char in line:
            if char != '\n':
                currentList.append(char)
                endsWithNewline = False
                continue
            endsWithNewline = True
            rows.append(currentList)
            currentList = []
        if not endsWithNewline:
            rows.append(currentList)

    ioStream.close()
    return rows


def getBestMove(moveOptions, end):
    closestOption = None
    closestDistance = float('inf')
    for moveOption in moveOptions:
        optionDistance = getDistanceBetweenCoordinates(moveOption, end)
        if closestDistance > optionDistance:
            closestDistance = optionDistance
            closestOption = moveOption
    return closestOption

def getEnd(grid):
    for rowIndex, row in enumerate(grid):
        for colIndex, col in enumerate(row):
            if col == 'E':
                return rowIndex, colIndex
def getDistanceBetweenCoordinates(start, end):
    # Get the row and column indices for the start and end coordinates
    start_row, start_col = start
    end_row, end_col = end

    # Calculate the difference in rows and columns
    row_diff = abs(start_row - end_row)
    col_diff = abs(start_col - end_col)

    # Return the total distance (number of moves)
    return row_diff + col_diff

def part1(fileName: str):
    ioStream = open(fileName, 'r')
    pass
# file = 'Day11/data.txt'
# part1(file)
# part2(file)
