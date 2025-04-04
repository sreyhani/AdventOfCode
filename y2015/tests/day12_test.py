from solutions.day12 import solve_part1, solve_part2

def test_sum():
    assert solve_part1("[1,2,3]") == 6
    assert solve_part1("[1,[2],3]") == 6
    assert solve_part1("[[[3]]]") == 3
    assert solve_part1('{"a":[-1,1]}') == 0

def test_sum2():
    assert solve_part2("[1,2,3]") == 6
    assert solve_part2('{"d":"red","e":[1,2,3,4],"f":5}') == 0
    assert solve_part2('[1,{"c":"red","b":2},3]') == 4
    assert solve_part2('[1,"red",5]') == 6
