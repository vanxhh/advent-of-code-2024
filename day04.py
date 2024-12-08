with open("input.txt", "r") as f:
    grid = f.read().splitlines()

def check(r, c, x, y, index): 
    flag = True
    str = 'XMAS'
    
    for i in range(1, 4):
        nx, ny = r + (i * x), c + (i * y)
        if nx not in range(0, len(grid)) or ny not in range(0, len(grid[0])):
            flag = False
            break
        if grid[nx][ny] != str[index + i]:
            flag = False
            break

    return flag

def part1():
    count = 0
    coords = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'X':
                for x, y in coords:
                    count += 1 if check(r, c, x, y, 0) else 0 

    print(count)

def part2():
    count = 0
    edgeList = [['M', 'M', 'S', 'S'], ['M', 'S', 'M', 'S'], ['S', 'M', 'S', 'M'], ['S', 'S', 'M', 'M']]
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if grid[r][c] != 'A':
                continue
            edges = [grid[r - 1][c - 1], grid[r - 1][c + 1], grid[r + 1][c - 1], grid[r + 1][c + 1]]
            count += 1 if edges in edgeList else 0

    print(count)

part1()
part2()