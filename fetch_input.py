import os
import requests
from dotenv import load_dotenv

load_dotenv()

SESSION_COOKIE = os.getenv("SESSION_COOKIE")

def fetch_input(year, day):
    filename = f"y{year}/inputs/day{day:02}.txt" 
    if os.path.isfile(filename):
        return
    response = make_request(day, year)

    if response.status_code == 200:
        write_input(filename, response)
        print(f"✅ Input for Day {day} saved.")
    else:
        print("❌ Failed to fetch input.")

def write_input(filename, response):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename , "w") as f:
        f.write(response.text.strip())

def make_request(day, year):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": SESSION_COOKIE}
    response = requests.get(url, cookies=cookies)
    return response

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python fetch_input.py <year> <day>")
        sys.exit(1)
        
    year = int(sys.argv[1])
    day = int(sys.argv[2])
    
    fetch_input(year, day)
