with open("Day6_WaitForIt/input.txt") as file:
    input = file.read().splitlines()

time = int(''.join(filter(str.isdigit ,input[0].split(':')[1])))

distance = int(''.join(filter(str.isdigit, input[1].split(':')[1])))

final = 0

hasReached = False

buttonTime = 0

while not hasReached:
    if (time - buttonTime) * buttonTime > distance:
        hasReached = True
    else:
        buttonTime += 1

print(time - buttonTime*2 + 1)

