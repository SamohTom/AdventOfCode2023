with open("Day2_CubeConundrum/input.txt") as file:
    input = file.read().splitlines()


numberMap = {}

final = 0

for line in input:
    values = line.split(':')

    id = int(values[0].replace('Game ', ''))

    cubeSets = values[1].split(';')

    colorCounter = {'red': 0,
                'green': 0,
                'blue': 0}

    for cubeSet in cubeSets:
        colors = cubeSet.split(',')

        for color in colors:
            numberColor = color.split(" ")
            numberColor.remove('')

            if int(numberColor[0]) > colorCounter[numberColor[1]]:
                colorCounter[numberColor[1]] = int(numberColor[0])
            


    final += colorCounter['red'] * colorCounter['green'] * colorCounter['blue']
    


print(final)