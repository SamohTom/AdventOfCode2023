with open("Day6_WaitForIt/input.txt") as file:
    input = file.read().splitlines()

times = list(map(lambda x: int(x), input[0].split(':')[1].split()))

distances = list(map(lambda x: int(x), input[1].split(':')[1].split()))

final = 1

for index, time in enumerate(times):
    buttonTime = 0

    distancesReached = []

    while buttonTime <= time:
        distancesReached.append((time - buttonTime)*buttonTime)
        buttonTime += 1

    final *= len(list(filter(lambda x: x > distances[index], distancesReached)))

print(final)

