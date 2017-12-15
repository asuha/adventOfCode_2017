# def check_binaries(bin_a, bin_b):
#     count = 1
#     for p in range(len(bin_a)-1, 16, -1):
#         if p >= len(bin_b):
#             return False

#         if int(bin_a[p]) == int(bin_b[p]):
#             count += 1
#         else:
#             count = 1
        
#         if count == 15:
#             return True
    
#     return False

# gen_a = 16807
# gen_b = 48271
# divider = 2147483647
# A = remainder_A = 65
# B = remainder_B = 8921

# count = match = 0

# while count < 40000000:
#     count += 1
    
#     A = (remainder_A * gen_a)
#     B = (remainder_B * gen_b)

#     remainder_A = A % divider
#     remainder_B = B % divider

#     bin_a = bin(remainder_A)[2:].zfill(32)
#     bin_b = bin(remainder_B)[2:].zfill(32)

#     if bitway_comparition(bin_a, bin_b):
#         match += 1 
    
#     if count % 10000 == 0:
#         print(count)

#######################

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

def parte2(gen_a, gen_b, divider, A, B):
    count = match = 0
    stackA = list()
    stackB = list()
    while count < 5000000:
        
        
        A = (A * gen_a) % divider
        B = (B * gen_b) % divider

        if A % 4 == 0:
            stackA.append(A)
        if B % 8 == 0:
            stackB.append(B)

        if len(stackA) > 0 and len(stackB) > 0:
            count += 1
            if count % 10000 == 0:
                print(count)
            if bitway_comparition(stackA.pop(0), stackB.pop(0)):
                match += 1
    return match
    
#print('Parte 1: ' + str(parte1(gen_a, gen_b, divider, A, B)))
print('Parte 2: ' + str(parte2(gen_a, gen_b, divider, A, B)))