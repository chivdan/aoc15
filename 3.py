def solve(part1: bool):
    line = open("input.txt").read().strip()
    action_map = {"<": lambda i, j: (i, j - 1),
                  ">": lambda i, j: (i, j + 1),
                  "^": lambda i, j: (i - 1, j),
                  "v": lambda i, j: (i + 1, j)}

    if part1:
        (i, j) = (0, 0)
        visited = {(i, j)}
        for c in line:
            (i, j) = action_map[c](i, j)
            visited.add((i, j))
        print(len(visited))
    else:
        pos = [(0, 0), (0, 0)]
        visited = {pos[0]}
        for i, c in enumerate(line):
            pos[i % 2] = action_map[c](*pos[i % 2])
            visited.add(pos[i % 2])
        print(len(visited))


if __name__ == '__main__':
    solve(True)
    solve(False)
