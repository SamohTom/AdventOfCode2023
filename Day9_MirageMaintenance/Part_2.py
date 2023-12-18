with open('Day9_MirageMaintenance/input.txt') as file:
    input = file.read().splitlines()

sequenzes = []

for line in input:
    sequenzes.append(list(map(lambda x: int(x), line.split())))

def recursivSequenzing(sequenz) -> int:
    newSequenz = []
    
    for i in range(1, len(sequenz)):
        newSequenz.append(sequenz[i] - sequenz[i-1])

    

    if list(sorted(newSequenz))[0] == 0 and list(sorted(newSequenz))[-1] == 0:
        return sequenz[0] 
    else:
        return sequenz[0] - recursivSequenzing(newSequenz)
    
final = 0

for sequenz in sequenzes:
    final += recursivSequenzing(sequenz)

print(final)