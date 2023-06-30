import day13

import unittest


# When comparing two values, the first value is called left and the second value is called right. Then:
#
# If both values are integers, the lower integer should come first.
#   If the left integer is lower than the right integer, the inputs are in the right order.
#   If the left integer is higher than the right integer, the inputs are not in the right order.
#       Otherwise, the inputs are the same integer; continue checking the next part of the input.
#   If both values are lists, compare the first value of each list, then the second value, and so on.
#       If the left list runs out of items first, the inputs are in the right order.
#       If the right list runs out of items first, the inputs are not in the right order.
#       If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
#       If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison.
# For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2);
# the result is then found by instead comparing [0,0,0] and [2].


class Day13Tests(unittest.TestCase):


    def testParsePackets(self):
        packetsString = '[1,1,3,1,1]\n[1,1,5,1,1]'
        packets = day13.parsePacketSet(packetsString)
        leftPacket = packets.leftPacket
        self.assertListEqual(leftPacket, [1, 1, 3, 1, 1])
        rightPacket = packets.rightPacket
        self.assertListEqual(rightPacket, [1, 1, 5, 1, 1])
        packetsString = '[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]'
        packets = day13.parsePacketSet(packetsString)
        leftPacket = packets.leftPacket
        self.assertListEqual(leftPacket, [1, [2, [3, [4, [5, 6, 7]]]], 8, 9])
        rightPacket = packets.rightPacket
        self.assertListEqual(rightPacket, [1,[2,[3,[4,[5,6,0]]]],8,9])
        self.assertFalse(packets.calculateIfPacketsAreInCorrectOrder())

    def testParsePackets2(self):
        packetsString = '[[1],[2,3,4]]\n[[1],4]'
        packetSet = day13.parsePacketSet(packetsString)
        self.assertTrue(packetSet.calculateIfPacketsAreInCorrectOrder())

    def testParsePackets3(self):
        packetsString = '[9]\n[[8,7,6]]'
        packetSet = day13.parsePacketSet(packetsString)
        self.assertFalse(packetSet.calculateIfPacketsAreInCorrectOrder())

    def testParsePackets4(self):
        packetsString = '[[4,4],4,4]\n[[4,4],4,4,4]'
        packetSet = day13.parsePacketSet(packetsString)
        self.assertTrue(packetSet.calculateIfPacketsAreInCorrectOrder())

    def testParsePackets5(self):
        packetsString = '[7,7,7,7]\n[7,7,7]'
        packetSet = day13.parsePacketSet(packetsString)
        self.assertFalse(packetSet.calculateIfPacketsAreInCorrectOrder())

    def testParsePackets6(self):
        packetsString = '[]\n[3]'
        packetSet = day13.parsePacketSet(packetsString)
        self.assertTrue(packetSet.calculateIfPacketsAreInCorrectOrder())

    def testParsePackets7(self):
        packetsString = '[[[]]]\n[[]]'
        packetSet = day13.parsePacketSet(packetsString)
        self.assertFalse(packetSet.calculateIfPacketsAreInCorrectOrder())

    def testParsePackets8(self):
        packetsString = '[1,[2,[3,[4,[5,6,7]]]],8,9]\n[1,[2,[3,[4,[5,6,0]]]],8,9]'
        packetSet = day13.parsePacketSet(packetsString)
        self.assertFalse(packetSet.calculateIfPacketsAreInCorrectOrder())

    def testParsePacketsFile(self):
        packetFile = 'testData.txt'
        packetSets = day13.parsePacketsFromFile(packetFile)
        self.assertEqual(8, len(packetSets))

    def testComparePackets(self):
        packetFile = 'testData.txt'
        packetSets = day13.parsePacketsFromFile(packetFile)
        results = []
        for packetSet in packetSets:
            results.append(packetSet.calculateIfPacketsAreInCorrectOrder())
        self.assertTrue(results[0])
        self.assertTrue(results[1])
        self.assertFalse(results[2])
        self.assertTrue(results[3])
        self.assertFalse(results[4])
        self.assertTrue(results[5])
        self.assertFalse(results[6])
        self.assertFalse(results[7])
