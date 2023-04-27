from __future__ import annotations

from abc import ABC


class Command(ABC):
    def __init__(self, value):
        pass

    def getCycles(self):
        return self.numCycles

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


def part2(fileName):
    pass


file = 'Day10/data.txt'
part1(file)
# part2(file)
