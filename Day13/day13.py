import json

from utils.enum import enum


class PacketSet:
    def __init__(self, leftPacket: list, rightPacket: list):
        self.leftPacket = leftPacket
        self.rightPacket = rightPacket

    def calculateIfPacketsAreInCorrectOrder(self) -> bool:
        """
        :return: true if packets are in correct order, otherwise false.
        """
        index = 0
        comparisonResult = 0
        while True:
            if index >= len(self.leftPacket):
                return comparisonResult < 1
            if index >= len(self.rightPacket):
                return False
            comparisonResult = self.__packetComparisonHelper(self.leftPacket[index], self.rightPacket[index])
            index += 1
            if comparisonResult == 0:
                continue
            return comparisonResult < 1
        return comparisonResult < 1

    def __packetComparisonHelper(self, leftElement, rightElement):
        """
        :param leftElement: could be a list or integer.
        :param rightElement: could be a list or integer.
        :return: if leftElement is less than rightElement, return -1.
                 if leftElement is equal to rightElement, return 0.
                 if leftElement is greater than rightElement, return 1.
        """
        if isinstance(leftElement, list) and not isinstance(rightElement, list):
            rightElement = [rightElement]
            return self.__compareLists(leftElement, rightElement)
        elif isinstance(rightElement, list) and not isinstance(leftElement, list):
            leftElement = [leftElement]
            return self.__compareLists(leftElement, rightElement)
        elif isinstance(leftElement, list) and isinstance(rightElement, list):
            return self.__compareLists(leftElement, rightElement)
        else:
            return self.__compareIntegers(leftElement, rightElement)


    def __compareIntegers(self, leftInteger, rightInteger):
        if leftInteger < rightInteger:
            return -1
        elif leftInteger == rightInteger:
            return 0
        else:
            return 1


    def __compareLists(self, leftList, rightList):
        """
        :param leftList:
        :param rightList:
        :return: if leftList is less than rightList, return -1.
                 if leftList is equal to rightList, return 0.
                 if leftList is greater than rightList, return 1.
        """
        index = 0
        for index, _ in enumerate(leftList):
            if len(rightList) == 0:
                return 1
            comparisonResult = self.__packetComparisonHelper(leftList[index], rightList[index])
            index += 1
            if comparisonResult == -1:
                return -1
            if comparisonResult == 0:
                continue
            if comparisonResult == 1:
                return 1
        return 0


def parsePacketSet(packetsString: str):
    packetsStrings = packetsString.split('\n')
    leftPacket = json.loads(packetsStrings[0])
    rightPacket = json.loads(packetsStrings[1])
    return PacketSet(leftPacket, rightPacket)

def parsePacketsFromFile(fileName: str):
    result = []
    with open(fileName, 'r') as file:
        sublist = []
        for line in file:
            line = line.strip()
            if line:
                sublist.append(line)
            else:
                if sublist:
                    result.append(parsePacketSet(sublist[0] + '\n' + sublist[1]))
                    sublist = []
        if sublist:
            result.append(parsePacketSet(sublist[0] + '\n' + sublist[1]))
    return result
