def solve_part1(input: str):
    lights = [[False] * 1000 for i in range(1000)]
    for line in input.splitlines():
        split = line.split()
        if line.startswith("turn"):
            start = split[2]
            end = split[4]
        elif line.startswith("toggle"):
            start = split[1]
            end = split[3]
        
        start = [int(x) for x in start.split(',')]
        end = [int(x) for x in end.split(',')]
        
        i = start[0]
        j = start[1]
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if line.startswith("turn off"):
                    lights[i][j] = True
                if line.startswith("turn off"):
                    lights[i][j] = False
                elif line.startswith("turn on"):
                    lights[i][j] = True
                elif line.startswith("toggle"):
                    lights[i][j] = not lights[i][j]
    return sum([sum(l) for l in lights])


def solve_part2(input: str):
    lights = [[0] * 1000 for i in range(1000)]
    for line in input.splitlines():
        split = line.split()
        if line.startswith("turn"):
            start = split[2]
            end = split[4]
        elif line.startswith("toggle"):
            start = split[1]
            end = split[3]
        
        start = [int(x) for x in start.split(',')]
        end = [int(x) for x in end.split(',')]
        
        i = start[0]
        j = start[1]
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if line.startswith("turn off"):
                    lights[i][j] = max(lights[i][j] - 1, 0)
                elif line.startswith("turn on"):
                    lights[i][j] += 1
                elif line.startswith("toggle"):
                    lights[i][j] += 2
    return sum([sum(l) for l in lights])




