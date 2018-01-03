with open('./input.txt', 'r') as inputFile:
    input = inputFile.read()

    def parse_string_in_matriz (matrix_stringfy):
        lines = input.split('\n')
        matriz = []

        for l in lines:
            column = l.split("\t")
            matriz.append(column)

        return matriz
            
    def soma_maior_menor (array):
        a = int(array[0])
        b = int(array[0])
        for v in array:
            v = int(v)
            if v < a:
                a = v
            if v > b:
                b = v
        return b - a

    def retorna_divisao_even (array):
        a = int(array[0])
        b = int(array[0])
        for i, v in enumerate(array):
            for j, v1 in enumerate(array):
                if i != j:
                    v = int(v)
                    v1 = int(v1)
                    if v % v1 == 0:
                        return v / v1 

    inputMatriz = parse_string_in_matriz(input)

    checksum = 0
    evenDivision = 0

    for i in inputMatriz:
        checksum = checksum + soma_maior_menor(i)
        evenDivision = evenDivision + retorna_divisao_even(i)

    print('Parte 1: ' + str(checksum))
    print('Parte 2: ' + str(int(evenDivision)))