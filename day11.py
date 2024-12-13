from functools import cache

with open("input.txt", "r") as f:
    stones = list(map(int, f.read().split(' ')))

def part1():
    curr_stones = stones
    for _ in range(25):
        stoneList = []
        for stone in curr_stones:
            if stone == 0:
                stoneList.append(1)
                continue
            s_stone = str(stone)
            if len(s_stone) % 2 == 0:
                stoneList.append(int(s_stone[:len(s_stone) // 2]))
                stoneList.append(int(s_stone[len(s_stone) // 2:]))
            else:
                stoneList.append(int(stone) * 2024)
        curr_stones = stoneList
    print(len(curr_stones))

@cache
def recur(stone, blinks):
    if blinks == 0:
        return 1
    if stone == 0:
        return recur(1, blinks - 1)
    
    s_stone = str(stone)
    length = len(s_stone)
    if length % 2 == 0:
        return recur(int(s_stone[:length // 2]), blinks - 1) + recur(int(s_stone[length // 2:]), blinks - 1)
    return recur(int(s_stone) * 2024, blinks - 1)

def part2():
    sum = 0
    for stone in stones:
        sum += recur(stone, 75)
    print(sum)

part1()
part2()