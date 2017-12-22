import re
import math
with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day16//input.txt', 'r') as inputFile:
    input = inputFile.read().split(',')

    string = "abcde"
    programs = []
    map_characters = { }

    count = 1
    for v in string:
        result = int(math.pow(2, count)) - 1
        programs.append(result)
        map_characters[v] = result
        count +=1

    def spin(array, p):
        begin = array[:len(array) - p]
        end = array[len(array) - p:]

        return end + begin

    def exchange(array, k1, k2):
        v1 = array[k1]
        v2 = array[k2]

        if v1 > v2:
            array[k1] = v1 & v2
            array[k2] = v1 | v2
        else:
            array[k1] = v1 | v2
            array[k2] = v1 & v2

        return array

    def partner(array, v1, v2):
        return exchange(array, array.index(map_characters[v1]), array.index(map_characters[v2]))

    count = 0

    while count < 1000000000:
        for i in input:

            if i[0] == 's':
                value = re.match(r"[a-z]([0-9]+)", i).group(1)
                programs = spin(programs, int(value))
            elif i[0] == 'x':
                regex = re.match(r"[a-z]([0-9]+)/([0-9]*)", i)
                programs = exchange(programs, int(regex.group(1)), int(regex.group(2)))
            else:
                regex = re.match(r"[a-z]([a-z])/([a-z])", i)
                programs = partner(programs, regex.group(1), regex.group(2))
        count += 1
        if count % 1000000 == 0:
            print count
            
    print programs