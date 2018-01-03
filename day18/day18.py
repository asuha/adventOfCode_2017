with open('./input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    variables = {}
    sound = 0
    pos = 0
   
    def is_int(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    def get_value(variables, value):
        if is_int(value):
            return int(value)
        return int(variables[value])

    while pos < len(input):
        line = input[pos].split(' ')

        pos += 1

        if line[1] not in variables: 
            variables[line[1]] = 0

        if len(line) > 2:
            p2 = get_value(variables, line[2])

        if line[0] == 'set':
            variables[line[1]] = p2

        elif line[0] == 'add':
            variables[line[1]] += p2

        elif line[0] == 'mul':
            variables[line[1]] *= p2

        elif line[0] == 'mod':
            variables[line[1]] = variables[line[1]] % p2

        elif line[0] == 'rcv':
            if variables[line[1]] != 0:
                print("Parte 1: " + str(sound))
                break
        
        elif line[0] == 'snd':
            sound = variables[line[1]]

        elif line[0] == 'jgz':
            p1 = get_value(variables, line[1])
            if p1 > 0:
                pos += p2 - 1