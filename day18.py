from collections import deque

with open("input.txt", "r") as f:
    coords = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]

SIZE = 71

def inRange(x, y):
    return 0 <= x < SIZE and 0 <= y < SIZE

def steps(bytes):
    grid = [['.'] * SIZE for _ in range(SIZE)]
    for x, y in coords[:bytes]:
        grid[y][x] = '#'
    q = deque([(0, 0, 0)])
    seen = {(0, 0)}
    while q:
        steps, cx, cy = q.popleft()
        for nx, ny in [(cx, cy - 1), (cx + 1, cy), (cx, cy + 1), (cx - 1, cy)]:
            if not inRange(nx, ny): continue
            if grid[nx][ny] == '#': continue
            if (nx, ny) in seen: continue
            if nx == ny == 70:
                return steps + 1
            seen.add((nx, ny))
            q.append((steps + 1, nx, ny))
    return 0

def part1():
    print(steps(1024))

def part2():
    # for i in range(1024, len(coords)):
    #     if steps(i) == 0:
    #         print(*coords[i - 1], sep=',')
    #         break
    l = 1024
    h = len(coords) - 1
    while l < h:
        mid = (l + h) // 2
        if steps(mid + 1):
            l = mid + 1
        else:
            h = mid
    print(l, *coords[l], sep=',')

part1()
part2()