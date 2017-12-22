with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day13/input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    class Node :
        def __init__(self,lenght) :
            self.lenght = lenght
            self.reset()

        def moveOne(self) :
            self.checkDirection()
            if self.direction == '+':
                self.pos += 1
            else:
                self.pos -= 1
        
        def checkDirection(self):
            if self.pos == 1 and self.direction == '-':
                self.direction = '+'
            if self.pos == self.lenght and self.direction == '+':
                self.direction = '-'

        def isCaught(self):
            if self.pos == 1:
                return True
            else:
                return False
        
        def reset(self):
            self.pos = 1
            self.direction = '+'


    def create_Hash():
        myHash = {}
        for i in input:
            v = i.split(': ')
            myHash[int(v[0])] = Node(int(v[1]))
    
        return myHash

    # def run_Firewall(myHash):
    #     caught = []
    #     count = 0
    #     while count <= max(myHash):
    #         if count in myHash.keys():
    #             if myHash[count].isCaught():
    #                 caught.append(count)

    #         for i in myHash:
    #             myHash[i].moveOne()

    #         count += 1
        
    #     severity = 0
    #     for i in caught:
    #         severity += i * myHash[i].lenght
        
    #     print('Caught: ', caught)
    #     print('Severity: ', severity)
    #     return caught

    def run_Firewall(myHash, delay):
        caught = []
        count = 0
        startCount = False
        second = 0
        while count <= max(myHash):
            if count in myHash.keys() and delay <= second:
                if myHash[count].isCaught():
                    caught.append(count)
                    break
                startCount = True

            for i in myHash:
                myHash[i].moveOne()

            if startCount:
                count += 1
            second += 1

        return caught

    

    myHash = create_Hash()
    # run_Firewall(myHash, 0)

    delay = 10
    while True:

        for i in myHash:
            myHash[i].reset()

        run = run_Firewall(myHash, delay)
        if len(run) == 0:
            print('Delay: ', delay)
            break

        delay += 1


