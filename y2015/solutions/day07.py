gates = {}
gatesval = {}
def solve_part1(input: str):
    for line in input.splitlines():
        split = line.split()
        gates[split[-1]] = split
        
    return eval(gates['a'])

def solve_part2(input: str):
    gates.clear()
    gatesval.clear()
    for line in input.splitlines():
        split = line.split()
        gates[split[-1]] = split
    gates['b'] = '16076 -> b'.split()
    return eval(gates['a'])

def eval(assignment):
    if assignment[1] == '->':
        return eval_or_ret(assignment[0])
    if assignment[1] == 'AND':
        return eval_or_ret(assignment[0]) & eval_or_ret(assignment[2])
    if assignment[1] == 'OR':
        return eval_or_ret(assignment[0]) | eval_or_ret(assignment[2])
    if assignment[1] == 'LSHIFT':
        return eval_or_ret(assignment[0]) << eval_or_ret(assignment[2])
    if assignment[1] == 'RSHIFT':
        return eval_or_ret(assignment[0]) >> eval_or_ret(assignment[2])
    if assignment[0] == 'NOT':
        return 65535 - eval_or_ret(assignment[1])

def eval_or_ret(val: str):
    if val in gatesval:
        return gatesval[val]
    if val.isdigit():
        return int(val)
    else:
        ret = eval(gates[val])
        gatesval[val] = ret
        return ret
    
    
    