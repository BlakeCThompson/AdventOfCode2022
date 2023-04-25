import Day9.day9 as day9

import unittest


class TestDay9(unittest.TestCase):

    def testDay9(self):
        day9.part1('day9/testData.txt')
        print("")


    def testTailFollowsRight(self):
        tailCoords = day9.Coordinates(0, 0)
        head = day9.Coordinates(2, 0)

        tail = day9.Knot(tailCoords)
        day9.moveTailIfNecessary(head, tail)
        self.assertEqual(2, tail.getVisitedCount())
        self.assertListEqual([(0, 0), (1, 0)], tail.visitedCoordinates)

    def testHeadIsMoreThanXAwayHorizontally(self):
        tailCoords = day9.Coordinates(0, 0)
        tail = day9.Knot(tailCoords)
        head = day9.Coordinates(0, 2)
        self.assertFalse(day9.headIsMoreThanXSpaceAwayHorizontally(head, tail, 1))
        head.xPosition = 2
        head.yPosition = 0
        self.assertTrue(day9.headIsMoreThanXSpaceAwayHorizontally(head, tail, 1))
        head.xPosition = 1
        head.yPosition = 2
        self.assertFalse(day9.headIsMoreThanXSpaceAwayHorizontally(head, tail, 1))
        head.xPosition = 2
        head.yPosition = 1
        self.assertTrue(day9.headIsMoreThanXSpaceAwayHorizontally(head, tail, 1))

    def testHeadIsMoreThanXAwayVertically(self):
        tailCoords = day9.Coordinates(0, 0)
        tail = day9.Knot(tailCoords)
        head = day9.Coordinates(2, 0)
        self.assertFalse(day9.headIsMoreThanXSpaceAwayVertically(head, tail, 1))
        head.xPosition = 0
        head.yPosition = 2
        self.assertTrue(day9.headIsMoreThanXSpaceAwayVertically(head, tail, 1))
        head.xPosition = 2
        head.yPosition = 1
        self.assertFalse(day9.headIsMoreThanXSpaceAwayVertically(head, tail, 1))
        head.xPosition = 1
        head.yPosition = 2
        self.assertTrue(day9.headIsMoreThanXSpaceAwayVertically(head, tail, 1))


    def testMoveTailIfNecessaryFollowsNorthWest(self):
        tailCoords = day9.Coordinates(4, 4)
        tail = day9.Knot(tailCoords)
        head = day9.Coordinates(2, 5)

        day9.moveTailIfNecessary(head, tail)
        self.assertEqual(2, tail.getVisitedCount())
        self.assertListEqual([(4, 4), (3, 5)], tail.visitedCoordinates)

    def testMoveTailIfNecessaryFollowsNorth(self):
        tailCoords = day9.Coordinates(4, 4)
        tail = day9.Knot(tailCoords)
        head = day9.Coordinates(4, 6)

        day9.moveTailIfNecessary(head, tail)
        self.assertEqual(2, tail.getVisitedCount())
        self.assertListEqual([(4, 4), (4, 5)], tail.visitedCoordinates)

if __name__ == '__main__':
    unittest.main()
