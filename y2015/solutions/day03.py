def solve_part1(input: str):
    houses: dict = {}
    point: tuple = (0, 0)
    houses[point] = houses.get(point, 0) + 1
    
    for dir in input:
        point = update_point(point, dir)
        houses[point] = houses.get(point, 0) + 1
        
    return len(houses.keys())

def solve_part2(input: str):
    houses: dict = {}
    santa_point: tuple = (0, 0)
    robot_point: tuple = (0, 0)
    # point: tuple = (0, 0)
    houses[santa_point] = houses.get(santa_point, 0) + 1
    it = iter(input)
    
    for dir in it:
        santa_dir = dir
        robot_dir = next(it)
        
        santa_point = update_point(santa_point, santa_dir)
        robot_point = update_point(robot_point, robot_dir)
        houses[santa_point] = houses.get(santa_point, 0) + 1
        houses[robot_point] = houses.get(robot_point, 0) + 1
        
    return len(houses.keys())

def update_point(point, dir):
    if dir == '>':
        return (point[0] + 1, point[1])
    if dir == '<':
        return (point[0] - 1, point[1])
    if dir == '^':
        return (point[0], point[1] + 1)
    if dir == 'v':
        return (point[0], point[1] - 1)