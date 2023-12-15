symbolOrder = 'A,K,Q,J,T,9,8,7,6,5,4,3,2'.split(',')


symbolOrder.sort()

test = 'aA,bK,cQ,dJ,eT,f9,g8,h7,i6,j5,k4,l3,m2'.split(',')

test.sort()

print(test)


test2 = ['1acbd', '1caaa', '1bfjk', '1cbaa', '1caaa', '2aaaa']

test2.sort()

print(test2)

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


print(symbolOrderMap.items())