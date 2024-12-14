import re

with open("input.txt", "r") as f:
    s_machines = f.read().split("\n\n")
    machines = []
    for s_machine in s_machines:
        machines.append(list(map(int, re.findall(r"\d+", s_machine))))

def part1():
    tokens = 0
    for machine in machines:
        ax, ay, bx, by, px, py = machine
        m = (px * by - py * bx) / (ax * by - ay* bx)
        n = (px - ax * m) / bx
        if m % 1 == n % 1 == 0 and m <= 100 and n <= 100:
            tokens += int(m * 3 + n)
    print(tokens)

def part2():
    tokens = 0
    for machine in machines:
        ax, ay, bx, by, px, py = machine
        px += 10000000000000
        py += 10000000000000
        m = (px * by - py * bx) / (ax * by - ay* bx)
        n = (px - ax * m) / bx
        if m % 1 == n % 1 == 0:
            tokens += int(m * 3 + n)
    print(tokens)

part1()
part2()