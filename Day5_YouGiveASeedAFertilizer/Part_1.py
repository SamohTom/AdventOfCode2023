with open("Day5_YouGiveASeedAFertilizer/input.txt") as file:
    input = file.read()

seeds = input.split('\n\n')[0].split(':')[1].split()
undecodedMaps = input.split('\n\n')[1:]

undecodedMaps = list(map(lambda x: x.split('\n'), undecodedMaps))

class Map:
    def __init__(self, entries, source, destination):
        entryList = list(map(lambda x: x.split(), entries))
        self.entries = []
        for stringMap in entryList:
            self.entries.append(list(map(lambda x: int(x), stringMap)))
        self.source = source
        self.destination = destination

    def mapSource(self, source) -> int:
        hasEntry = False
        for entry in self.entries:
            if entry[1] <= int(source) and int(source) <= entry[1] + entry[2] - 1:
                hasEntry = True
                return entry[0] + (int(source) - entry[1])
            
        return int(source)
        
plantingMaps = []

for undecodedMap in undecodedMaps:
    sd = undecodedMap[0].replace(' map:', '')
    plantingMaps.append(Map(undecodedMap[1:], sd.split('-')[0], sd.split('-')[2]))

current = 'seed'

while current != 'location':
    for plantingMap in plantingMaps: 
        if current == plantingMap.source:
            for index, seed in enumerate(seeds):
                seeds[index] = plantingMap.mapSource(seed)
            current = plantingMap.destination
        
print(min(seeds))