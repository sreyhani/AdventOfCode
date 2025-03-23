def solve_part1(input: str):
    area = 0
    for present in input.splitlines():
        dimensions = [int(i) for i in present.split('x')]
        area+=calc_area(dimensions[0], dimensions[1], dimensions[2])
    return area

def solve_part2(input):
    ribbon_len = 0
    for present in input.splitlines():
        dimensions = [int(i) for i in present.split('x')]
        ribbon_len+=calc_ribbon(dimensions[0], dimensions[1], dimensions[2])
    return ribbon_len


def calc_area(lenght: int, width: int, height: int):
    surfaces = [lenght*width, lenght*height, width*height]
    return 2*sum(surfaces) + min(surfaces)


def calc_ribbon(lenght: int, width: int, height: int):
    surfaces = [lenght+width, lenght+height, width+height]
    return 2*min(surfaces) + lenght*width*height
