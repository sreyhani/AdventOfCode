import hashlib
def solve_part1(input: str):
    num = 0
    while True:
        hash = hashlib.md5((input + str(num)).encode()).hexdigest()
        if hash.startswith('00000'):
            break
        num+=1
    return num

def solve_part2(input: str):
    num = 0
    while True:
        hash = hashlib.md5((input + str(num)).encode()).hexdigest()
        if hash.startswith('000000'):
            break
        num+=1
    return num