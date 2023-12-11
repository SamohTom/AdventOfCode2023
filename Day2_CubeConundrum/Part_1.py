with open("Day2_CubeConundrum/input.txt") as file:
    input = file.read().splitlines()


numberMap = {}

final = 0

for line in input:
    values = line.split(':')

    id = int(values[0].replace('Game ', ''))

    possible = True

    cubeSets = values[1].split(';')

    for cubeSet in cubeSets:
        colors = cubeSet.split(',')

        colorCounter = {'red': 0,
                        'green': 0,
                        'blue': 0}


        for color in colors:
            numberColor = color.split(" ")
            numberColor.remove('')
            if numberColor[1] in colorCounter.keys():   
                colorCounter[numberColor[1]] += int(numberColor[0])
            else:
                colorCounter[numberColor[1]] = int(numberColor[0])

        if colorCounter['red'] > 12 or colorCounter['green'] > 13 or colorCounter['blue'] > 14:
            possible = False
            

    if possible:
        final += id

    print(colorCounter)

    


print(final)