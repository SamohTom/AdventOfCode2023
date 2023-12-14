with open("Day3_GearRatios/input.txt") as file:
    input = file.read().splitlines()

symbols = list('.1234567890')

final = 0

#
# could be optimized by just compareing symbols with numbers in y-1; y+1
#


class Number:
    def __init__(self, number, xEnd, y):
        self.number = int(number)
        self.xEnd = xEnd
        self.y = y

        self.xStart = xEnd - len(number) + 1

    def checkSpot(self, x, y) -> bool:
        spots = [
            [x-1, y-1],
            [x, y-1],
            [x+1, y-1],
            [x+1, y],
            [x+1, y+1],
            [x, y+1],
            [x-1, y+1],
            [x-1, y]
        ]

        returnValue = False

        for spot in spots:
            if self.xStart <= spot[0] and spot[0] <= self.xEnd and self.y == spot[1]:
                returnValue = True

        return returnValue

class Spot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.numbers = []

    def checkNumber(self, numbers) -> int:
        for number in numbers:
            if number.checkSpot(self.x, self.y):
                self.numbers.append(number)

        if len(self.numbers) == 2:
            return self.numbers[0].number * self.numbers[1].number
        
        return 0
        

numbers = []

spots = []


for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char not in symbols:
            spots.append(Spot(x, y))


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

finalList = []


for spot in spots:
    finalList.append(spot.checkNumber(numbers))


print(sum(finalList))
