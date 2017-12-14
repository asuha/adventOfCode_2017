with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day1/input.txt', 'r') as inputFile:
    input = inputFile.read()


    def part1():
        new_input = input[len(input) - 1] + input
        soma = 0
        i = 1

        for c in input[1:]:
            if c == input[i - 1]:
                soma += int(c)
            i = i + 1
        print('Parte 1: ' + str(soma))

    def part2():
        jump = int(len(input) / 2)

        soma = 0
        i = 0
        for c in input:
            if input[(i + jump) % len(input)] == c:
                soma += int(c)
            i = i + 1

        print('Parte 2: ' + str(soma))

    part1()
    part2()


