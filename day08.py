with open("input.txt", "r") as f:
    grid = f.read().splitlines()
    map = {}
    for x, row in enumerate(grid):
        for y, ch in enumerate(row):
            if ch != '.':
                if ch not in map:
                    map[ch] = []
                map[ch].append((x, y))

def inRange(node1):
    return 0 <= node1[0] < len(grid) and 0 <= node1[1] < len(grid[0])

def part1():
    antinodes = set()

    for frequency in map.keys():
        for i in range(len(map[frequency])):
            for j in range(i + 1, len(map[frequency])):
                n1, n2 = map[frequency][i], map[frequency][j]
                an1 = (2 * n1[0] - n2[0], 2 * n1[1] - n2[1])
                an2 = (2 * n2[0] - n1[0], 2 * n2[1] - n1[1])
                if inRange(an1): antinodes.add(an1)
                if inRange(an2): antinodes.add(an2)

    print(len(antinodes))

def part2():
    antinodes = set()

    for frequency in map:
        for i in range(len(map[frequency])):
            for j in range(len(map[frequency])):
                if i == j: continue
                n1, n2 = map[frequency][i], map[frequency][j]
                r1, c1 = n1
                r2, c2 = n2
                r, c = r1, c1
                dr, dc = r2 - r1, c2 - c1
                while inRange((r, c)):
                    antinodes.add((r, c))
                    r += dr
                    c += dc

    print(len(antinodes))

part1()
part2()