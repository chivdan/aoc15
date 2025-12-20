def solve(part1: bool):
    instructions = []
    for line in open("input.txt"):
        s = line.strip().split()
        command = s[0]
        if command in ["jio", "jie"]:
            reg, offset = s[1][:-1], s[2]
            if offset.startswith("+"):
                offset = int(offset[1:])
            else:
                offset = -int(offset[1:])
            instructions.append((command, reg, offset))
        elif command == "jmp":
            offset = s[1]
            if offset.startswith("+"):
                offset = int(offset[1:])
            else:
                offset = -int(offset[1:])
            instructions.append((command, offset))
        else:
            instructions.append(tuple(s))

    reg = {"a": 0 if part1 else 1, "b": 0}
    pos = 0
    while 0 <= pos < len(instructions):
        inst = instructions[pos]
        command = inst[0]
        if command == "hlf":
            reg[inst[1]] = reg[inst[1]] // 2
            pos += 1
            continue
        elif command == "tpl":
            reg[inst[1]] *= 3
            pos += 1
            continue
        elif command == "inc":
            reg[inst[1]] += 1
            pos += 1
            continue
        elif command == "jmp":
            pos += inst[1]
            continue
        elif command == "jie":
            if reg[inst[1]] % 2 == 0:
                pos += inst[2]
            else:
                pos += 1
        elif command == "jio":
            if reg[inst[1]] == 1:
                pos += inst[2]
            else:
                pos += 1

    print(reg["b"])



if __name__ == '__main__':
    solve(True)
    solve(False)
