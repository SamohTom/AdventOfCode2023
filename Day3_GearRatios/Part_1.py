with open("Day3_GearRatios/input.txt") as file:
    input = file.read().splitlines()

symbols = list('.1234567890')

final = 0

class Number:
    def __init__(self, number, xEnd, y):
        self.isPart = False
        self.number = int(number)
        self.xEnd = xEnd
        self.y = y

        self.xStart = xEnd - len(number) + 1


    
    def checkSpot(self, x, y):
        if self.xStart <= x and x <= self.xEnd and self.y == y:
            self.isPart = True 
    
numbers = []

spots = []
    

for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char not in symbols: 
            spots.append([x-1, y-1])
            spots.append([x, y-1])
            spots.append([x+1, y-1])
            spots.append([x+1, y])
            spots.append([x+1, y+1])
            spots.append([x, y+1])
            spots.append([x-1, y+1])
            spots.append([x-1, y])


isNumber = False
numberString = ''

for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char.isdigit():
            isNumber = True
            numberString += char
        else:
            if isNumber:
                isNumber = False
                numbers.append(Number(numberString, x-1, y))
                numberString = ''
    if isNumber:
        isNumber = False
        numbers.append(Number(numberString, len(line)-1, y))
        numberString = ''

for spot in spots:
    for number in numbers:
        number.checkSpot(spot[0], spot[1])

for number in numbers:
    if number.isPart:
        final += number.number

print(final)