import day12

import unittest


class Day12Tests(unittest.TestCase):
    def testParseGrid(self):
        expectedGrid = [
            ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
            ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
            ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
            ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
            ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
        ]
        parsedGrid = day12.parseGrid('testData.txt')
        for rowIndex, expectedRow in enumerate(expectedGrid):
            parsedRow = parsedGrid[rowIndex]
            for index, expectedValue in enumerate(expectedRow):
                parsedValue = parsedRow[index]
                self.assertEqual(expectedValue, parsedValue, 'row ' + str(rowIndex) + ' column: ' + str(
                    index) + ' did not match expected value.')

    def testGetCharsBetweenChars(self):
        self.assertEqual(2, day12.countCharsBetweenChars('a', 'd'))
        self.assertEqual(0, day12.countCharsBetweenChars('a', 'a'))
        self.assertEqual(1, day12.countCharsBetweenChars('f', 'd'))
        self.assertEqual(5, day12.countCharsBetweenChars('j', 'p'))
        self.assertEqual(5, day12.countCharsBetweenChars('p', 'j'))


    def testGetDistanceFromEnd(self):
        grid = [
            ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
            ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
            ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
            ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
            ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
        ]
        end = day12.getEnd(grid)
        self.assertEqual(end, (2, 5))
        distanceFromEnd = day12.getDistanceBetweenCoordinates((2, 0), end)
        self.assertEqual(distanceFromEnd, 5)
        distanceFromEnd = day12.getDistanceBetweenCoordinates((4, 5), end)
        self.assertEqual(distanceFromEnd, 2)
        distanceFromEnd = day12.getDistanceBetweenCoordinates((0, 1), end)
        self.assertEqual(distanceFromEnd, 6)

    def testGetMoveOptions(self):
        grid = [
            ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
            ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
            ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
            ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
            ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
        ]
        moveOptions = day12.getMoveOptions(grid, 0, 2)
        self.assertListEqual(moveOptions, [(0, 1), (1, 2)])
        moveOptions = day12.getMoveOptions(grid, 2, 2)
        self.assertListEqual(moveOptions, [(2, 1), (1, 2), (3, 2)])
        moveOptions = day12.getMoveOptions(grid, 2, 6)
        self.assertListEqual(moveOptions, [(1, 6), (3, 6)])

if __name__ == '__main__':
    unittest.main()
