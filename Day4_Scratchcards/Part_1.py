with open("Day4_Scratchcards/input.txt") as file:
    input = file.read().splitlines()

final = 0

for line in input:

    isMatch = False


    allNumbers = line.split(':')[1].split('|')

    winningNumbers = allNumbers[0].split()
    yourNumbers = allNumbers[1].split()


    matchingNumbers = []

    for number in yourNumbers:
        if number in winningNumbers:   
            isMatch = True
            matchingNumbers.append(number)


    if isMatch:
        final += pow(2, len(matchingNumbers)-1)

print(final)
