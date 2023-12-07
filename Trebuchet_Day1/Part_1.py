
with open("Day1/input.txt") as file:
    input = file.read().splitlines()

final = 0

for v in input:
    numbers = ''.join(filter(str.isdigit, v))
    final += int(numbers[0] + numbers[-1])

print(final)