
def solve_part1(input: str):
    sues = []
    for suetxt in input.splitlines():
        suetxt+=','
        splitted = suetxt.split()
        sue_num = int(splitted[1][:-1])
        splitted = splitted[2:]
        sue = {'num':sue_num}
        for i in range(3):
            field_name = splitted[i*2][:-1]
            field_val = int(splitted[i*2+1][:-1])
            sue[field_name] = field_val
            sues.append(sue)

    descriptions = ['children: 3', 'cats: 7', 'samoyeds: 2', 'pomeranians: 3', 'akitas: 0', 'vizslas: 0', 'goldfish: 5', 'trees: 3', 'cars: 2', 'perfumes: 1']
    for desc in descriptions:
        field, num = desc.split()
        num = int(num)
        field=field[:-1]
        new_sues = []
        for sue in sues:
            if field not in sue.keys():
                new_sues.append(sue)
            elif sue[field] == num:
                new_sues.append(sue)

        sues = new_sues
    return sues[0]['num']

def solve_part2(input: str):
    sues = []
    for suetxt in input.splitlines():
        suetxt+=','
        splitted = suetxt.split()
        sue_num = int(splitted[1][:-1])
        splitted = splitted[2:]
        sue = {'num':sue_num}
        for i in range(3):
            field_name = splitted[i*2][:-1]
            field_val = int(splitted[i*2+1][:-1])
            sue[field_name] = field_val
            sues.append(sue)

    descriptions = ['children: 3', 'cats: 7', 'samoyeds: 2', 'pomeranians: 3', 'akitas: 0', 'vizslas: 0', 'goldfish: 5', 'trees: 3', 'cars: 2', 'perfumes: 1']
    for desc in descriptions:
        field, num = desc.split()
        num = int(num)
        field=field[:-1]
        new_sues = []
        for sue in sues:
            if field not in sue.keys():
                new_sues.append(sue)
            elif field in ['cats', 'trees']:
                if sue[field] > num:
                    new_sues.append(sue)
            elif field in ['goldfish', 'pomeranians']:
                if sue[field] < num:
                    new_sues.append(sue)
            elif sue[field] == num:
                new_sues.append(sue)

        sues = new_sues
    return sues[0]['num']