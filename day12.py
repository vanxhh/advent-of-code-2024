from collections import deque

with open("input.txt", "r") as f:
    grid = f.read().splitlines()


def inRange(coordinates):
    x, y = coordinates
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

seen = set()
regions = []
index = 0
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if (x, y) in seen: continue
        seen.add((x, y))
        regions.append([(x, y)])
        q = deque([(x, y)])
        while len(q) > 0:
            r, c = q.popleft()
            for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
                if not inRange((nr, nc)): continue
                if (nr, nc) in seen: continue
                if grid[nr][nc] != grid[r][c]: continue
                seen.add((nr, nc))
                q.append((nr, nc))
                regions[index].append((nr, nc))
        index += 1

def findPerimeter(region):
    perimeter = 0
    for r, c in region:
        perimeter += 4
        for nr, nc in [(r - 1, c), (r, c + 1), (r + 1, c), (r, c - 1)]:
            if (nr, nc) in region:
                perimeter -= 1
    return perimeter

def part1():
    price = 0
    for region in regions:
        perimeter = findPerimeter(region)
        price += len(region) * perimeter
    print(price)

part1()