import day11

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
        self.assertIsInstance(monkey0.test, day11.Test)

    def testTestDivisibleBy(self):
        testDivisibleBy = day11.TestDivisibleBy('Test: divisible by 17')
        self.assertTrue(testDivisibleBy.testPasses(17))
        self.assertTrue(testDivisibleBy.testPasses(34))
        self.assertFalse(testDivisibleBy.testPasses(15))
        self.assertFalse(testDivisibleBy.testPasses(20))


    def testOperation(self):
        operation = day11.Operation('Operation: new = old + 3')
        testDivisibleBy17 = day11.TestDivisibleBy('Test: divisible by 17')

        monkey1 = day11.Monkey(0, [15, 48], operation, testDivisibleBy17, 1, 2)
        self.assertEqual(0, monkey1.getNumberOfItemsInspected())
        monkey2 = day11.Monkey(1, [], day11.Operation('Operation: new = old * 2'), day11.TestDivisibleBy('Test: divisible by 5'), 0, 2)
        monkey3 = day11.Monkey(2, [], day11.Operation('Operation: new = old / 3'), day11.TestDivisibleBy('Test: divisible by 4'), 0, 1)
        monkey1.setTrueMonkey(monkey2)
        monkey1.setFalseMonkey(monkey3)
        monkey1.execute()

        self.assertEqual(2, monkey1.getNumberOfItemsInspected())

        self.assertEqual(0, len(monkey1.itemWorryLevels), 'monkey should have passed item 1 to monkey3 and item 2 to monkey2')
        self.assertEqual(6, monkey3.itemWorryLevels[0])
        self.assertEqual(17, monkey2.itemWorryLevels[0])
        monkey1.execute()
        self.assertEqual(0, len(monkey1.itemWorryLevels))

    def testParseStartingItems(self):
        startingItemsString = '  Starting items: 71, 56, 50, 73'
        startingItems = day11.parseStartingItems(startingItemsString)
        self.assertEqual(4, len(startingItems))
        self.assertEqual(71, startingItems[0])
        self.assertEqual(56, startingItems[1])
        self.assertEqual(50, startingItems[2])
        self.assertEqual(73, startingItems[3])
    def getMonkeyGroupOfThree(self):
        monkeyGroup = day11.MonkeyGroup()
        monkeyString0 = '''Monkey 0:
                  Starting items: 1, 2, 3
                  Operation: new = old + 1
                  Test: divisible by 3
                    If true: throw to monkey 1
                    If false: throw to monkey 2
                '''
        monkey0 = day11.parseMonkeyObjectFromString(monkeyString0)
        monkeyString1 = '''Monkey 1:
                  Starting items: 63
                  Operation: new = old + 3
                  Test: divisible by 6
                    If true: throw to monkey 0
                    If false: throw to monkey 2'''
        monkey1 = day11.parseMonkeyObjectFromString(monkeyString1)
        monkeyString2 = '''Monkey 2:
                  Starting items: 74
                  Operation: new = old + 3
                  Test: divisible by 6
                    If true: throw to monkey 0
                    If false: throw to monkey 1'''
        monkey2 = day11.parseMonkeyObjectFromString(monkeyString2)
        monkeyGroup.addMonkey(monkey0)
        monkeyGroup.addMonkey(monkey1)
        monkeyGroup.addMonkey(monkey2)
        return monkeyGroup
    def testMonkeyGroup(self):
        monkeyGroup = self.getMonkeyGroupOfThree()
        self.assertEqual(3, len(monkeyGroup.monkeys))

    def testParseMonkeyIndexFromString(self):
        trueString = '            If true: throw to monkey 0'
        index = day11.parseMonkeyIndexFromString(trueString)
        self.assertEqual(0, index)

    def testParseFalseMonkeyIndex(self):
        falseString = '            If false: throw to monkey 1'
        index = day11.parseMonkeyIndexFromString(falseString)
        self.assertEqual(1, index)


    def testMonkeyGroupExecute(self):
        monkeyGroup = day11.MonkeyGroup()
        monkeyString0 = '''Monkey 0:
                          Starting items: 1, 2, 3
                          Operation: new = old + 1
                          Test: divisible by 3
                            If true: throw to monkey 1
                            If false: throw to monkey 2
                        '''
        monkey0 = day11.parseMonkeyObjectFromString(monkeyString0)
        monkeyString1 = '''Monkey 1:
                          Starting items: 63
                          Operation: new = old + 3
                          Test: divisible by 6
                            If true: throw to monkey 0
                            If false: throw to monkey 2'''
        monkey1 = day11.parseMonkeyObjectFromString(monkeyString1)
        monkeyString2 = '''Monkey 2:
                          Starting items: 74
                          Operation: new = old + 3
                          Test: divisible by 6
                            If true: throw to monkey 0
                            If false: throw to monkey 1'''
        monkey2 = day11.parseMonkeyObjectFromString(monkeyString2)
        monkeyGroup.addMonkey(monkey0)
        monkeyGroup.addMonkey(monkey1)
        monkeyGroup.addMonkey(monkey2)
        monkeyGroup.executeOnAll()
        self.assertEqual(monkeyGroup.monkeys[0].inspectedItems, [1, 2, 3])
        self.assertEqual(monkeyGroup.monkeys[1].inspectedItems, [63])
        self.assertEqual(monkeyGroup.monkeys[2].inspectedItems, [74])
        monkeyGroup.executeOnAll()

    def testGetMonkeyByIndex(self):
        monkeyGroup = day11.MonkeyGroup()
        monkeyString0 = '''Monkey 0:
                  Starting items: 1, 2, 3
                  Operation: new = old + 1
                  Test: divisible by 3
                    If true: throw to monkey 1
                    If false: throw to monkey 2
                '''
        monkey0 = day11.parseMonkeyObjectFromString(monkeyString0)
        monkeyString1 = '''Monkey 1:
                  Starting items: 63
                  Operation: new = old + 3
                  Test: divisible by 6
                    If true: throw to monkey 0
                    If false: throw to monkey 2'''
        monkey1 = day11.parseMonkeyObjectFromString(monkeyString1)
        monkeyString2 = '''Monkey 2:
                  Starting items: 74
                  Operation: new = old + 3
                  Test: divisible by 6
                    If true: throw to monkey 0
                    If false: throw to monkey 1'''
        monkey2 = day11.parseMonkeyObjectFromString(monkeyString2)
        monkeyGroup.addMonkey(monkey0)
        monkeyGroup.addMonkey(monkey1)
        monkeyGroup.addMonkey(monkey2)
        monkeyIndex = 2
        foundMonkey = monkeyGroup.getMonkeyByIndex(2)
        self.assertEqual(foundMonkey.index, monkeyIndex)
        monkeyIndex = 1
        foundMonkey = monkeyGroup.getMonkeyByIndex(monkeyIndex)
        self.assertEqual(foundMonkey.index, monkeyIndex)
        monkeyIndex = 0
        foundMonkey = monkeyGroup.getMonkeyByIndex(monkeyIndex)
        self.assertEqual(foundMonkey.index, monkeyIndex)
    def testMain(self):
        fileName = 'testData.txt'
        ioStream = open(fileName, 'r')
        monkeyStrings = day11.parseMonkeyStrings(ioStream)
        monkeyGroup = day11.MonkeyGroup()
        for monkeyString in monkeyStrings:
            monkeyGroup.addMonkey(day11.parseMonkeyObjectFromString(monkeyString))
        day11.executeOnAllXTimes(monkeyGroup)
        self.assertEqual(101, len(monkeyGroup.monkeys[0].inspectedItems))

if __name__ == '__main__':
    unittest.main()
