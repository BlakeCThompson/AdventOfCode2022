import string
import numpy


def findCommonItems(item1, item2):
    commonItems = []
    for char1 in item1:
        for char2 in item2:
            if char1 == char2:
                if char1 not in commonItems:
                    commonItems += char1
    return commonItems


def calculateItemPriorities(commonItems):
    values = calculateValues()
    totalValue = 0
    for char in commonItems:
        totalValue += values[char]
    return totalValue


def calculateValues():
    valueMap = {}
    val = 1
    for char in string.ascii_lowercase[:26]:
        valueMap[char] = val
        val += 1
    for char in string.ascii_uppercase[:26]:
        valueMap[char] = val
        val += 1
    return valueMap


def part1():
    data = open("Day3/data.txt", "r")
    # Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.
    #
    # Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.
    #
    # The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
    #
    # The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    print("part 1:")
    total = 0
    for line in data:
        line = line[:-1]
        firstHalf = line[int(len(line)/2):]
        latterHalf = line[:int(len(line)/2)]
        commonItems = findCommonItems(firstHalf, latterHalf)
        total += calculateItemPriorities(commonItems)

    print(total)
    data.close()

part1()

def findCommonItemsForElfGroups(rucksacks: dict):
    rucksacks = rucksacks.values()
    rucksacks = list(rucksacks)
    rucksacks = numpy.array(rucksacks)
    commonItems = rucksacks[0]
    for rucksack in rucksacks[1:]:
        commonItems = findCommonItems(commonItems, rucksack)
    return commonItems


def part2():
    data = open("Day3/data.txt", "r")
    # "Anyway, the second column says how the round needs to end:
    # X means you need to lose,
    # Y means you need to end the round in a draw, and
    # Z means you need to win
    print("part 2:")
    total = 0

    elfGroupCapacity = 3
    badges = []
    rucksackBuffer = {}
    i = 0
    for line in data:
        if len(rucksackBuffer) % elfGroupCapacity == 0:
            # reset buffer every elf grouping
            rucksackBuffer = {}
        rucksackBuffer[i] = line[:-1]
        i += 1
        if len(rucksackBuffer) % elfGroupCapacity == 0:
            commonItems = findCommonItemsForElfGroups(rucksackBuffer)
            for commonItem in commonItems:
                total += calculateItemPriorities(commonItem)

    print(total)
    data.close()

part2()