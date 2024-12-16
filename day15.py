from collections import deque

with open("input.txt", "r") as f:
    first, second = f.read().split('\n\n')
    moves = second.replace('\n', '')

movements = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

def part1():
    grid = [list(line) for line in first.splitlines()]
    for x in range(len(grid)):
        for y in range(len(grid[0])) :
            if grid[x][y] == '@': break
        else: continue
        break
    
    for move in moves:
        dx, dy = movements[move]
        track_list = [(x, y)]
        nx, ny = x, y
        wallFound = False
        while True:
            nx += dx
            ny += dy
            if grid[nx][ny] == '#':
                wallFound = True
                break
            elif grid[nx][ny] == 'O':
                track_list.append((nx, ny))
            elif grid[nx][ny] == '.':
                break
        if wallFound: continue
        grid[x][y] = '.'
        grid[x + dx][y + dy] = '@'
        for bx, by in track_list[1:]:
            grid[bx + dx][by + dy] = 'O'
        x += dx
        y += dy
    
    sum = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                sum += r * 100 + c
    print(sum)

def part2():
    grid = [list(line) for line in first.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.').splitlines()]
    for x in range(len(grid)):
        for y in range(len(grid[0])) :
            if grid[x][y] == '@': break
        else: continue
        break
    
    for move in moves:
        dx, dy = movements[move]
        track_list = [(x, y)]
        wallFound = False
        for cx, cy in track_list:
            nx = cx + dx
            ny = cy + dy
            if (nx, ny) in track_list: continue
            if grid[nx][ny] == '#':
                wallFound = True
                break
            elif grid[nx][ny] == '[':
                track_list.append((nx, ny))
                track_list.append((nx, ny + 1))
            elif grid[nx][ny] == ']':
                track_list.append((nx, ny))
                track_list.append((nx, ny - 1))
        
        if wallFound: continue
        
        track_list_copy = [list(line) for line in grid]
        grid[x][y] = '.'
        grid[x + dx][y + dy] = '@'
        for bx, by in track_list[1:]:
            grid[bx][by] = '.'
        for bx, by in track_list[1:]:
            grid[bx + dx][by + dy] = track_list_copy[bx][by]
        x += dx
        y += dy
    
    sum = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '[':
                sum += r * 100 + c
    print(sum)

part1()
part2()