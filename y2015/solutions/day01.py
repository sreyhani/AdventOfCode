def solve_part1(input):
    floor = 0
    for i in input:
        if i == "(":
            floor+=1
        elif i == ")":
            floor-=1
    return floor


def solve_part2(input):
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
