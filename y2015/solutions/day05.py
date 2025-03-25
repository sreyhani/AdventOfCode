def solve_part1(input: str):
    count = 0
    for line in input.splitlines():
        if is_nice(line):
            count += 1
    return count

def is_nice(line: str):
    vowels = ['a','e','i','o','u']
    if sum([line.count(vowel) for vowel in vowels]) < 3:
        return False
    if not contains_double(line):
        return False
    
    banned_strings = ['ab', 'cd', 'pq', 'xy']
    if sum([line.count(banned_string) for banned_string in banned_strings]) > 0:
        return False
    
    return True

def contains_double(line: str):
    i = 0
    while i < len(line) - 1:
        if line[i] == line[i+1]:
            return True
        i+=1
    return False
        
def solve_part2(input: str):
    count = 0
    for line in input.splitlines():
        if is_nice2(line):
            count += 1
    return count

def is_nice2(line: str):
    if not contains_double_pair(line):
        return False
    if not contains_repeating_between(line):
        return False
    return True

def contains_double_pair(line: str):
    i = 0
    while i < len(line) - 2:
        if line[i+2:].count(line[i:i+2]) > 0:
            return True
        i+=1
    return False

    
def contains_repeating_between(line: str):
    i = 0
    while i < len(line) - 2:
        if line[i] == line[i+2]:
            return True
        i+=1
    return False
