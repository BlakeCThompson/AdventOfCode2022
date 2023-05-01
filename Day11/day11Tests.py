import Day11.day11
import Day11.day11 as day11

import unittest


class TestDay11(unittest.TestCase):
    def testParseMonkeyStrings(self):
        testFile = 'testData.txt'
        fileStream = open(testFile, 'r')
        monkeyStrings = day11.parseMonkeyStrings(fileStream)
        fileStream.close()
        self.assertEqual(4, len(monkeyStrings))
        for monkeyString in monkeyStrings:
            lines = monkeyString.split('\n')
            if lines[-1] == '':
                lines = lines[:-1]
            self.assertEqual(6, len(lines))


    def testParseMonkeyObjectFromString(self):
        monkeyString0 = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
'''
        lastMonkeyString = '''Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''
        monkey0 = day11.parseMonkeyObjectFromString(monkeyString0)
        # self.assertIsInstance(monkey0.test, day11.Test)

    def testTestDivisibleBy(self):
        testDivisibleBy = Day11.day11.TestDivisibleBy('Test: divisible by 17')
        self.assertTrue(testDivisibleBy.executeTest(17))
        self.assertTrue(testDivisibleBy.executeTest(34))
        self.assertFalse(testDivisibleBy.executeTest(15))
        self.assertFalse(testDivisibleBy.executeTest(20))


    def testOperation(self):
        operation = day11.Operation('Operation: new = old + 3')
        testDivisibleBy17 = Day11.day11.TestDivisibleBy('Test: divisible by 17')

        monkey = day11.Monkey([15, 14], operation, testDivisibleBy17)
        monkey.execute()
        self.assertEqual(18, monkey.items[0])
        self.assertEqual(17, monkey.items[1])
        monkey.execute()
        self.assertEqual(21, monkey.items[0])





if __name__ == '__main__':
    unittest.main()
