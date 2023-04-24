class Coordinates:
    def __init__(self, xPosition, yPosition):
        self.xPosition = xPosition
        self.yPosition = yPosition


from enum import Enum


class Directions(Enum):
    N = 0, 1
    NE = 1, 1
    E = 1, 0
    SE = 1, -1
    S = 0, -1
    SW = -1, -1
    W = -1, 0
    NW = -1, 1


class Tail:
    def __init__(self, coordinate: Coordinates):
        self.coordinate = coordinate
        self.visitedCoordinates = []
        self._addVisitedPlace(coordinate)

    def move(self, direction: Directions):
        self.coordinate.xPosition += direction.value[0]
        self.coordinate.yPosition += direction.value[1]
        self._addVisitedPlace(self.coordinate)

    def _addVisitedPlace(self, coordinate: Coordinates):
        for x, y in self.visitedCoordinates:
            if coordinate.xPosition == x and coordinate.yPosition == y:
                return
        self.visitedCoordinates.append((coordinate.xPosition, coordinate.yPosition))

    def getVisitedCount(self) -> int:
        return len(self.visitedCoordinates)


def moveTailIfNecessary(headPosition: Coordinates, tailPosition: Tail):
    if headIsMoreThanXSpaceAwayVertically(headPosition, tailPosition) or headIsMoreThanXSpaceAwayHorizontally(
            headPosition, tailPosition):
        followHead(headPosition, tailPosition)


def followHead(headPosition: Coordinates, tailPosition: Tail):
    if headPosition.xPosition == tailPosition.coordinate.xPosition:
        if headPosition.yPosition > tailPosition.coordinate.yPosition:
            tailPosition.move(Directions.N)
            return
        if headPosition.yPosition < tailPosition.coordinate.yPosition:
            tailPosition.move(Directions.S)
            return
    if headPosition.xPosition > tailPosition.coordinate.xPosition:
        if headPosition.yPosition > tailPosition.coordinate.yPosition:
            tailPosition.move(Directions.NE)
            return
        if headPosition.yPosition < tailPosition.coordinate.yPosition:
            tailPosition.move(Directions.SE)
            return
        if headPosition.yPosition == tailPosition.coordinate.yPosition:
            tailPosition.move(Directions.E)
            return
    if headPosition.xPosition < tailPosition.coordinate.xPosition:
        if headPosition.yPosition > tailPosition.coordinate.yPosition:
            tailPosition.move(Directions.NW)
            return
        if headPosition.yPosition < tailPosition.coordinate.yPosition:
            tailPosition.move(Directions.SW)
            return
        if headPosition.yPosition == tailPosition.coordinate.yPosition:
            tailPosition.move(Directions.W)


def headIsMoreThanXSpaceAwayVertically(headPosition: Coordinates, tailPosition: Tail, spacesAway: int = 1):
    return headPosition.yPosition > tailPosition.coordinate.yPosition + spacesAway or headPosition.yPosition < tailPosition.coordinate.yPosition - spacesAway


def headIsMoreThanXSpaceAwayHorizontally(headPosition: Coordinates, tailPosition: Tail, spacesAway: int = 1):
    return headPosition.xPosition > tailPosition.coordinate.xPosition + spacesAway or headPosition.xPosition < tailPosition.coordinate.xPosition - spacesAway


def moveDirection(direction: str, iterations: int, ropeHead: Coordinates, ropeTail: Tail):
    if direction == 'U':
        for iteration in range(iterations):
            ropeHead.yPosition += 1
            moveTailIfNecessary(ropeHead, ropeTail)
    elif direction == 'R':
        for iteration in range(iterations):
            ropeHead.xPosition += 1
            moveTailIfNecessary(ropeHead, ropeTail)
    elif direction == 'D':
        for iteration in range(iterations):
            ropeHead.yPosition -= 1
            moveTailIfNecessary(ropeHead, ropeTail)
    elif direction == 'L':
        for iteration in range(iterations):
            ropeHead.xPosition -= 1
            moveTailIfNecessary(ropeHead, ropeTail)


def followCommand(commandLine: str, ropeHead: Coordinates, ropeTail: Tail):
    commandLine = commandLine.split(' ')
    direction = commandLine[0]
    numberOfIterations = int(commandLine[1])
    moveDirection(direction, numberOfIterations, ropeHead, ropeTail)


def part1(fileName):
    commandLines = open(fileName, "r")
    ropeHead = Coordinates(0, 0)
    ropeTail = Tail(Coordinates(0, 0))
    for commandLine in commandLines:
        followCommand(commandLine, ropeHead, ropeTail)
    print('tail visited ' + str(ropeTail.getVisitedCount()))
    commandLines.close()


file = 'Day9/data.txt'
part1(file)
