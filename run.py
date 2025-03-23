from importlib import import_module
from fetch_input import fetch_input

def main(year, day):
    fetch_input(year, day)
    input_file_name = f"y{year}/inputs/day{day:02}.txt"
    with open(input_file_name) as f:
        data = f.read().strip()

    module = import_module(f"y{year}.solutions.day{day:02}")
    print(f"Day {day}:")
    print("Part 1:", module.solve_part1(data))
    print("Part 2:", module.solve_part2(data))

if __name__ == "__main__":
    import sys 
    
    if len(sys.argv) < 3:
        print("Usage: python run.py <year> <day>")
        sys.exit(1)
    
    year = int(sys.argv[1])
    day = int(sys.argv[2])
    
    main(year, day)
