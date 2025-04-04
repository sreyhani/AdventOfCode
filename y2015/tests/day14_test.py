from solutions.day14 import solve_part1, solve_part2, calc_distance, calc_scores


def test_calc_distance():
    assert calc_distance(10, 10, 2, 8) == 20
    assert calc_distance(10, 10, 5, 8) == 50
    assert calc_distance(10, 10, 5, 1) == 90
    assert calc_distance(1000, 14, 10, 127) == 1120
    assert calc_distance(1000, 16, 11, 162) == 1056


def test_scores():
    assert list(calc_scores({(14, 10, 127): 0, (16, 11, 162): 0},
                       1000).values()) == [312, 689]
