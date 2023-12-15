with open("Day7_CamelCard/input.txt") as file:
    input = file.read().splitlines()

symbolOrder = 'A,K,Q,J,T,9,8,7,6,5,4,3,2'.split(',')

symbolOrderMap = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'J': 'd',
    'T': 'e',
    '9': 'f',
    '8': 'g',
    '7': 'h',
    '6': 'i',
    '5': 'j',
    '4': 'k',
    '3': 'l',
    '2': 'm'
}

final = 0

class Hand:
    def __init__(self, hand, value):
        self.handMap = {}
        for card in hand:
            if card in self.handMap.keys():
                self.handMap[card] += 1
            else:
                self.handMap[card] = 1

        self.value = int(value)

        self.comparison = ''

        self.fullRateing = 0

        self.hand = hand

        self.rateHand()

    def rateHand(self):
        cardCount = list(self.handMap.values())

        cardCount.sort(reverse=True)

        handType = 0

        if len(cardCount) == 1:
            handType = 1
        elif len(cardCount) == 2:
            if cardCount[0] == 4:
                handType = 2
            if cardCount[0] == 3:
                handType = 3
        elif len(cardCount) == 3:
            if cardCount[0] == 3:
                handType = 4
            if cardCount[0] == 2:
                handType = 5
        elif len(cardCount) == 4:
            handType = 6
        elif len(cardCount) == 5:
            handType = 7

        cardComparisonValue = ''

        for card in self.hand:
            cardComparisonValue += symbolOrderMap[card]

        self.comparison = str(handType) + cardComparisonValue
        

hands = []

for line in input:
    hands.append(Hand(line.split()[0], int(line.split()[1])))

hands.sort(key=lambda x: x.comparison, reverse=True)

for index, hand in enumerate(hands):
    final += hand.value * (index + 1)

print(final)