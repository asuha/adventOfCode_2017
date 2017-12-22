def generator_A():
    gen_a = 16807
    divider = 2147483647
    A = 883
    while True:
        A = (A * gen_a) % divider
        if A % 4 == 0:
            yield A

def generator_B():
    gen_b = 48271
    divider = 2147483647
    B = 879
    while True:
        B = (B * gen_b) % divider
        if B % 8 == 0:
            yield B

def bitway_comparition(a, b):
    mask = 0b00000000000000001111111111111111

    vB = a & mask
    vA = b & mask

    if vB^vA == 0:
        return True
    
    return False

def parte2():
    GA = generator_A()
    GB = generator_B()
    count = match = 0
    while count < 5000000:
        count += 1
        if bitway_comparition(GA.next(), GB.next()):
            match += 1
        
        if count % 10000 == 0:
            print count
    return match

print(parte2())

