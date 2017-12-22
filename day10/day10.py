with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day10/input.txt', 'r') as inputFile:
    input = inputFile.read()

    def part1(input, lastRoundInfo):
        def createRoundList(listLenght):
            roundList = []
            currentIndex = 0
            
            while currentIndex < listLenght:
                roundList.append(currentIndex)
                currentIndex += 1
            
            return roundList

        def getCurrentRoundList(roundList, currentPos, lenght):
            currentRound = []

            if (lenght + currentPos) <= len(roundList):
                currentRound = roundList[currentPos:currentPos + lenght]
            else:
                totalLenght = lenght + currentPos
                lenghtFromBegin = totalLenght % len(roundList)
                end = roundList[currentPos: totalLenght]
                begin = (roundList[0: lenghtFromBegin])

                currentRound.extend(end)
                currentRound.extend(begin)
            
            return currentRound

        def replaceValuesInRoundList(currentPos, newValues, roundList):
            pos = currentPos
            for element in newValues:
                if pos >= len(roundList):
                    pos = pos % len(roundList)
                
                roundList[pos] = element
                pos += 1


        def orderRoundList(input, roundList, currentPos, skipSize):
            if currentPos == None:
                currentPos = 0
            if skipSize == None:
                skipSize = 0
            
            for lenght in input:
                lenght = int(lenght)

                if lenght > len(roundList):
                    continue

                currentList = getCurrentRoundList(roundList, currentPos, lenght)

                reorderedList = list(reversed(currentList))

                replaceValuesInRoundList(currentPos, reorderedList, roundList)

                currentPos += lenght + skipSize
                currentPos = currentPos % len(roundList)
                skipSize += 1

            hashToReturn = {}
            hashToReturn['currentPos'] = currentPos
            hashToReturn['skipSize'] = skipSize

            return hashToReturn

        if lastRoundInfo['list'] == None:
            roundList = createRoundList(256)
        else:
            roundList = lastRoundInfo['list']

        hashToReturn = orderRoundList(input, roundList, lastRoundInfo['currentPos'], lastRoundInfo['skipSize'])
        #print('Multiplying the first 2 values: ',(roundList[0]*roundList[1]))

        hashToReturn['list'] = roundList

        return hashToReturn

    def part2(input):
        inputAscii = [ord(c) for c in input]
        newInput = ','.join(str(e) for e in inputAscii) + ',17,31,73,47,23'
        newInput = newInput.split(',')

        lastRoundInfo = {}
        lastRoundInfo['list'] = None
        lastRoundInfo['currentPos'] = None
        lastRoundInfo['skipSize'] = None


        count = 64
        while count > 0:
            lastRoundInfo = part1(newInput, lastRoundInfo)

            count -= 1

        roundList = lastRoundInfo['list']

        denseHash = []
        i = 0
        while i <= 255:
            curArray = roundList[i:i+16]

            lastResult = curArray[0]
            for j,v in enumerate(curArray):
                if j == 0:
                    continue
                
                lastResult = lastResult^v

            denseHash.append(lastResult)
            i += 16

        hexArray = []
        
        for v in denseHash:
            hexArray.append('{0:02x}'.format(v))

        hashResult = ''.join(str(e) for e in hexArray)

        print(hashResult)

    part1(input.split(','), None)

    part2(input)

    




