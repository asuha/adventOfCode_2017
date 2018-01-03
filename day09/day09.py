class Stack :
    def __init__(self) :
        self.items = []
        self.count = 0

    def push(self, item) :
        self.items.append(item)

    def pop(self) :
        self.count += len(self.items)
        return self.items.pop()

    def isEmpty(self) :
        return (self.items == [])

    def getCount(self):
        return self.count

with open('./input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    stack = Stack()
    ignoreGarbage = False
    ignoreNext = False
    group = 0
    garbageCount = 0

    for c in input[0]:
        
        if ignoreNext == True:
            ignoreNext = False
            continue

        if ignoreGarbage == True:
            if c == '>':
                ignoreGarbage = False
            elif c == '!':
                ignoreNext = True
            else:
                garbageCount += 1
            continue

        if c == '<':
            ignoreGarbage = True
            continue

        if c == '!':
            ignoreNext = True
            continue
            
        if c == '{':
            stack.push('{')

        if c == '}':
            stack.pop()

    print('Parte 1: ' + str(stack.getCount()))
    print('Parte 2: ' + str(garbageCount))