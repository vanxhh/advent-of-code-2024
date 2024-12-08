import re

with open("input.txt", "r") as f:
    text = f.read()

def part1():
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)
    sum = 0
    
    for match in matches:
        a, b = map(int, match[4:-1].split(','))
        sum += a * b
    
    print(sum)

def part2():
    do = True
    matches = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", text)
    sum = 0
    
    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        elif do:
            a, b = map(int, match[4:-1].split(','))
            sum += a * b
    
    print(sum)

part1()
part2()