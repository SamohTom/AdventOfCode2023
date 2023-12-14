with open("Day5_YouGiveASeedAFertilizer/input.txt") as file:
    input = file.read()


# 
# not optimal but better than brute force all seeds
# maybe searching for optimal solution
#



seeds = input.split('\n\n')[0].split(':')[1].split()
undecodedMaps = input.split('\n\n')[1:]

undecodedMaps = list(map(lambda x: x.split('\n'), undecodedMaps))

ranges = seeds[1::2]
seeds = seeds[::2]

class Seed:
    def __init__(self, seed, range):
        self.seed = seed
        self.range = range
        self.endSeed = seed + range - 1 
    
    def isSeed(self, seed) -> bool:
        return self.seed <= seed and seed <= self.endSeed
    

class Map:
    def __init__(self, entries, source, destination):
        entryList = list(map(lambda x: x.split(), entries))
        self.entries = []
        for stringMap in entryList:
            self.entries.append(list(map(lambda x: int(x), stringMap)))
        self.source = source
        self.destination = destination

    def mapSource(self, source) -> int:
        for entry in self.entries:
            if entry[1] <= int(source) and int(source) <= entry[1] + entry[2] - 1:
                return entry[0] + (int(source) - entry[1])
            
        return int(source)
    
    def mapDestination(self, destination) -> int:
        for entry in self.entries:
            if entry[0] <= int(destination) and int(destination) <= entry[0] + entry[2] - 1:
                return entry[1] + (int(destination) - entry[0])
            
        return int(destination)
    
newSeeds = []

for i, currSeed in enumerate(seeds):
    newSeeds.append(Seed(int(currSeed), int(ranges[i])))
        
plantingMaps = []

for undecodedMap in undecodedMaps:
    sd = undecodedMap[0].replace(' map:', '')
    plantingMaps.append(Map(undecodedMap[1:], sd.split('-')[0], sd.split('-')[2]))


foundSeed = False
location = 0


while not foundSeed:
    current = 'location'
    currSeed = location
    for plantingMap in reversed(plantingMaps): 
        if current == plantingMap.destination:
            currSeed = plantingMap.mapDestination(currSeed)
            current = plantingMap.source
    for seed in newSeeds:
        if seed.isSeed(currSeed):
            foundSeed = True
            print(location)
    location += 1

