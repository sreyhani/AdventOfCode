from solutions.day08 import solve_part1, solve_part2

def test_1():
    assert solve_part1('"aaa"') == 2
    assert solve_part1(r'"a\"aa"') == 3
    assert solve_part1(r'"a\\\""') == 4
    assert solve_part1(r'"a\\aa"') == 3
    assert solve_part1(r'"a\xaa"') == 5
    assert solve_part1(r'"a\\xaa"') == 3

def test_2():
    assert solve_part2('"aaa"') == 4
    assert solve_part2(r'"aa\"a"') == 6
    assert solve_part2(r'"\x27"') == 5


