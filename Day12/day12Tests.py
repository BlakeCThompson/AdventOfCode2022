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
        charMapping = {}
        charMapping['S'] = 'a'
        charMapping['E'] = 'z'
        self.assertEqual(-3, day12.countCharsBetweenChars('a', 'd'), charMapping)
        self.assertEqual(0, day12.countCharsBetweenChars('a', 'a'), charMapping)
        self.assertEqual(2, day12.countCharsBetweenChars('f', 'd'), charMapping)
        self.assertEqual(-6, day12.countCharsBetweenChars('j', 'p'), charMapping)
        self.assertEqual(6, day12.countCharsBetweenChars('p', 'j'), charMapping)


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
        self.assertListEqual(moveOptions, [(1, 6), (2, 7), (3, 6)])
        moveOptions = day12.getMoveOptions(grid, 0, 3)
        self.assertListEqual(moveOptions, [(0, 2), (0, 4), (1, 3)])
        moveOptions = day12.getMoveOptions(grid, 3, 4)
        self.assertListEqual(moveOptions, [(3, 3), (3, 5), (4, 4)])

    def testGetBestOption(self):
        grid = [
            ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
            ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
            ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
            ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
            ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
        ]
        location = (2, 1)
        moveOptions = [(2, 0), (1, 1), (2, 2), (3, 1)]
        expectedBestMove = (2, 2)
        end = (2, 5)
        bestMove = day12.getBestMove(moveOptions, end)
        self.assertEqual(expectedBestMove, bestMove)

    def testGetMoveCost(self):
        grid = [
            ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
            ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
            ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
            ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
            ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
        ]
        breadthFirstSearcher = day12.BreadthFirstSearcher(grid)
        self.assertEqual(breadthFirstSearcher.distanceGraph[0][0], 0)
        for row in breadthFirstSearcher.distanceGraph:
            for cost in row[1:]:
                self.assertEqual(float('inf'), cost)

    def testBreadthFirstSearch(self):
        grid = [
            ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
            ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
            ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
            ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
            ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
        ]
        breadthFirstSearcher = day12.BreadthFirstSearcher(grid)
        self.assertEqual(breadthFirstSearcher.distanceGraph[0][0], 0)
        breadthFirstSearcher.searchOneStepOut()
        self.assertFalse(breadthFirstSearcher.pathFound)
        self.assertListEqual(breadthFirstSearcher.visited, [(0, 0), (0, 1), (1, 0)])
        self.assertEqual(breadthFirstSearcher.distanceGraph[0][0], 0)
        self.assertEqual(breadthFirstSearcher.distanceGraph[0][1], 1)
        self.assertEqual(breadthFirstSearcher.distanceGraph[1][0], 1)
        breadthFirstSearcher.searchOneStepOut()
        self.assertFalse(breadthFirstSearcher.pathFound)
        self.assertListEqual(breadthFirstSearcher.visited, [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0)])
        self.assertEqual(breadthFirstSearcher.distanceGraph[0][2], 2)
        self.assertEqual(breadthFirstSearcher.distanceGraph[1][1], 2)
        self.assertEqual(breadthFirstSearcher.distanceGraph[2][0], 2)

        breadthFirstSearcher.searchOneStepOut()
        self.assertFalse(breadthFirstSearcher.pathFound)
        self.assertListEqual(breadthFirstSearcher.visited, [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0), (1, 2), (2, 1), (3, 0)])


    def testGetsMinimumDistance(self):
        grid = [
            ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
            ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
            ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
            ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
            ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
        ]
        breadthFirstSearcher = day12.BreadthFirstSearcher(grid)
        self.assertEqual(breadthFirstSearcher.distanceGraph[0][0], 0)
        while not breadthFirstSearcher.pathFound:
            breadthFirstSearcher.searchOneStepOut()
        self.assertEqual(breadthFirstSearcher.distanceGraph[breadthFirstSearcher.end[0]][breadthFirstSearcher.end[1]], 31)

    def testSolvePart1(self):
        self.assertEqual(day12.solvePart1('data.txt'), 361)


if __name__ == '__main__':
    unittest.main()
