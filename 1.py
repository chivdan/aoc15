def solve(part1: bool):
    line = open("input.txt").read()
    line = [1 if c == "(" else -1 for c in line.strip()]
    if part1:
        print(sum(line))
    else:
        result = 0
        for i in range(len(line)):
            result += line[i]
            if result == -1:
                print(i + 1)
                return

if __name__ == '__main__':
    solve(True)
    solve(False)
