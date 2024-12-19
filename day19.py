from functools import cache

with open("input.txt", "r") as f:
    first, second = f.read().split('\n\n')
    patterns = first.split(', ')
    designs = second.splitlines()

@cache
def possible(design):
    if design == "": return 1
    ways = 0
    for pattern in patterns:
        if len(design) < len(pattern): continue
        if design.startswith(pattern): 
            ways += possible(design[len(pattern):])
    return ways

part1 = 0
part2 = 0
for design in designs:
    t = possible(design)
    if t:
        part1 += 1
        part2 += t
print(part1, part2, sep='\n')