from solutions.day01 import solv, solv2
def test_1():
    assert solv('(())') == 0
    assert solv('()()') == 0
    assert solv('(((') == 3
    assert solv('(()(()(') == 3
    assert solv('))(((((') == 3
    assert solv('())') == -1
    assert solv(')))') == -3
    assert solv(')())())') == -3
    
    
def test_2():
    assert solv2('())') == 3
    assert solv2(')()') == 1
    assert solv2(')))') == 1
    assert solv2('()())') == 5