def solve_part1(input: str):
    for _ in range(40):
        input = mutate(input)
    return len(input)

def solve_part2(input: str):
    for _ in range(50):
        input = mutate(input)
    return len(input)

def mutate(input: str):
    mutated: str = ""

    count = 0
    i = 0
    j = 0
    while(i != len(input)):
        while(i != len(input) and input[i] == input[j]):
            count+=1
            i+=1
        mutated += str(count)
        mutated += input[j]
        j = i
        count=0
    return mutated
    #         if index == len(input):
    #             return str(count) + input[0] 
    # return str(count) + input[0] + mutate(input[index:])
    