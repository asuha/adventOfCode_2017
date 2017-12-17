input = 316

def parte1(input):
    buffer = [0]
    curPos = 0
    count = 0
    while count < 2017:
        count += 1

        steps = (curPos + input) % len(buffer)

        p1 = buffer[:steps+1]
        p1.append(count)
        buffer = p1 + buffer[steps+1:]
        curPos = buffer.index(count)

    return str(buffer[curPos + 1])

def parte2(input):
    curPos = 0
    count = 0
    next_value = None
    while count < 50000000:
        count += 1

        pos = (curPos + input) % (count)
        
        if pos == 0:
            next_value = count

        curPos = pos + 1

    return str(next_value)

print("Parte 1: " + parte1(input))
print("Parte 2: " + parte2(input))


