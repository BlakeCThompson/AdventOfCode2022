
class Point:
    xCoord: int
    yCoord: int
    def __init__(self, xCoord: int, yCoord: int):
        self.xCoord = xCoord
        self.yCoord = yCoord


def isHigherThanAllWest(point: Point, grid):
    pointOfInterestValue = grid[point.yCoord][point.xCoord]
    for valueToTheWest in grid[point.yCoord][1:point.xCoord - 1]:
        if valueToTheWest >= pointOfInterestValue:
            return False
    return True


def isHigherThanAllEast(point: Point, grid):
    pointOfInterestValue = grid[point.yCoord][point.xCoord]

    for valueToTheWest in grid[point.yCoord][point.xCoord - 1:len(grid) - 1]:
        if valueToTheWest >= pointOfInterestValue:
            return False


def isHigherThanAllNorth(point: Point, grid):
    pass


def isHigherThanAllSouth(point: Point, grid):
    pass


def getTreeGrid(fileName: str):
    treesDataSource = open(fileName, "r")
    rowNumber = 0
    treeGrid = []
    for rowOfTrees in treesDataSource:
        rowOfTrees = rowOfTrees.strip()
        treeGrid.append([])
        for height in rowOfTrees:
            treeGrid[rowNumber].append(height)
        rowNumber += 1
    return treeGrid


def isVisibleFromOutsideTheGrid(point: Point, grid):
    if isHigherThanAllWest(point, grid):
        return True
    if isHigherThanAllNorth(point, grid):
        return True
    if isHigherThanAllEast(point, grid):
        return True
    if isHigherThanAllSouth(point, grid):
        return True
    return False


def getNumberOfTreesVisibleFromOutsideSquareGrid(grid):
    numberOfTreesAroundEdges = len(grid)*2 + len(grid[0])*2 - 4
    rows = len(grid)
    xValue = 1
    for rowOfTrees in grid[1:rows - 1]:
        numberOfTreesInRow = len(rowOfTrees)
        yValue = 1
        for tree in rowOfTrees[1:numberOfTreesInRow - 1]:
            point = Point(xValue, yValue)
            if isVisibleFromOutsideTheGrid(point, grid):
                numberOfTreesAroundEdges += 1
        xValue += 1
    return numberOfTreesAroundEdges


def part1(fileName):
    grid = getTreeGrid(fileName)
    numberOfTreesVisibleFromOutsideSquareGrid = getNumberOfTreesVisibleFromOutsideSquareGrid(grid)
    print("number of trees visible from outside square grid: " + str(numberOfTreesVisibleFromOutsideSquareGrid))



file = 'Day8/testData.txt'
part1(file)
