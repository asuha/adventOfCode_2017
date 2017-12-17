with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day8/input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    hashValues = {}
    highestValue = 0

    for line in input:
        values = line.split(' ')

        if values[0] not in hashValues:
            hashValues[values[0]] = 0
        if values[4] not in hashValues:
            hashValues[values[4]] = 0

        signal = '-'
        if values[1] == 'inc':
            signal = '+'
        
        result = eval(str(hashValues[values[4]]) + values[5] + values[6])

        if result:
            equationResult = eval(str(hashValues[values[0]]) + signal + values[2])
            hashValues[values[0]] = equationResult
            if equationResult > highestValue:
                highestValue = equationResult
            

    print("Parte 1: " + str(max(hashValues.values())))
    print("Parte 2: " + str(highestValue))

        
