from __future__ import annotations

import time
from typing import TextIO

from abc import ABC

import math


def lcm(numbers):
    # Find the LCM of two numbers
    def lcm_helper(x, y):
        return abs(x * y) // math.gcd(x, y)

    # Find the LCM of a list of numbers recursively
    def lcm_rec(numbers):
        if len(numbers) == 1:
            return numbers[0]
        else:
            return lcm_helper(numbers[0], lcm_rec(numbers[1:]))

    return lcm_rec(numbers)


class Test(ABC):
    def __init__(self):
        self.divisor = 1

    def testPasses(self, value) -> bool:
        return False


class TestDivisibleBy(Test):
    def __init__(self, testString: str):
        self.testString = testString
        divisor = testString.split('Test: divisible by ')[1]
        self.divisor = int(divisor)

    def testPasses(self, value) -> bool:
        return value % self.divisor == 0


class Operation:
    _floatingValue = 0

    def __init__(self, operationString):
        self.operationString = operationString

    def executeOperation(self, value):
        operation = self.operationString.split('Operation:')[1]
        return self._execute(operation, value)

    def _execute(self, command: str, value: int):
        self._floatingValue = value
        command = command.replace('new', 'self._floatingValue')
        command = command.replace('old', 'self._floatingValue')
        command = command.strip()
        exec(command)
        return self._floatingValue


class MonkeyGroup:
    def __init__(self):
        self.monkeys = []
        self.leastCommonMultiple = 1

    def getLeastCommonMultiple(self):
        divisors = []
        for monkey in self.monkeys:
            divisors.append(monkey.test.divisor)
        return lcm(divisors)

    def addMonkey(self, newMonkey: Monkey) -> None:
        newMonkey.monkeyGroup = self
        for monkey in self.monkeys:
            if newMonkey.trueMonkeyIndex == monkey.index:
                newMonkey.setTrueMonkey(monkey)
            if newMonkey.falseMonkeyIndex == monkey.index:
                newMonkey.setFalseMonkey(monkey)
        self.monkeys.append(newMonkey)
        self.leastCommonMultiple = self.getLeastCommonMultiple()

    def executeOnAll(self, reliefModifier=None) -> None:
        for monkey in self.monkeys:
            if reliefModifier is None:
                monkey.execute(self.leastCommonMultiple)
            else:
                print(time.asctime(), monkey.index, monkey.itemWorryLevels)
                monkey.execute(reliefModifier)

    def getInspectedCounts(self) -> list:
        inspectedCounts = []
        for monkey in self.monkeys:
            inspectedCounts.append((monkey.index, monkey.getNumberOfItemsInspected()))
        return inspectedCounts

    def getMonkeyByIndex(self, index):
        for monkey in self.monkeys:
            if monkey.index == index:
                return monkey


class Monkey:

    def __init__(self, index: int, items: list, operation: Operation, test: Test, trueMonkeyIndex, falseMonkeyIndex):
        self.falseMonkey = None
        self.trueMonkey = None
        self.trueMonkeyIndex = trueMonkeyIndex
        self.falseMonkeyIndex = falseMonkeyIndex
        self.index = index
        self.itemWorryLevels = items
        self.operation = operation
        self.test = test
        self.inspectedItems = 0
        self.monkeyGroup = None

    def addItem(self, itemValue: int) -> None:
        self.itemWorryLevels.append(itemValue)

    def lookForTrueMonkey(self):
        for monkey in self.monkeyGroup.monkeys:
            if monkey.index == self.trueMonkeyIndex:
                self.trueMonkey = monkey
                return monkey

    def lookForFalseMonkey(self):
        for monkey in self.monkeyGroup.monkeys:
            if monkey.index == self.falseMonkeyIndex:
                self.falseMonkey = monkey
                return monkey

    def execute(self, reliefModifier=3) -> None:
        itemsCopy = self.itemWorryLevels.copy()
        for item in itemsCopy:
            self.inspectedItems += 1
            item = self.operation.executeOperation(item)

            item = item % reliefModifier
            item = int(item)
            if self.test.testPasses(item):
                if self.trueMonkey is None:
                    self.lookForTrueMonkey()
                self.trueMonkey.addItem(item)
            else:
                if self.falseMonkey is None:
                    self.lookForFalseMonkey()
                self.falseMonkey.addItem(item)
            firstElement = 0
            self.itemWorryLevels.pop(firstElement)

    def setTrueMonkey(self, monkey: Monkey) -> None:
        self.trueMonkey = monkey

    def setFalseMonkey(self, monkey: Monkey) -> None:
        self.falseMonkey = monkey

    def getNumberOfItemsInspected(self) -> int:
        return self.inspectedItems


