with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    reports = []
    for line in lines:
        reports.append([int(item) for item in line.split(' ')])

def part1():
    safeCount = 0

    for report in reports:
        n = len(report)
        flag = True
        prev = 1

        for i in range(0, n - 1):
            diff = report[i + 1] - report[i]

            if diff == 0 or abs(diff) > 3 or (i != 0 and prev * diff < 0):
                flag = False
                break

            prev = diff

        if flag:
            safeCount += 1

    print(safeCount)

def part2():
    safeCount = 0
    
    for report in reports:
        for index in range(len(report)):
            levels = report[:index] + report[index + 1:]
            diffs = [a - b for a, b in zip(levels, levels[1:])]
            if all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs):
                safeCount += 1
                break
    
    print(safeCount)

# part1()
part2()