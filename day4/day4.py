with open('/Users/juliorenner/Documents/git/adventOfCode_2017/day4//input.txt', 'r') as inputFile:

    input = inputFile.read()

    passphrases = input.split("\n")

    def parte1(passphrase):
        
        keys = passphrase.split(" ")

        dict = {}

        for key in keys:
            if key in dict:
                return False
            else:
                dict[key] = True
        
        return True

    def parte2(passphrase):
        
        keys = passphrase.split(" ")

        dict = {}

        for key in keys:
            word = ''.join(sorted(key))
            if word in dict:
                return False
            else:
                dict[word] = True
        
        return True

    count1 = 0
    count2 = 0
    for p in passphrases:
        if (parte1(p)):
            count1 += 1
        if (parte2(p)):
            count2 += 1

    print('Parte 1: ' + str(count1))
    print('Parte 2: ' + str(count2))