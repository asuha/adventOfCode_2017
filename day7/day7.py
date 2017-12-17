class Node:
    def __init__(self, root, key, weight):
        self.root = root
        self.weight = weight
        self.totalWeight = weight
        self.key = key
        self.childrens = []

    def addChildrens(self, childrens):
        self.childrens.extend(childrens)
        self.calculateTotalWeight()


    def calculateTotalWeight(self):
        self.totalWeight = self.weight
        for children in self.childrens:
            self.totalWeight += children.totalWeight



with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day7/input.txt', 'r') as inputFile:
    input = inputFile.read()

    inputHash = input.split('\n')

    def parte1(inputHash):
        allChildren = []
        keys = []

        for value in inputHash:
            value = value.replace("\r","")
            if '->' in value:
                splittedValues = value.split(" -> ")
                
                children = splittedValues[1:]
                children = children[0].split(', ')
                
                key = splittedValues[0].split(' (')[0]

                allChildren.extend(children)
                keys.append(key)
            else:
                key = value.split(' (')[0]
                keys.append(key)
        
        return (set(keys) - set(allChildren)).pop()

    def getKeys(inputHash):
        keys = {}
        for value in inputHash:
            value = value.replace("\r","")
            values = value.split(' ')
            key = values[0]
            weight = values[1].replace('(', '').replace(')', '')

            keys[key] = weight

        return keys

    def getChildren(inputHash):
        childrenList = {}
        for value in inputHash:
            value = value.replace("\r","")
            if '->' in value:
                splittedValues = value.split(" -> ")
                
                children = splittedValues[1:]
                children = children[0].split(', ')
                
                key = splittedValues[0].split(' (')[0]

                childrenList[key] = children

        return childrenList

    def createTree(rootKey, weightList, childrenList):
        tree = Node(None, rootKey, int(weightList[rootKey]))
        
        tree.addChildrens(createChildren(rootKey,  childrenList, weightList))

        return tree


    def createChildren(root, childrenList, weightList):
        childrens = []
        children = []
        if root in childrenList:
            children = childrenList[root]

        for c in children:
            weight = int(weightList[c])

            childrens.append(Node(root, c, weight))

        if len(childrens) > 0:
            for c in childrens:
                c.addChildrens(createChildren(c.key, childrenList, weightList))

        return childrens


    def parte2(inputHash):
        root = parte1(inputHash)
        weightList = getKeys(inputHash)
        childrenList = getChildren(inputHash)

        tree = createTree(root, weightList, childrenList)
        # calculateTreeIssue(tree)
        
    print(parte1(inputHash))
    #parte2 done via debug






