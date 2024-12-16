import re

with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    robots = []
    for line in lines:
        robots.append(list(map(int, re.findall(r'-?\d+', line))))

width = 101
height = 103

def part1():
    res_positions = []

    for px, py, vx, vy in robots:
        nx, ny = (px + vx * 100) % width, (py + vy * 100) % height
        res_positions.append((nx, ny))
    
    quadrants = [0] * 4
    horizontal_middle = (width - 1) // 2
    vertical_middle = (height - 1) // 2
    
    for px, py in res_positions:
        if px == horizontal_middle or py == vertical_middle: continue
        if px < horizontal_middle:
            if py < vertical_middle:
                quadrants[0] += 1
            else:
                quadrants[1] += 1
        else:
            if py < vertical_middle:
                quadrants[2] += 1
            else:
                quadrants[3] += 1
    
    product = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    print(product)

def part2():
    for second in range(10000):
        res = [["."] * width for _ in range(height)]
        
        for px, py, vx, vy in robots:
            nx, ny = (px + vx * second) % width, (py + vy * second) % height
            res[ny][nx] = '#'
        
        for line in res:
            if '###########' in "".join(line):
                print(second)
                return
    return

part1()
part2()