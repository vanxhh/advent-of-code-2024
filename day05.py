with open("input.txt", "r") as f:
    text = f.read().split("\n\n")
    orders, updates = [elem.splitlines() for elem in text]

orderDict = {}
updateList = []
incorrect = []

def read():
    for order in orders:
        a, b = map(int, order.split('|'))
        if a not in orderDict.keys():
            orderDict[a] = []
        orderDict[a].append(b)

    updateList[:] = [list(map(int, update.split(','))) for update in updates]

def part1():
    sum = 0
    
    for update in updateList:
        flag = True
        for i in range(len(update)):
            for num in update[i+1:]:
                if num in orderDict.keys() and update[i] in orderDict[num]:
                    flag = False
                    break
            if not flag:
                break
        if flag:
            sum += update[len(update) // 2]
        else:
            incorrect.append(update)
    
    print(sum)

def part2():
    sum = 0
    for update in incorrect:
        for i in range(len(update)):
            for num in range(i + 1, len(update)):
                if update[num] in orderDict.keys() and update[i] in orderDict[update[num]]:
                    update[num], update[i] = update[i], update[num]
        sum += update[len(update) // 2]
    print(sum)

read()
part1()
part2()