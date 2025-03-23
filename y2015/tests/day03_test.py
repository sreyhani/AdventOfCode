from solutions.day03 import solve_part1, solve_part2

def test_1():
    assert solve_part1('>') == 2
    assert solve_part1('^>v<') == 4
    assert solve_part1('^v^v^v^v^v') == 2
    
    
def test_2():
    assert solve_part2('^v') == 3
    assert solve_part2('^>v<') == 3
    assert solve_part2('^v^v^v^v^v') == 11