def parseMonkeyStrings(fileName: TextIO):
    monkeyStrings = []
    currentMonkeyString = ''
    for line in fileName:
        line = str(line)
        if line == '\n':
            continue
        currentMonkeyString += line
        isLastLineOfMonkeyRepresentation = line.find('If false:') != -1
        if isLastLineOfMonkeyRepresentation:
            monkeyStrings.append(currentMonkeyString)
            currentMonkeyString = ''
    return monkeyStrings


def parseMonkeyIndexFromString(trueMonkeyString: str):
    return readIntegerFromString(trueMonkeyString.split('onkey ')[1])


def readIntegerFromString(string: str):
    num_str = ""
    for char in string:
        if char.isdigit():
            num_str += char
        else:
            break
    if num_str == "":
        return None
    else:
        return int(num_str)


def parseMonkeyObjectFromString(monkeyString: str) -> Monkey:
    monkeyString = monkeyString.strip()
    monkeyLines = monkeyString.split('\n')
    monkeyIndex = parseMonkeyIndexFromString(monkeyLines[0])
    startingItems = parseStartingItems(monkeyLines[1])
    operation = Operation(monkeyLines[2])
    test = TestDivisibleBy(monkeyLines[3])
    trueIndex = parseMonkeyIndexFromString(monkeyLines[4])
    falseIndex = parseMonkeyIndexFromString(monkeyLines[5])

    return Monkey(monkeyIndex, startingItems, operation, test, trueIndex, falseIndex)


def parseStartingItems(startingItemsString):
    startingItemsString = startingItemsString.split('items: ')[1]
    startingItemsHolder = startingItemsString.split(', ')
    startingItems = []
    for item in startingItemsHolder:
        startingItems.append(int(item))
    return startingItems


def getTopInspectingMonkeys(monkeyGroup: MonkeyGroup, topCount: int) -> list:
    topMonkeys = []
    pass
    # for monkeyIndex, monkey in monkeyGroup.getInspectedCounts():


def executeOnAllXTimes(monkeyGroup: MonkeyGroup, numberOfTimes: int = 20, reliefModifier=None):
    for iteration in range(numberOfTimes):
        if iteration % 100 == 0:
            print(iteration, monkeyGroup.getInspectedCounts())
        if reliefModifier is None:
            monkeyGroup.executeOnAll()
        else:
            monkeyGroup.executeOnAll(reliefModifier)


def part1(fileName):
    ioStream = open(fileName, 'r')
    monkeyStrings = parseMonkeyStrings(ioStream)
    ioStream.close()
    monkeyGroup = MonkeyGroup()
    for monkeyString in monkeyStrings:
        monkeyGroup.addMonkey(parseMonkeyObjectFromString(monkeyString))
    numberOfIterations = 20
    executeOnAllXTimes(monkeyGroup, numberOfIterations)
    inspections = monkeyGroup.getInspectedCounts()
    inspections = sorted(inspections, key=lambda x: x[1], reverse=True)
    print('top 2 by inspections:', inspections[0], inspections[1])
    print('monkey business level = ' + str(inspections[0][1] * inspections[1][1]))


def part2(fileName):
    ioStream = open(fileName, 'r')
    monkeyStrings = parseMonkeyStrings(ioStream)
    ioStream.close()
    monkeyGroup = MonkeyGroup()
    for monkeyString in monkeyStrings:
        monkeyGroup.addMonkey(parseMonkeyObjectFromString(monkeyString))
    numberOfIterations = 10000
    executeOnAllXTimes(monkeyGroup, numberOfIterations, 1)
    inspections = monkeyGroup.getInspectedCounts()
    inspections = sorted(inspections, key=lambda x: x[1], reverse=True)
    print('top 2 by inspections:', inspections[0], inspections[1])
    print('monkey business level = ' + str(inspections[0][1] * inspections[1][1]))


file = 'Day11/testData.txt'
# file = 'Day11/data.txt'
# part1(file)
# part2(file)
