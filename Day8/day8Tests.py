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


if __name__ == '__main__':
    unittest.main()
