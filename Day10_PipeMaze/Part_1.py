with open('Day10_PipeMaze/input.txt') as file:
    input = file.read().splitlines()

pipeMap = list(map(lambda x: list(x), input))


for y, pipe in enumerate(pipeMap):
    for x, tile in enumerate(pipe):
        if tile == 'S':
            start = (x, y)


numberMap = []

for i in range(len(pipeMap)):
    newLine = []
    for j in range(len(pipeMap[i])):
        newLine.append('.')
    numberMap.append(newLine)



def aStar(pre, cur):
    x = cur[0]
    y = cur[1]
    preX = pre[0]
    preY = pre[1]
    thisTile = pipeMap[y][x]

    if thisTile == "|" :
        if preY - y < 0:
            nextTile = (x, y + 1)
        else:
            nextTile = (x, y - 1)
    elif thisTile == '-':
        if preX - x < 0:
            nextTile = (x + 1, y)
        else:
            nextTile = (x - 1, y)
    elif thisTile == 'L':
        if preY - y < 0:
            nextTile = (x + 1, y )
        else:
            nextTile = (x, y - 1)
    elif thisTile == 'J':
        if preY - y < 0:
            nextTile = (x - 1, y)
        else:
            nextTile = (x, y - 1)
    elif thisTile == '7':
        if y - preY < 0:
            nextTile = (x - 1, y)
        else:
            nextTile = (x, y + 1)
    elif thisTile == 'F':
        if y - preY < 0:
            nextTile = (x + 1, y)
        else:
            nextTile = (x, y + 1)
    elif thisTile == 'S':
        nextTile = pre


    nx = nextTile[0]
    ny = nextTile[1]

    if numberMap[ny][nx] != '.':
        return None, None

    numberMap[ny][nx] = '0'

    return nextTile, cur

def findStartNodes(start):
    x = start[0]
    y = start[1]

    top = pipeMap[y-1][x]
    right = pipeMap[y][x+1]
    bottom = pipeMap[y+1][x]
    left = pipeMap[y][x-1]

    startNodes = []

    if top == '|' or top == 'F' or top == '7':
        startNodes.append((x, y-1))
    if right == '7' or right == '-' or right == 'J':
        startNodes.append((x+1, y))
    if bottom == '|' or bottom == 'J' or bottom == 'L':
        startNodes.append((x, y+1))
    if left == '-' or left == 'F' or left == 'L':
        startNodes.append((x+1, y))
    
    return startNodes[0], startNodes[1]


currentNode = findStartNodes(start)[0]
prevNode = start

numberMap[currentNode[1]][currentNode[0]] = '0'

steps = 0
    
while currentNode != None:
    newNodes = aStar(prevNode, currentNode)

    currentNode = newNodes[0]
    prevNode = newNodes[1]
    steps += 1


for line in numberMap:
    print(line)

print(steps/2)


