import copy

def solve(part1: bool):
    m = []
    for line in open("input.txt"):
        m.append([False if v == "." else True for v in line[:-1]])

    def neighbors(i, j):
        result = []
        for ii in [i - 1, i, i + 1]:
            for jj in [j - 1, j, j + 1]:
                if ii == i and jj == j:
                    continue
                if ii < 0 or ii >= 100:
                    continue
                if jj < 0 or jj >= 100:
                    continue
                result.append((ii, jj))
        return result

    def fix_corners(m):
        m[0][0] = True
        m[0][99] = True
        m[99][0] = True
        m[99][99] = True
    
    if not part1:
        fix_corners(m)

    for _ in range(100):
        m_next = copy.deepcopy(m)
        for i in range(100):
            for j in range(100):
                s = sum(m[ii][jj] for (ii, jj) in neighbors(i, j))
                if m[i][j]:
                    if s not in [2, 3]:
                        m_next[i][j] = False
                elif s == 3:
                    m_next[i][j] = True
        if not part1:
            fix_corners(m_next)
        m = m_next

    print(sum(sum(row) for row in m))

if __name__ == '__main__':
    solve(True)
    solve(False)
