from solutions.day02 import solve_part1, solve_part2
def test_1():
    assert solve_part1('1x1x1') == 7
    assert solve_part1('2x3x4') == 58
    assert solve_part1('1x1x10') == 43
    assert solve_part1('1x1x10\n1x1x1') == 43 + 7
    
def test_2():
    assert solve_part2('1x1x1') == 5
    assert solve_part2('2x3x4') == 34
    assert solve_part2('1x1x10') == 14
    assert solve_part2('1x1x10\n1x1x1') == 14 + 5
