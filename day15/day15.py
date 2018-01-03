gen_a = 16807
gen_b = 48271
divider = 2147483647
A = 883
B = 879

def bitway_comparition(a, b):
    mask = 0b00000000000000001111111111111111

    vB = a & mask
    vA = b & mask

    if vB^vA == 0:
        return True
    
    return False

def parte1(gen_a, gen_b, divider, A, B):
    count = match = 0
    while count < 40000000:
        count += 1
        
        A = (A * gen_a) % divider
        B = (B * gen_b) % divider

        if bitway_comparition(A, B):
            match += 1 
    return match

def isPair(value):
    mask = 0b00000000000000000000000000000001

    v = value & mask

    if v == 1:
        return False
    
    return True

def parte2(gen_a, gen_b, divider, A, B):
    count = match = 0
    stackA = list()
    stackB = list()
    while count < 5000000:
        
        
        A = (A * gen_a) % divider
        B = (B * gen_b) % divider

        bA = isPair(A) 
        bB = isPair(B)
        
        if bA:
            if A % 4 == 0:
                stackA.append(A) 
        if bB:
            if B % 8 == 0:
                stackB.append(B)

        if bA or bB:
            if len(stackA) > 0 and len(stackB) > 0:
                count += 1
                if count % 10000 == 0:
                    print(count)
                if bitway_comparition(stackA.pop(0), stackB.pop(0)):
                    match += 1
    return match
    
print 'Parte 1: ' + str(parte1(gen_a, gen_b, divider, A, B))
## Takes a life time
print('Parte 2: ' + str(parte2(gen_a, gen_b, divider, A, B)))