from collections import deque

with open("input.txt", "r") as f:
    grid = [list(map(int, line.strip())) for line in f.read().splitlines()]
    zeroes = [(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 0]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def inRange(coordinates):
    x, y = coordinates
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def findScore(zero):
    queue = deque([zero])
    seen = {zero}
    score = 0
    
    while len(queue) > 0:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in seen: continue
            if not inRange((nr, nc)): continue
            if grid[nr][nc] != grid[r][c] + 1: continue
            
            seen.add((nr, nc))
            if grid[nr][nc] == 9:
                score += 1
            else:
                queue.append((nr, nc))
    
    return score

def findRating(coordinates, height):
    x, y = coordinates
    if height == 9: return 1

    rating = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if inRange((nx, ny)) and grid[nx][ny] == height + 1:
            rating += findRating((nx, ny), height + 1)
    return rating

def part1():
    score = 0
    for zero in zeroes:
        score += findScore(zero)
    print(score)

def part2():
    rating = 0
    for zero in zeroes:
        rating += findRating(zero, 0)
    print(rating)

part1()
part2()