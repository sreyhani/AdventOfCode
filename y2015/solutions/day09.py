from copy import deepcopy
from math import inf


indicies = {
    "Faerun": 0, "Tristram":   1, "Tambi":  2, "Norrath": 3, "Snowdin":  4, "Straylight": 5, "AlphaCentauri": 6, "Arbre": 7}

# indicies = {"London": 0, "Dublin": 1, "Belfast": 2}
LEN = len(indicies)


def solve_part1(input: str):
    distances = [[inf for _ in range(LEN)] for _ in range(LEN)]
    for line in input.splitlines():
        (src, _, dest, _, distance) = line.split()
        distance = int(distance)
        distances[indicies[src]][indicies[dest]] = distance
        distances[indicies[dest]][indicies[src]] = distance
    for distance in distances:
        print(distance)

    original_dist = deepcopy(distances)
    for m in range(LEN - 2):
        
        print('--------------')
        for i in range(LEN):
            for j in range(LEN):
                cross = []
                for k in range(LEN):
                    cross.append(distances[i][k] + original_dist[k][j])
                print(f"m:{m} i:{i} j:{j}: cross:{cross}")
                distances[i][j] = min(cross)
                if i == j:
                    distances[i][j] = inf

        for distance in distances:
            print(distance)

    return min(sum(distances, []))


def solve_part2(input: str):
    return 0
