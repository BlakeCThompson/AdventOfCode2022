from __future__ import annotations

from abc import ABC


class Command(ABC):
    def __init__(self, value):
        pass

    def execute(self, cpu: CPU):
        pass


class AddXCommand(Command):
    def __init__(self, value: int):
        super().__init__(value)
        self._numCycles = 2
        self.value = value

    def execute(self, cpu: CPU):
        for cycle in range(self._numCycles):
            cpu.states.append(cpu.xRegister)
        cpu.xRegister = cpu.xRegister + self.value


class CPU:
    def __init__(self):
        self.cycleNumber = 0
        self.xRegister = 1
        # states is a list representing the state of the xRegister at every tick of the clock.
        self.states = []

    def executeCommand(self, command: Command):
        command.execute(self)

    def getSignalStrengthDuringTick(self, tick):
        return self.states[tick - 1] * tick


class NoOpCommand(Command):
    def execute(self, cpu: CPU):
        cpu.states.append(cpu.xRegister)


def commandFactory(commandLine: str) -> Command:
    command = commandLine.split(' ')
    commandName = command[0]
    if commandName == 'addx':
        value = command[1]
        return AddXCommand(int(value))
    return NoOpCommand(0)


def part1(fileName):
    commandLines = open(fileName, "r")
    cpu = CPU()

    for commandLine in commandLines:
        command = commandFactory(commandLine)
        cpu.executeCommand(command)
    sumOfSignalStrengths = 0
    for tickNumber in range(len(cpu.states))[20::40]:
        signalStrength = cpu.getSignalStrengthDuringTick(tickNumber)
        print('signal strength at ', str(tickNumber), signalStrength)
        sumOfSignalStrengths += signalStrength
    print('sum of signal strengths', str(sumOfSignalStrengths))

    commandLines.close()


def spriteOverLapsWithCurrentClockTick(spriteCenter: int, spriteLengthOnEitherSideOfCenter: int, tickNumber: int):
    leftSideOfSprite = spriteCenter - spriteLengthOnEitherSideOfCenter
    rightSideOfSprite = spriteCenter + spriteLengthOnEitherSideOfCenter
    return leftSideOfSprite <= tickNumber <= rightSideOfSprite


def renderImage(cpuStates: list, spriteSize=3, screenPixelWidth=40):
    spriteSizeOnEitherSideOfCenter = int(spriteSize / 2)
    stringRepresentationOfRenderedImage = ''
    for tickNumber, xRegisterValue in enumerate(cpuStates):
        tickNumber = tickNumber
        tickNumber = tickNumber % screenPixelWidth
        if tickNumber % screenPixelWidth == 0:
            stringRepresentationOfRenderedImage += '\n'
        if spriteOverLapsWithCurrentClockTick(xRegisterValue, spriteSizeOnEitherSideOfCenter, tickNumber):
            stringRepresentationOfRenderedImage += '#'
        else:
            stringRepresentationOfRenderedImage += '.'
    return stringRepresentationOfRenderedImage


def part2(fileName):
    commandLines = open(fileName, "r")
    cpu = CPU()
    for commandLine in commandLines:
        command = commandFactory(commandLine)
        cpu.executeCommand(command)
    commandLines.close()

    spriteSize = 3
    screenPixelWidth = 40
    stringImage = renderImage(cpu.states, spriteSize, screenPixelWidth)
    print(stringImage)


# file = 'Day10/testData.txt'
file = 'Day10/data.txt'
part1(file)
part2(file)
