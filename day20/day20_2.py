import re

with open('./input.txt', 'r') as inputFile:
    input = inputFile.read().split('\n')

    p = list()
    v = list()
    a = list()

    for i in input:
        regex = re.match(r"p=<(.*)>, v=<(.*)>, a=<(.*)>", i)

        p.append([int(z) for z in regex.group(1).split(',')])
        v.append([int(x) for x in regex.group(2).split(',')])
        a.append([int(y) for y in regex.group(3).split(',')])

    def generate(p, v, a):
        p0 = p
        v0 = v
        a0 = a

        while True:
            v0 = v0 + a0
            p0 += v0
            yield [p0, v0, a0]

    def validate_conflict(val_1, val_2, prev_diff):
        diff = 0
        
        val_a = val_1.next()
        val_b = val_2.next()
            
        p1 = val_a[0]
        p2 = val_b[0]
        v1 = val_a[1]
        v2 = val_b[1]
        a1 = val_a[2]
        a2 = val_b[2]

        diff = abs(p1 - p2)

        if diff == 0:
            return 0
        elif ((v1 >= 0 and a1 < 0) or (v1 <= 0 and a1 > 0)) or ((v2 >= 0 and a2 < 0) or (v2 <= 0 and a2 > 0)):
            return diff
        elif (a1 > a2 and v1 < v2) or (a2 > a1 and v2 < v1):
            return diff
        elif a1 == a2 and (v1 + a1) == (v2 + a2):
            return -1
        elif prev_diff < diff:
            return -1

        return diff
        
    conflict = set()
    for index, pos in enumerate(p):
        next_v = index + 1
        while next_v < len(p):

            _x1 = generate(p[index][0], v[index][0], a[index][0])
            _x2 = generate(p[next_v][0], v[next_v][0], a[next_v][0])
            _y1 = generate(p[index][1], v[index][1], a[index][1])
            _y2 = generate(p[next_v][1], v[next_v][1], a[next_v][1])
            _z1 = generate(p[index][2], v[index][2], a[index][2])
            _z2 = generate(p[next_v][2], v[next_v][2], a[next_v][2])
            
            prev_diff_x = abs(p[index][0] - p[next_v][0])
            prev_diff_y = abs(p[index][1] - p[next_v][1])
            prev_diff_z = abs(p[index][2] - p[next_v][2])

            if prev_diff_x == 0 and prev_diff_y == 0 and prev_diff_z == 0:
                conflict.add(index)
                conflict.add(next_v)
                next_v += 1
                break
            
            while True:

                posx = validate_conflict(_x1, _x2, prev_diff_x)
                if posx < 0:
                    break
                
                posy = validate_conflict(_y1, _y2, prev_diff_y)
                if posy < 0:
                    break
                
                posz = validate_conflict(_z1, _z2, prev_diff_z)
                if posz < 0:
                    break

                if posx == 0 and posy == 0 and posz == 0:
                    conflict.add(index)
                    conflict.add(next_v)
                    break

                prev_diff_x = posx
                prev_diff_y = posy
                prev_diff_z = posz

            next_v += 1

    print("Parte 2: " + str(len(p) - len(conflict)))