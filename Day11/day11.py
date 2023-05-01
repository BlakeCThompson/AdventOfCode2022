from __future__ import annotations

from typing import TextIO

from abc import ABC



class Test(ABC):
    def executeTest(self, value):
        pass


class TestDivisibleBy(Test):
    def __init__(self, testString: str):
        self.testString = testString
        divisor = testString.split('Test: divisible by ')[1]
        self.divisor = int(divisor)

    def executeTest(self, value) -> bool:
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



class Monkey:
    _index = 0
    def __init__(self, items: list, operation: Operation, test: Test):
        self.index = Monkey._index
        Monkey._index += 1
        self.items = items
        self.operation = operation
        self.test = test

    def execute(self):
        for index, item in enumerate(self.items):
            self.items[index] = self.operation.executeOperation(item)

    def setTrueMonkey(self, monkey: Monkey):
        self.trueMonkey = monkey


    def setFalseMonkey(self, monkey: Monkey):
        self.falseMonkey = monkey


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

def parseMonkeyObjectFromString(monkeyString) -> Monkey:
    pass



def part1(fileName):
    monkeys = parseMonkeyStrings(fileName)

    # print(stringImage)


# file = 'Day10/testData.txt'
file = 'Day11/data.txt'
# part1(file)
# part2(file)
