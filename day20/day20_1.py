import re

with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day20/input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    p = list()
    v = list()
    a = list()

    for i in input:
        regex = re.match(r"p=<(.*)>, v=<(.*)>, a=<(.*)>", i)

        p.append([int(z) for z in regex.group(1).split(',')])
        v.append([int(x) for x in regex.group(2).split(',')])
        a.append([int(y) for y in regex.group(3).split(',')])

    minSum = 300
    index = 0
    for i,value in enumerate(a):
        x = value[0]
        y = value[1]
        z = value[2]

        summ = abs(x) + abs(y) + abs(z)

        if minSum > summ:
            minSum = summ
            index = i

    print("Parte 1: " + str(index))