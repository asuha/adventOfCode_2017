with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day12/input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    def find_dependencies(key, groups):
        group = input[key]

        ck = group.split(' <-> ')
        ck[0] = int(ck[0])

        if ck[0] not in groups:
            groups.add(ck[0])
        else:
            return

        for v in ck[1].split(', '):
            find_dependencies(int(v), groups)

        return groups

    allKeys = set()
    for v in input:
        allKeys.add(int(v.split(' <-> ')[0]))
    
    count = 0
    while len(allKeys) > 0:
        key = allKeys.pop()
        group = find_dependencies(key, set())
        
        if len(group) > 0:
            count += 1

        allKeys = allKeys - group