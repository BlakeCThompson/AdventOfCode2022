import string
import numpy


def isSetSupersetOfOtherSet(range1: str, range2: str):
    """
    Take two strings of ranges in the format of "x-y", where x is the lower limit of the range
    and y is the higher limit of the range.
    Check if range1 is a superset of range2.
    :param range1: string
    :param range2: string
    :return: is range1 superset of range2? : bool
    """
    partitionedRange1 = range1.partition('-')
    lowerLimit = int(partitionedRange1[0])
    upperLimit = int(partitionedRange1[2])

    partitionedRange2 = range2.partition('-')
    return lowerLimit <= int(partitionedRange2[0]) and upperLimit >= int(partitionedRange2[2])


def part1():
    data = open("Day4/data.txt", "r")

    print("part 1:")
    # Every item in the range is a tuple of a low and high range.
    # Need to look at each pair, and see if one is a superset of the other.
    supersetsCount = 0
    for line in data:
        partitionedLine = line.partition(',')
        firstSet = partitionedLine[0]
        secondSet = partitionedLine[2]
        if isSetSupersetOfOtherSet(firstSet, secondSet) or isSetSupersetOfOtherSet(secondSet, firstSet):
            supersetsCount += 1
    print("number of superset pairs:")
    print(supersetsCount)
    data.close()


part1()


def setIntersectsOtherSet(range1: str, range2: str):
    partitionedRange1 = range1.partition('-')
    range1LowerLimit = int(partitionedRange1[0])
    range1UpperLimit = int(partitionedRange1[2])

    partitionedRange2 = range2.partition('-')
    range2LowerLimit = int(partitionedRange2[0])
    range2UpperLimit = int(partitionedRange2[2])
    return (range1LowerLimit <= range2LowerLimit <= range1UpperLimit) \
        or (range1LowerLimit <= range2UpperLimit <= range1UpperLimit)


def part2():
    data = open("Day4/data.txt", "r")

    print("part 2:")
    # Every item in the range is a tuple of a low and high range.
    # Need to look at each pair, and see if one is a superset of the other.
    intersectingCount = 0
    for line in data:
        partitionedLine = line.partition(',')
        firstSet = partitionedLine[0]
        secondSet = partitionedLine[2]
        if setIntersectsOtherSet(firstSet, secondSet) or setIntersectsOtherSet(secondSet, firstSet):
            intersectingCount += 1
    print("number of intersecting pairs:")
    print(intersectingCount)
    data.close()


part2()
