data = open("data.txt", "r")

elves = []
currentCals = 0
highest = 0
index=0
for line in data:
    if len(elves) <= index:
        elves.append(0)
    if line == '\n':
        currentCals = 0
        index += 1
        continue
    elves[index] += int(line)

elves.sort(reverse=True)
print(elves[0], elves[1], elves[2])
print(elves[0] + elves[1] + elves[2])
