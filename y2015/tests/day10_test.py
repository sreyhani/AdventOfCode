from solutions.day10 import solve_part1, solve_part2, mutate

def test_mutate():
    assert mutate("1") == "11"
    assert mutate("11") == "21"
    assert mutate("21") == "1211"
    assert mutate("1211") == "111221"
    assert mutate("111221") == "312211"

