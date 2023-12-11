
with open("Day1_Trebuchet/input.txt") as file:
    input = file.read().splitlines()

final = 0

numberStrings = 'one,two,three,four,five,six,seven,eight,nine'.split(',')
allNumbers = numberStrings  + '1,2,3,4,5,6,7,8,9'.split(',')
print(numberStrings)


for v in input:
    value = v

    first = [len(v)+1, '0']

    for number in allNumbers:

        firstFind = value.find(number)

        if(firstFind != -1 and firstFind < first[0]):
            first[0] = firstFind
            first[1] = number

    last = [-1, '0']

    for number in allNumbers:

        lastFind = value.rfind(number)

        if(lastFind != -1 and lastFind > last[0]):
            last[0] = lastFind
            last[1] = number
    print(value)
    print(first)
    print(last)

    for index, numberString in enumerate(numberStrings):
        first[1] = first[1].replace(numberString, str(index + 1))
        last[1] = last[1].replace(numberString, str(index + 1))
        
    final += int(str(first[1]) + str(last[1]))

print(final)

