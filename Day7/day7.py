def backDirectory(path: str):
    path = path.split('/')

    if path[-1] == '':
        parentPathSegments = path[1:-2:]
    else:
        parentPathSegments = path[1:-1:]
    newPath = '/'
    for elem in parentPathSegments:
        newPath = newPath + elem + '/'
    return newPath


def handleCD(currentDirectory: str, toDirectory: str):
    """
    :param currentDirectory:
    :param toDirectory:
    :return: newCurrentDirectory: str
    """
    if toDirectory == '/':
        return '/'
    elif toDirectory == '..':
        return backDirectory(currentDirectory)
    return currentDirectory + toDirectory + '/'


def handleLS(currentDirectory: str, dataStream, directories: dict):
    """
    handleLS uses the currentDirectory, and then peaks ahead through the
    datastream, reading the output of every line, and mapping information
    into the directories object.
    :param currentDirectory:
    :param dataStream:
    :param directories:
    :return:
    """
    line = peekLine(dataStream)
    nextLineIsACommand = line.startswith('$ ')
    if nextLineIsACommand:
        return
    line = dataStream.readline().strip('\n')
    while line:
        segments = line.split(' ')
        firstSegment = segments[0]
        thisLineIsAFileStartingWithItsSize, value = isInt(firstSegment)
        if thisLineIsAFileStartingWithItsSize:
            fileName = segments[1]
            directories[currentDirectory + fileName] = value
        line = peekLine(dataStream)
        if line.startswith('$ '):
            return
        line = dataStream.readline().strip('\n')


def isInt(value):
    i = int(value) if value.isdecimal() else None
    if i is None:
        return False, i
    return True, i


def addFileSizeToAllParentDirectories(size, fileName, directorySizes):
    parentDir = backDirectory(fileName)
    if parentDir != '/':
        parentDir = parentDir[:-1]
    if parentDir not in directorySizes.keys():
        directorySizes[parentDir] = size
    else:
        directorySizes[parentDir] += size
    if parentDir != '/':
        addFileSizeToAllParentDirectories(size, parentDir, directorySizes)


def getSumsByDirectory(files):
    directorySizes = {}
    for fileName in files:
        size = files[fileName]
        addFileSizeToAllParentDirectories(size, fileName, directorySizes)
    return directorySizes


def getDirectoriesHavingSizeLessThanOrEqualToX(directoriesToCheck: dict, maxSizeX: int):
    """
    :param directoriesToCheck: a dictionary of string->dictionary key value pairs.
        every dictionary key value in the inner dictionary is a filename -> size.
    :param maxSize: the "X" value referred to in the function name
    :return: read every directory in the dictionary of directories, and returns every directory's file size
    ("directory file size" is defined here as the sum of the file sizes that live directly in the directory --
    e.g. not including files in descendant folders.)
    """
    qualifyingDirectories = {}
    for directory in directoriesToCheck:
        if directoriesToCheck[directory] <= maxSizeX:
            qualifyingDirectories[directory] = directoriesToCheck[directory]
    return qualifyingDirectories



def getDirectoriesHavingSizeGreaterThanOrEqualToX(directoriesToCheck: dict, minimumSizeX: int):
    qualifyingDirectories = {}
    for directory in directoriesToCheck:
        if directoriesToCheck[directory] >= minimumSizeX:
            qualifyingDirectories[directory] = directoriesToCheck[directory]
    return qualifyingDirectories

def getSumOfDirectories(directories):
    sumOfDirectories = 0
    for d in directories:
        sumOfDirectories += directories[d]
    return sumOfDirectories


def peekLine(fileObj):
    pos = fileObj.tell()
    line = fileObj.readline().strip('\n')
    fileObj.seek(pos)
    return line


def getFilesFromCommandOutputs(fileNameOfCommandOutputs):
    data = open(fileNameOfCommandOutputs, "r")
    directories = {}
    currentDirectory = ''
    x = data.tell()
    line = data.readline()
    while line:
        line = line.strip('\n')
        if line.startswith('$ cd '):
            toDirectory = line.split('cd ')[1]
            currentDirectory = handleCD(currentDirectory, toDirectory)
        elif line.startswith('$ ls'):
            handleLS(currentDirectory, data, directories)
        line = data.readline()
    return directories


def part1(fileName):
    print("part 1:")
    files = getFilesFromCommandOutputs(fileName)
    directorySizeLimit = 100000
    directories = getSumsByDirectory(files)
    qualifyingDirectories = getDirectoriesHavingSizeLessThanOrEqualToX(directories, directorySizeLimit)
    print('directories having less than ' + str(directorySizeLimit) + ": " + qualifyingDirectories.__str__())
    directoriesSum = getSumOfDirectories(qualifyingDirectories)
    print("sum of directory sizes having size >= " + str(directorySizeLimit) + '= ' + str(directoriesSum))




def part2(fileName):
    print("part 2:")

    files = getFilesFromCommandOutputs(fileName)
    directories = getSumsByDirectory(files)

    totalSystemMemory = 70000000
    print("Total system memory = " + str(totalSystemMemory))
    usedMemory = directories['/']

    print("used memory: " + str(usedMemory))
    availableMemory = totalSystemMemory - usedMemory
    print("available memory: " + str(availableMemory))
    neededMemory = 30000000
    print("needed memory: " + str(neededMemory))
    amountOfMemoryNeedingFreed = neededMemory - availableMemory
    qualifyingDirectories = getDirectoriesHavingSizeGreaterThanOrEqualToX(directories, amountOfMemoryNeedingFreed)
    sortedDirectoriesBySize = dict(sorted(qualifyingDirectories.items(), key=lambda item: item[1]))
    print("directory having smallest size that releases enough memory: " + str(list(sortedDirectoriesBySize.items())[0][1]))

fileName = "Day7/data.txt"
# fileName = "Day7/testData.txt"

part1(fileName)

part2(fileName)
