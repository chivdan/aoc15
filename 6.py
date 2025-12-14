import numpy as np

def solve(part1: bool):
    if part1:
        m = [[False] * 1000 for _ in range(1000)]
    else:
        m = np.zeros((1000, 1000))
    for line in open("input.txt"):
        s = line.strip().split()
        func = None

        if "turn" in line:
            si, sj = [int(v) for v in s[2].split(",")]
            ei, ej = [int(v) for v in s[4].split(",")]
            if part1:
                foo = lambda x: "on" in line 
            else:
                foo = lambda x: x + 1 if "on" in line else max(0, x - 1)
        elif "toggle" in line:
            si, sj = [int(v) for v in s[1].split(",")]
            ei, ej = [int(v) for v in s[3].split(",")]
            if part1:
                foo = lambda x: not x
            else:
                foo = lambda x: x + 2
        else:
            raise RuntimeError()


        for i in range(si, ei + 1):
            for j in range(sj, ej + 1):
                m[i][j] = foo(m[i][j])

    if part1:
        print(sum(sum(row) for row in m))
    else:
        print(int(m.sum()))


if __name__ == '__main__':
    solve(True)
    solve(False)
