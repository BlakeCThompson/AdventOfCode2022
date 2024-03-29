import Day8.day8 as day8

import unittest


class TestDay8(unittest.TestCase):

    def test_isHigherThanAllWest(self):
        grid = [[1, 2, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [6, 1, 2, 3, 4],
                [1, 3, 6, 1, 2]]
        highPointIsHigherThanAnyToTheWest = day8.isHigherThanAllWest(1, 3, grid)
        self.assertTrue(highPointIsHigherThanAnyToTheWest)

        lowPointIsHigherThanAnyToTheWest = day8.isHigherThanAllWest(2, 3, grid)
        self.assertFalse(lowPointIsHigherThanAnyToTheWest)

    def test_isHigherThanAllEast(self):
        grid = [[1, 2, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [6, 1, 2, 3, 4],
                [1, 3, 6, 1, 2]]
        lowPointIsHigherThanAnyToTheEast = day8.isHigherThanAllEast(1, 3, grid)
        self.assertFalse(lowPointIsHigherThanAnyToTheEast)

        highPointIsHigherThanAnyToTheEast = day8.isHigherThanAllEast(3, 2, grid)
        self.assertTrue(highPointIsHigherThanAnyToTheEast)

    def test_isHigherThanAllNorth(self):
        grid = [[1, 2, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [6, 5, 2, 3, 4],
                [1, 3, 6, 1, 2]]
        highPointIsHigherThanAnyToTheNorth = day8.isHigherThanAllNorth(2, 1, grid)
        self.assertTrue(highPointIsHigherThanAnyToTheNorth)

        lowPointIsHigherThanAnyToTheNorth = day8.isHigherThanAllNorth(2, 3, grid)
        self.assertFalse(lowPointIsHigherThanAnyToTheNorth)

    def test_isHigherThanAllSouth(self):
        grid = [[1, 2, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [6, 5, 2, 3, 4],
                [1, 3, 6, 1, 2]]
        highPointIsHigherThanAnyToTheSouth = day8.isHigherThanAllSouth(2, 1, grid)
        self.assertTrue(highPointIsHigherThanAnyToTheSouth)

        lowPointIsHigherThanAnyToTheSouth = day8.isHigherThanAllSouth(1, 2, grid)
        self.assertFalse(lowPointIsHigherThanAnyToTheSouth)

    def test_getNumberOfTreesVisibleToNorthOf(self):
        grid = [[1, 2, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [6, 5, 2, 3, 4],
                [1, 3, 6, 1, 2]]
        shouldBeTwo = day8.getNumberOfTreesVisibleToNorthOf(2, 1, grid)
        self.assertEquals(shouldBeTwo, 2)
        shouldBeThree = day8.getNumberOfTreesVisibleToNorthOf(3, 2, grid)
        self.assertEquals(shouldBeThree, 3)
        shouldBeOne = day8.getNumberOfTreesVisibleToNorthOf(1, 2, grid)
        self.assertEquals(shouldBeOne, 1)
        shouldBeOne = day8.getNumberOfTreesVisibleToNorthOf(2, 4, grid)
        self.assertEquals(shouldBeOne, 1)

    def test_getNumberOfTreesVisibleToEastOf(self):
        grid = [[1, 2, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [6, 5, 2, 3, 4],
                [1, 3, 6, 1, 2]]
        shouldBeTwo = day8.getNumberOfTreesVisibleToEastOf(3, 2, grid)
        self.assertEquals(shouldBeTwo, 2)
        shouldBeThree = day8.getNumberOfTreesVisibleToEastOf(2, 1, grid)
        self.assertEquals(shouldBeThree, 3)
        shouldBeOne = day8.getNumberOfTreesVisibleToEastOf(1, 3, grid)
        self.assertEquals(shouldBeOne, 1)
        shouldBeOne = day8.getNumberOfTreesVisibleToEastOf(0, 3, grid)
        self.assertEquals(shouldBeOne, 1)

    def test_getNumberOfTreesVisibleToSouthOf(self):
        grid = [[1, 6, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [6, 5, 2, 3, 4],
                [1, 3, 6, 1, 2]]
        shouldBeTwo = day8.getNumberOfTreesVisibleToSouthOf(1, 4, grid)
        self.assertEquals(shouldBeTwo, 2)
        shouldBeThree = day8.getNumberOfTreesVisibleToSouthOf(0, 1, grid)
        self.assertEquals(shouldBeThree, 3)
        shouldBeOne = day8.getNumberOfTreesVisibleToSouthOf(1, 1, grid)
        self.assertEquals(shouldBeOne, 1)
        shouldBeOne = day8.getNumberOfTreesVisibleToSouthOf(0, 3, grid)
        self.assertEquals(shouldBeOne, 1)

    def test_getNumberOfTreesVisibleToWestOf(self):
        grid = [[1, 6, 3, 4, 5],
                [2, 2, 3, 4, 5],
                [6, 5, 2, 3, 4],
                [1, 3, 6, 1, 2]]
        shouldBeTwo = day8.getNumberOfTreesVisibleToWestOf(1, 2, grid)
        self.assertEquals(shouldBeTwo, 2)
        shouldBeThree = day8.getNumberOfTreesVisibleToWestOf(2, 4, grid)
        self.assertEquals(shouldBeThree, 3)
        shouldBeOne = day8.getNumberOfTreesVisibleToWestOf(1, 1, grid)
        self.assertEquals(shouldBeOne, 1)
        shouldBeOne = day8.getNumberOfTreesVisibleToWestOf(2, 2, grid)
        self.assertEquals(shouldBeOne, 1)

    def test_getScenicScore(self):
        grid = [[3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0]]
        score = day8.getScenicScore(3, 2, grid)
        self.assertEquals(8, score)
        score = day8.getScenicScore(0, 3, grid)
        self.assertEquals(12, score)

    def test_getTreeHavingHighestScenicScore(self):
        grid = [[3, 0, 3, 7, 3],
                [2, 5, 5, 1, 2],
                [6, 5, 3, 3, 2],
                [3, 3, 5, 4, 9],
                [3, 5, 3, 9, 0]]
        tree, score = day8.getTreeHavingHighestScenicScore(grid)
        self.assertEquals(8, score)
        self.assertEquals(3, tree[0])
        self.assertEquals(2, tree[1])

if __name__ == '__main__':
    unittest.main()
