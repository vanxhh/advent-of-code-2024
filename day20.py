from collections import deque

with open("input.txt", "r") as f:
    grid = [list(line) for line in f.read().splitlines()]

for SX in range(len(grid)):
    for SY in range(len(grid[0])):
        if grid[SX][SY] == 'S': break
    else: continue
    break

def inRange(x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

q = deque([(SX, SY)])
dists = [[-1] * len(grid[0]) for _ in range(len(grid))]
dists[SX][SY] = 0
while q:
    cx, cy = q.popleft()
    for nx, ny in [(cx, cy - 1), (cx + 1, cy), (cx, cy + 1), (cx - 1, cy)]:
        if not inRange(nx, ny): continue
        if grid[nx][ny] == '#': continue
        if dists[nx][ny] != -1: continue
        dists[nx][ny] = dists[cx][cy] + 1
        q.append((nx, ny))

def part1():
    res = 0
    for x in range(len(dists)):
        for y in range(len(dists[0])):
            if dists[x][y] == -1: continue
            for jx, jy in {(x, y - 2), (x + 2, y), (x, y + 2), (x - 2, y)}:
                if not inRange(jx, jy): continue
                if dists[jx][jy] - dists[x][y] > 101: res += 1
    print(res)

def part2():
    res = 0
    for x in range(len(dists)):
        for y in range(len(dists[0])):
            if dists[x][y] == -1: continue
            for radius in range(2, 21):
                for dx in range(radius + 1):
                    dy = radius - dx
                    for jx, jy in {(x + dx, y + dy), (x + dx, y - dy), (x - dx, y - dy), (x - dx, y + dy)}:
                        if not inRange(jx, jy): continue
                        if dists[jx][jy] - dists[x][y] > (100 + radius - 1): res += 1
    print(res)

part1()
part2()