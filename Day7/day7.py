
def backDirectory(path :str):
    path = path.split('/')
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
    if line.startswith('$ '):
        return
    line = dataStream.readline().strip('\n')
    while line:
        segments = line.split(' ')
        firstSegment = segments[0]
        firstSegmentIsInt, value = isInt(firstSegment)
        if firstSegmentIsInt:
            secondSegment = segments[1]
            directories[currentDirectory + secondSegment] = value
        line = peekLine(dataStream)
        if line.startswith('$ '):
            return
        line = dataStream.readline().strip('\n')


def isInt(value):
    i = int(value) if value.isdecimal() else None
    if i is None:
        return False, i
    return True, i


def getSumsByDirectory(files):
    directories = {}
    for file in files:
        parentDir = backDirectory(file)
        if parentDir not in directories.keys():
            directories[parentDir] = files[file]
        else:
            directories[parentDir] += files[file]
    return directories


def getDirectoriesHavingSizeLessThanOrEqualToX(directoriesToCheck: dict, maxSize: int):
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
        if directoriesToCheck[directory] > maxSize:
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


def part1():
    print("part 1:")
    data = open("Day7/testData.txt", "r")
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
    directorySizeLimit = 100000
    directories = getSumsByDirectory(directories)
    qualifyingDirectories = getDirectoriesHavingSizeLessThanOrEqualToX(directories, directorySizeLimit)
    directoriesSum = getSumOfDirectories(qualifyingDirectories)
    print("sum of directory sizes having size >= " + str(directorySizeLimit) + '= ' + str(directoriesSum))


def part2():
    print("part 2:")


part1()

part2()
