with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    a = []
    b = []
    for line in lines:
        x, y = line.split('   ')
        a.append(int(x))
        b.append(int(y))

def part1():
    ans = 0
    for i in range(len(a)):
        ans += abs(a[i] - b[i])
    print(ans)

def part2():
    ans = 0
    for i in range(len(a)):
        ans += a[i] * b.count(a[i])
    print(ans)

a = sorted(a)
b = sorted(b)

part1()
part2()