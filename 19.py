import re
from functools import cache

def solve(part1: bool):
    repl = dict()
    molecule = None
    for line in open("input.txt"):
        if "=>" in line:
            src, dst = line.strip().split(" => ")
            if src not in repl:
                repl[src] = [dst]
            else:
                repl[src].append(dst)
        elif line:
            molecule = line.strip()

    if part1:
        prod = set()
        for src in repl:
            for dst in repl[src]:
                for m in re.finditer(src, molecule):
                    i, j = m.span()
                    s = molecule[:i] + dst + molecule[j:]
                    prod.add(s)
        print(len(prod))
    else:
        rev = dict()
        for k in repl:
            for v in repl[k]:
                if v in rev:
                    raise Exception()
                rev[v] = k

        cnt = 0
        while molecule != "e":
            for src, dst in rev.items():
                if src in molecule:
                    molecule = molecule.replace(src, dst, 1)
                    cnt += 1
                    break
        print(cnt)


if __name__ == '__main__':
    solve(True)
    solve(False)
