import json

class PacketSet:
    def __init__(self, leftPacket: list, rightPacket: list):
        self.leftPacket = leftPacket
        self.rightPacket = rightPacket


def parseLeftAndRightPackets(packetsString: str):
    packetsStrings = packetsString.split('\n')
    leftPacket = json.loads(packetsStrings[0])
    rightPacket = json.loads(packetsStrings[1])
    return PacketSet(leftPacket, rightPacket)

