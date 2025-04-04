def solve_part1(input: str):
    distance = []
    for reindeer in input.splitlines():
        split = reindeer.split()
        distance.append(calc_distance(
            2503, int(split[3]), int(split[6]), int(split[13])))

    return max(distance)


def calc_distance(total_time: int, speed: int, travel_time: int, rest_time: int):
    total_travel_time = total_time//(travel_time+rest_time)*travel_time + min(
        total_time % (travel_time+rest_time), travel_time)
    return speed*total_travel_time


def solve_part2(input: str):
    reindeers = {}
    for reindeer in input.splitlines():
        split = reindeer.split()
        reindeers[(int(split[3]), int(split[6]), int(split[13]))] = 0

    calc_scores(reindeers, 2503)
    return max(reindeers.values())


def calc_scores(reindeers: dict, total_time: int):
    for i in range(1, total_time+1):
        travels = {}
        for reindeer in reindeers.keys():
            travels[reindeer] = calc_distance(i, *reindeer)
        furthest = max(travels.values())
        winners = [k for k,v in travels.items() if v == furthest]
        for winner in winners:
            reindeers[winner]+=1
    return reindeers
