class Grid:
    def __init__(self, rows: list):
        self.rows = rows


def isHigherThanAllWest(row, column, grid):
    pointOfInterestValue = grid[row][column]
    for valueToTheWest in grid[row][0: column]:
        if int(valueToTheWest) >= int(pointOfInterestValue):
            return False
    return True


def isHigherThanAllEast(row, column, grid):
    pointOfInterestValue = grid[row][column]
    for valueToTheEast in grid[row][column + 1:]:
        if int(valueToTheEast) >= int(pointOfInterestValue):
            return False
    return True


def isHigherThanAllNorth(row, column, grid):
    pointOfInterestValue = grid[row][column]
    for r in grid[0:row]:
        if r[column] >= pointOfInterestValue:
            return False
    return True


def isHigherThanAllSouth(row, column, grid):
    pointOfInterestValue = grid[row][column]
    for r in grid[row + 1:]:
        if r[column] >= pointOfInterestValue:
            return False
    return True


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


def isVisibleFromOutsideTheGrid(row, column, grid):
    if isHigherThanAllWest(row, column, grid):
        return True
    if isHigherThanAllNorth(row, column, grid):
        return True
    if isHigherThanAllEast(row, column, grid):
        return True
    if isHigherThanAllSouth(row, column, grid):
        return True
    return False


def getNumberOfTreesVisibleFromOutsideSquareGrid(grid):
    numberOfTreesVisibleFromOutsideSquareGrid = len(grid) * 2 + len(grid[0]) * 2 - 4
    rows = len(grid)
    row = 1
    for rowOfTrees in grid[1:rows - 1]:
        numberOfTreesInRow = len(rowOfTrees)
        column = 0
        for _ in rowOfTrees[1:numberOfTreesInRow - 1]:
            column += 1
            if isVisibleFromOutsideTheGrid(row, column, grid):
                print(row, column)
                numberOfTreesVisibleFromOutsideSquareGrid += 1
        row += 1
    return numberOfTreesVisibleFromOutsideSquareGrid


def part1(fileName):
    grid = getTreeGrid(fileName)
    numberOfTreesVisibleFromOutsideSquareGrid = getNumberOfTreesVisibleFromOutsideSquareGrid(grid)
    print("number of trees visible from outside square grid: " + str(numberOfTreesVisibleFromOutsideSquareGrid))


def getNumberOfTreesVisibleToNorthOf(row, column, grid):
    pointOfInterestValue = grid[row][column]
    numberOfTreesVisible = 0
    for r in grid[row-1::-1]:
        comparedTree = r[column]
        numberOfTreesVisible += 1
        if comparedTree >= pointOfInterestValue:
            return numberOfTreesVisible
    return numberOfTreesVisible


def getNumberOfTreesVisibleToEastOf(row, column, grid):
    pointOfInterestValue = grid[row][column]
    numberOfTreesVisible = 0
    for tree in grid[row][column + 1:]:
        comparedTree = tree
        numberOfTreesVisible += 1
        if comparedTree >= pointOfInterestValue:
            return numberOfTreesVisible
    return numberOfTreesVisible


def getNumberOfTreesVisibleToSouthOf(row, column, grid):
    pointOfInterestValue = grid[row][column]
    numberOfTreesVisible = 0
    for r in grid[row + 1:]:
        comparedTree = r[column]
        numberOfTreesVisible += 1
        if comparedTree >= pointOfInterestValue:
            return numberOfTreesVisible
    return numberOfTreesVisible

def getScenicScore(row, column, grid):
    treesVisibleToNorth = getNumberOfTreesVisibleToNorthOf(row, column, grid)
    # treesVisibleToEast = getNumberOfTreesVisibleToEastOf(row, column, grid)
    # treesVisibleToSouth = getNumberOfTreesVisibleToSouthOf(row, column, grid)
    # treesVisibleToWest = getNumberOfTreesVisibleToWestOf(row, column, grid)
    # return treesVisibleToNorth * treesVisibleToEast * treesVisibleToSouth * treesVisibleToWest
    return treesVisibleToNorth


def getTreeHavingHighestScenicScore(grid):
    highestScenicScore = 0
    highestScenicScoreTree = []
    rowNumber = 0
    for r in grid:
        colNumber = 0
        for c in r:
            scenicScore = getScenicScore(rowNumber, colNumber, grid)
            if scenicScore > highestScenicScore:
                highestScenicScoreTree = (rowNumber, colNumber)
                highestScenicScore = scenicScore
    return highestScenicScoreTree, highestScenicScore


def part2(fileName):
    grid = getTreeGrid(fileName)
    treeWithBestScenicScore = getTreeHavingHighestScenicScore(grid)
    print(treeWithBestScenicScore[0], ' ', treeWithBestScenicScore[1])

file = 'Day8/data.txt'
part1(file)
