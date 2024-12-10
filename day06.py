with open("input.txt", "r") as f:
    grid = f.read().splitlines()

def part1():
    dx = -1
    dy = 0
    map = set()

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '^':
                break
        else:
            continue
        break

    while True:
        map.add((x, y))
        if x + dx < 0 or x + dx >= len(grid) or y + dy < 0 or y + dy >= len(grid[0]):
            break
        if grid[x + dx][y + dy] == '#':
            dx, dy = dy, -dx
        x, y = x + dx, y + dy

    print(len(map))

part1()