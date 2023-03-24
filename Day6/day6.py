import io


def hasAllUniqueChars(charBuffer: str):
    for index, c in enumerate(charBuffer):
        if index == len(charBuffer) - 1:
            return True
        for compared in charBuffer[index + 1::]:
            if c == compared:
                return False


def getNumberOfProcessedCharactersBeforeXUniqueSequentialCharactersAppear(fileName: str, x: int):
    with open(fileName, "r", encoding='utf-8') as data:
        bufferLimit = x
        charBuffer = data.read(bufferLimit - 1)
        c = data.read(1)
        processedCharacters = bufferLimit - 1
        while c:
            charBuffer += c
            processedCharacters += 1
            if hasAllUniqueChars(charBuffer):
                return processedCharacters
            charBuffer = charBuffer[1::]
            c = data.read(1)


def part1():
    print("part 1:")
    numberOfUniqueChars = 4
    processedChars = getNumberOfProcessedCharactersBeforeXUniqueSequentialCharactersAppear('Day6/data.txt',
                                                                                           numberOfUniqueChars)
    print("processed " + str(processedChars) + " characters to find first " + str(
        numberOfUniqueChars) + " sequential unique characters")


def part2():
    print("part 2:")
    numberOfUniqueChars = 14
    # fileName = 'Day6/testData.txt'
    fileName = 'Day6/data.txt'
    processedChars = getNumberOfProcessedCharactersBeforeXUniqueSequentialCharactersAppear(fileName,
                                                                                           numberOfUniqueChars)
    print("processed " + str(processedChars) + " characters to find first " + str(
        numberOfUniqueChars) + " sequential unique characters")


part1()

part2()
