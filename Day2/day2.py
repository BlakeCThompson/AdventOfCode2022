
mapping = {'A': 1, 'B': 2, 'C': 3}
comboMapping = {'X': 'A', 'Y': 'B', 'Z': 'C'}
losses = ['A Z', 'B X', 'C Y']
wins = ['A Y', 'B Z', 'C X']


def isWin(combo: str):
    return combo in wins


def isLoss(combo: str):
    return combo in losses


def calculateComboValue(combo: str):
    choiceVal = mapping[comboMapping[combo.partition(' ')[2]]]
    if isWin(combo):
        return choiceVal + 6
    elif isLoss(combo):
        return choiceVal
    return choiceVal + 3


def part1():
    data = open("Day2/data.txt", "r")
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
        total += calculateComboValue(line[:-1])
    print(total)
    data.close()

part1()


newWinningMapping = {'A': 'B', 'B': 'C', 'C': 'A'}
newLosingMapping = {'A': 'C', 'B': 'A', 'C': 'B'}
newDrawMapping = {'A': 'A', 'B': 'B', 'C': 'C'}
scenarioValues = {'X': 0, 'Y': 3, 'Z': 6}


def calculateComboValue2(combo:str):
    scenario = combo.partition(' ')[2]
    comboVal = scenarioValues[scenario]
    match scenario:
        case 'X':
            return comboVal + mapping[newLosingMapping[combo.partition(' ')[0]]]
        case 'Y':
            return comboVal + mapping[newDrawMapping[combo.partition(' ')[0]]]
        case 'Z':
            return comboVal + mapping[newWinningMapping[combo.partition(' ')[0]]]


def part2():
    data = open("Day2/data.txt", "r")
    # "Anyway, the second column says how the round needs to end:
    # X means you need to lose,
    # Y means you need to end the round in a draw, and
    # Z means you need to win
    print("part 2:")
    total = 0
    for line in data:
        total += calculateComboValue2(line[:-1])
    print(total)
    data.close()

part2()