with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    results = []
    values = []
    for line in lines:
        results.append(int(line.split(":")[0]))
        values.append(list(map(int, line.split(":")[1].split(" ")[1:])))

def helper1(valueList, valIndex, calcValue):
    if -valIndex > len(valueList):
        if calcValue == 0:
            return True
        return False
    if calcValue > 0 and helper1(valueList, valIndex - 1, calcValue - valueList[valIndex]):
        return True
    if calcValue > 0 and helper1(valueList, valIndex - 1, calcValue / valueList[valIndex]):
        return True
    return False

def part1():
    sum = 0
    for i in range(len(results)):
        sum += results[i] if helper1(values[i], -1, results[i]) else 0
    print(sum)

def helper2(valueList, calcValue):
    if len(valueList) == 1:
        return calcValue == valueList[-1]
    if calcValue > valueList[-1] and helper2(valueList[:-1], calcValue - valueList[-1]):
        return True
    if calcValue % valueList[-1] == 0 and helper2(valueList[:-1], calcValue // valueList[-1]):
        return True
    
    sCalcValue = str(calcValue)
    last = str(valueList[-1])
    if sCalcValue.endswith(last) and len(sCalcValue) > len(last) and helper2(valueList[:-1], int(sCalcValue[:-len(last)])):
        return True
    
    return False

def part2():
    sum = 0
    for i in range(len(results)):
        if helper2(values[i], results[i]):
            sum += results[i]
    print(sum)

part1()
part2()