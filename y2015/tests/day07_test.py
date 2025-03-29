from solutions.day07 import solve_part1

def test_1():
    assert solve_part1('10 -> a') == 10
    assert solve_part1('123 -> x\n456 -> y\nx AND y -> a') == 72
    assert solve_part1('123 -> x\n456 -> y\nx OR y -> a') == 507
    assert solve_part1('123 -> x\n456 -> y\nx LSHIFT 2 -> a') == 492
    assert solve_part1('123 -> x\n456 -> y\ny RSHIFT 2 -> a') == 114
    assert solve_part1('123 -> x\n456 -> y\nNOT x -> a') == 65412
