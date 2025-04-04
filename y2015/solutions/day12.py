import json

def solve_part1(input: str):
    data = json.loads(input)
    sum=0
    sum+=add_up(data)
    return sum

def add_up(data):
    sum = 0
    if isinstance(data, list):
        for i in data:
            sum+=add_up(i)
    elif isinstance(data, int):
        return data
    elif isinstance(data, dict):
        for i in data.values():
            sum+=add_up(i)
    return sum

def solve_part2(input: str):
    data = json.loads(input)
    sum=0
    sum+=add_up2(data)
    return sum


def add_up2(data):
    sum = 0
    if isinstance(data, list):
        for i in data:
            sum+=add_up2(i)
    elif isinstance(data, int):
        return data
    elif isinstance(data, dict):
        for i in data.values():
            if i == "red":
                return 0
            sum+=add_up2(i)
    return sum