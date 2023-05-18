from __future__ import annotations


class BreadthFirstSearcher:
    def __init__(self, graph: list[list]):
        self.distanceGraph = []
        self.graph = graph
        self.visited = []
        rowNumber = 0
        for row in graph:
            newRow = []
            colNumber = 0
            for val in row:
                if val == 'S':
                    newRow.append(0)
                    self.visited.append((rowNumber, colNumber))
                    self.freshlyVisited = [(rowNumber, colNumber)]
                else:
                    newRow.append(float('inf'))
                if val == 'E':
                    self.end = (rowNumber, colNumber)
                colNumber += 1
            self.distanceGraph.append(newRow)
            rowNumber += 1
        self.bestPath = []

        self.pathFound = False

    def searchOneStepOut(self):
        freshlyVisitedCopy = self.freshlyVisited.copy()
        self.freshlyVisited = []
        for next in freshlyVisitedCopy:
            distance = self.distanceGraph[next[0]][next[1]]
            for option in getMoveOptions(self.graph, next[0], next[1]):
                if option not in self.visited:
                    self.distanceGraph[option[0]][option[1]] = distance + 1
                    if self.graph[option[0]][option[1]] == 'E':
                        self.pathFound = True
                        return
                    self.freshlyVisited.append((option[0], option[1]))
                    self.visited.append((option[0], option[1]))
                else:
                    currentNodeCanGetToThisOptionMoreEasilyThanExistingWay = self.distanceGraph[option[0]][option[1]] > \
                                                                            self.distanceGraph[next[0]][next[1]] + 1
                    if currentNodeCanGetToThisOptionMoreEasilyThanExistingWay:
                        self.distanceGraph[option[0]][option[1]] = self.distanceGraph[next[0]][next[1]] + 1


def countCharsBetweenChars(destinationChar, currentChar, charMapping=None):
    if charMapping is None:
        charMapping = {}  # Default empty mapping

    # Apply character mapping if available
    currentChar = charMapping.get(currentChar, currentChar)
    destinationChar = charMapping.get(destinationChar, destinationChar)

    if currentChar == destinationChar:
        return 0

    # Calculate the number of characters between char1 and char2
    return ord(destinationChar) - ord(currentChar)



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
    charMapping = {}
    charMapping['S'] = 'a'
    charMapping['E'] = 'z'
    # Get the value of the vertex to the left (if it exists)
    if col > 0:
        if countCharsBetweenChars(graph[row][col - 1], currentChar, charMapping) <= 1:
            adjacent_vertices.append((row, col - 1))

    # Get the value of the vertex above (if it exists)
    if row > 0:
        if countCharsBetweenChars(graph[row - 1][col], currentChar, charMapping) <= 1:
            adjacent_vertices.append((row - 1, col))

    # Get the value of the vertex to the right (if it exists)
    if col < num_cols - 1:
        if countCharsBetweenChars(graph[row][col + 1], currentChar, charMapping) <= 1:
            adjacent_vertices.append((row, col + 1))

    # Get the value of the vertex below (if it exists)
    if row < num_rows - 1:
        if countCharsBetweenChars(graph[row + 1][col], currentChar, charMapping) <= 1:
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

def solvePart1(fileName: str):
    grid = parseGrid(fileName)
    breadthFirstSearcher = BreadthFirstSearcher(grid)
    while not breadthFirstSearcher.pathFound:
        breadthFirstSearcher.searchOneStepOut()
    return breadthFirstSearcher.distanceGraph[breadthFirstSearcher.end[0]][breadthFirstSearcher.end[1]]


def part1(fileName: str):
    print('shortest length to end:', solvePart1(fileName))
# file = 'Day12/data.txt'
# part1(file)
# # part2(file)
