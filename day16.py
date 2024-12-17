import heapq

with open("input.txt", "r") as f:
    grid = [list(line) for line in f.read().splitlines()]

for SX in range(len(grid)):
    for SY in range(len(grid[0])):
        if grid[SX][SY] == 'S': break
    else: continue
    break

def part1():
    hq = [(0, SX, SY, 0, 1)]
    seen = {(SX, SY, 0, 1)}
    while hq:
        cost, cx, cy, dx, dy = heapq.heappop(hq)
        seen.add((cx, cy, dx, dy))
        if grid[cx][cy] == 'E':
            print(cost)
            break
        for n_cost, nx, ny, ndx, ndy in [(cost + 1, cx + dx, cy + dy, dx, dy), (cost + 1000, cx, cy, dy, -dx), (cost + 1000, cx, cy, -dy, dx)]:
            if grid[nx][ny] == '#': continue
            if (nx, ny, ndx, ndy) in seen: continue
            heapq.heappush(hq, (n_cost, nx, ny, ndx, ndy))
part1()