def solve_part1(input: str):
    count = 0
    for line in input.splitlines():
        count += 2
        line = line[1:-1]
        count+=line.count('\\\\')
        line = line.replace(r'\\','')
        count+=line.count('\\"')
        count+=(line.count('\\x'))*3
    return count

def solve_part2(input: str):
    count = 0
    for line in input.splitlines():
        count+=2
        count+=line.count('"')
        count+=line.count('\\')
    return count