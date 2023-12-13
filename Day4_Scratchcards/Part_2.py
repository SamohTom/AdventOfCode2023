with open("Day4_Scratchcards/input.txt") as file:
    input = file.read().splitlines()

final = 0

cardWins = {}
cards = {}

for line in input:

    allNumbers = line.split(':')[1].split('|')

    cardNumber = int(line.split(':')[0].split()[1])

    winningNumbers = allNumbers[0].split()
    yourNumbers = allNumbers[1].split()


    matchingNumbers = []

    for number in yourNumbers:
        if number in winningNumbers:   
            matchingNumbers.append(number)


    cardWins[cardNumber] = len(matchingNumbers)
    cards[cardNumber] = 1


cardList = list(cardWins.keys())

for key in cardWins.keys():
    for copyKey in cardList[key: key + cardWins[key]]:
        cards[copyKey] += cards[key]
    

print(sum(list(cards.values())))

