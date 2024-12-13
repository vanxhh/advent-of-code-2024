with open("input.txt", "r") as f:
    instruction = f.read()

def part1():
    disk = []
    fid = 0
    for index, char in enumerate(instruction):
        char = int(char)
        if index % 2 == 0:
            disk += [fid] * char
            fid += 1
        else: disk += [-1] * char
    blanks = []
    for index, char in enumerate(disk):
        if char == -1: blanks.append(index)
    
    for index in blanks:
        while disk[-1] == -1: disk.pop()
        if len(disk) <= index: break
        disk[index] = disk.pop()
    
    checksum = 0
    for index, char in enumerate(disk): checksum += index * char
    print(checksum)

def part2():
    files = {}
    blanks = []
    fid = 0
    pos = 0
    
    for index, char in enumerate(instruction):
        char = int(char)
        if index % 2 == 0:
            files[fid] = (pos, char)
            fid += 1
        else:
            blanks.append((pos, char))
        pos += char

    while fid > 0:
        fid -= 1
        fileStart, fileSize = files[fid]
        for blankIndex, (blankStart, blankSize) in enumerate(blanks):
            if fileStart <= blankStart:
                break
            if fileSize <= blankSize:
                files[fid] = (blankStart, fileSize)
                if fileSize == blankSize:
                    blanks.pop(blankIndex)
                else:
                    blanks[blankIndex] = (blankStart + fileSize, blankSize - fileSize)
                break

    checksum = 0
    for fid in files:
        index, size = files[fid]
        for temp in range(index, index + size):
            checksum += fid * temp
    print(checksum)

part1()
part2()