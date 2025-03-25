from solutions.day06 import solve_part1, solve_part2

def test_1():
    assert solve_part1('turn on 0,0 through 999,999') == 1000 * 1000
    assert solve_part1('toggle 0,0 through 999,0') == 1000
    assert solve_part1('turn on 0,0 through 999,999\nturn off 499,499 through 500,500') ==  1000 * 1000 - 4


def test_2():
    assert solve_part2('turn on 0,0 through 999,999') == 1000 * 1000
    assert solve_part2('toggle 0,0 through 999,0') == 2000
    assert solve_part2('turn on 0,0 through 999,999\nturn off 499,499 through 500,500') ==  1000 * 1000 - 4
    assert solve_part2('turn off 499,499 through 500,500\nturn on 0,0 through 999,999') ==  1000 * 1000
