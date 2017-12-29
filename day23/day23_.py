b = 57*100
b += 100000
c = b + 17000
g = 0
h = 0

while True:
    f = 1
    d = g = 2
    while g != 0:
        e = 2
        if b % d == 0:
            f = 0
            break
        d += 1
        g = d
        g = g - b
    if f == 0:
        h += 1
    g = b
    g = g - c
    if g == 0:
        break
    b += 17

print h