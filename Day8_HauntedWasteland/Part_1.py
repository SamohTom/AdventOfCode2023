with open("Day8_HauntedWasteland/input.txt") as file:
    input = file.read()

instructions = input.split('\n\n')[0]

inputNodes = input.split('\n\n')[1].splitlines()

LRMap = {
    'L': 0,
    'R': 1
}

nodes = {}


def createNodeKey(node, link):
    nodeKey = node.replace(' ', '')

    linkLeft = link.split(',')[0].replace('(', '').replace(' ', '')
    linkRight = link.split(',')[1].replace(')', '').replace(' ', '')


    return (nodeKey, linkLeft, linkRight)


for node in inputNodes:
    getKeyValue = createNodeKey(node.split('=')[0], node.split('=')[1])
    nodes[getKeyValue[0]] = (getKeyValue[1], getKeyValue[2])


current = 'AAA'
steps = 1

while current != 'ZZZ':
    instruction = instructions[(steps-1)%len(instructions)]
    current = nodes[current][LRMap[instruction]]

    steps += 1

print(steps-1)