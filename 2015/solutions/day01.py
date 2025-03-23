def solv(input):
    floor = 0
    for i in input:
        if i == "(":
            floor+=1
        elif i == ")":
            floor-=1
    return floor


def solv2(input):
    floor = 0
    pos = 1
    for i in input:
        if i == "(":
            floor+=1
        elif i == ")":
            floor-=1
        if floor < 0:
            return pos
        pos+=1
    return floor

with open('inputs/01.txt') as f:
    input = f.read()
    print(solv(input))
    print(solv2(input))