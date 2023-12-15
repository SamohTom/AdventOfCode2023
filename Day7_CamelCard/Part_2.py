with open("Day7_CamelCard/input.txt") as file:
    input = file.read().splitlines()

symbolOrderMap = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'T': 'd',
    '9': 'e',
    '8': 'f',
    '7': 'g',
    '6': 'h',
    '5': 'i',
    '4': 'j',
    '3': 'k',
    '2': 'l',
    'J': 'm',
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
        if 'J' in self.handMap.keys():
            joker = self.handMap['J']

            items = list(self.handMap.items())

            items.sort(key=lambda x: x[1], reverse=True)

            if len(items) > 1:
                if len(items) == 3 and items[0][1] == 2 and items[1][1] == 2 and items[2][0] == 'J':
                    self.handMap[items[0][0]] += 1
                else:
                    if items[0][0] == 'J':
                        self.handMap[items[1][0]] += joker
                    else:
                        self.handMap[items[0][0]] += joker
                

                self.handMap.pop('J')


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

        # print(self.hand)
        # print(self.comparison)
        

hands = []

for line in input:
    hands.append(Hand(line.split()[0], int(line.split()[1])))

hands.sort(key=lambda x: x.comparison, reverse=True)



for index, hand in enumerate(hands):
    final += hand.value * (index + 1)

print(final)