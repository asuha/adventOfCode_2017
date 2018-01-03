with open('./input.txt', 'r') as inputFile:
    input = inputFile.read()

    def parte1(): 
        inputList = input.split("\n")
        index = 0

        stepsCount = 0
        while True:
            previous  = index

            steps = int(inputList[index])
            stepsCount += 1

            if len(inputList) > (index + steps) and -1 < (index + steps) :
                inputList[previous] = int(inputList[previous])
                inputList[previous] = inputList[previous] + 1
                index = index + steps
            else:
                break;
        return stepsCount   

    def parte2():
        inputList = input.split("\n")
        index = 0

        stepsCount = 0
        while True:
            previous  = index

            steps = int(inputList[index])
            stepsCount += 1

            if len(inputList) > (index + steps) and -1 < (index + steps) :
                inputList[previous] = int(inputList[previous])
                if inputList[previous] > 2:
                    inputList[previous] = inputList[previous] - 1
                else:
                    inputList[previous] = inputList[previous] + 1
                index = index + steps
            else:
                break;
        
        return stepsCount
        
    print('Parte 1: ' + str(parte1()))
    print('Parte 2: ' + str(parte2()))