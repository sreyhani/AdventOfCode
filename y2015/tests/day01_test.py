from solutions.day01 import solve_part1, solve_part2
def test_1():
    assert solve_part1('(())') == 0
    assert solve_part1('()()') == 0
    assert solve_part1('(((') == 3
    assert solve_part1('(()(()(') == 3
    assert solve_part1('))(((((') == 3
    assert solve_part1('())') == -1
    assert solve_part1(')))') == -3
    assert solve_part1(')())())') == -3
    
    
def test_2():
    assert solve_part2('())') == 3
    assert solve_part2(')()') == 1
    assert solve_part2(')))') == 1
    assert solve_part2('()())') == 5