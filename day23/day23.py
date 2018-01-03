with open('./input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    
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

    def run_instructions(variables, is_1):
        pos = 0
        if is_1:
            count_mul = 0

        while pos < len(input):
            line = input[pos].split(' ')

            pos += 1

            if (line[1] not in variables) and (is_int(line[1]) == False): 
                variables[line[1]] = 0

            if len(line) > 2:
                p2 = get_value(variables, line[2])

            if line[0] == 'set':
                variables[line[1]] = p2

            elif line[0] == 'sub':
                variables[line[1]] -= p2

            elif line[0] == 'mul':
                variables[line[1]] *= p2
                if is_1:
                    count_mul += 1

            elif line[0] == 'jnz':
                p1 = get_value(variables, line[1])
                if p2 == -8:
                    variables['e'] = variables['b']
                    # if (variables['b'] % variables['d'] == 0):
                    #     variables['f'] = 0
                    variables['g'] = 0
                elif p2 == -13:
                    variables['d'] = variables['b']
                    variables['g'] = 0
                    
                    e = 2
                    while e <= variables['b']:
                        d = variables['b'] % e
                        if (d == 0):
                            variables['f'] = 0
                            break
                        e += 1


                elif p1 != 0:
                    pos += p2 - 1


        if is_1:
            return count_mul
        
        return variables['h']
            
        
    variables = {}
    
    # print "Parte 1: " + str(run_instructions(variables, True))

    variables = {'a': 1}

    print "Parte 2: " + str(run_instructions(variables, False))