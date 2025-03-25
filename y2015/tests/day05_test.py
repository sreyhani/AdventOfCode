from solutions.day05 import solve_part1, solve_part2

def test_1():
    assert solve_part1('ugknbfddgicrmopn') == 1
    assert solve_part1('aaa') == 1
    assert solve_part1('jchzalrnumimnmhp') == 0
    assert solve_part1('haegwjzuvuyypxyu') == 0
    assert solve_part1('dvszwmarrgswjxmb') == 0

def test_2():
    assert solve_part2('qjhvhtzxzqqjkmpb') == 1
    assert solve_part2('xxyxx') == 1
    assert solve_part2('uurcxstgmygtbstg') == 0
    assert solve_part2('ieodomkazucvgmuy') == 0

from solutions.day05 import contains_double, contains_double_pair

def test_contains_double():
    assert  contains_double('aa') == True
    assert  contains_double('ab') == False
    assert  contains_double('abcddefg') == True
    
def test_contains_double_pair():
    assert contains_double_pair('aabaa') == True
    assert contains_double_pair('aaba') == False
    assert contains_double_pair('aaa') == False
    assert contains_double_pair('aaaa') == True
    assert contains_double_pair('ajgcsaja') == True
    