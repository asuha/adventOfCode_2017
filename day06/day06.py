input = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]

def redistribute_blocks(array):
    index = array.index(max(array))
    count = array[index]

    newArray = array
    newArray[index] = 0 

    while count > 0:
        index += 1
        index = index % len(array)

        newArray[index] += 1

        count -= 1
    
    return newArray

def parte1():
    myList = {}
    steps = 0
    array = input
    key = ''
    while True:
        array = redistribute_blocks(array)
        steps += 1

        string = ''.join(str(e) for e in array)

        if string in myList:        
            key = string
            break
        else:
            myList[string] = True
        
    result = {}
    result['steps'] = steps
    result['key'] = key
    return result

def parte2(key): 
    round1 = round2 = None
    turn = 0
    array = input
    while True:
        array = redistribute_blocks(array)
        turn += 1

        string = ''.join(str(e) for e in array)

        if string == key:        
            if round1 == None:
                round1 = turn
            else:
                round2 = turn
                break
    return round2 - round1

result = parte1()
print('Parte 1: ' + str(result.pop('steps')))
print('Parte 2: ' + str(parte2(result.pop('key'))))