import itertools
import numpy as np

def solve(part1: bool):
    def score(counts):
        sums = [0] * 5
        for i in range(5):
            sums[i] = max(0, sum(ingredients[j][i] * counts[j] for j in range(len(ingredients))))
            if i < 4 and sums[i] == 0:
                return 0
        return np.prod(sums[:-1])

    ingredients = []
    for line in open("input.txt"):
        s = line.strip().split()
        ingredients.append([int(s[2][:-1]), int(s[4][:-1]), int(s[6][:-1]), int(s[8][:-1]), int(s[10])])

    C = 100
    max_score = 0
    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - i - j):
                l = 100 - i - j - k
                counts = [i, j, k, l]
                if not part1:
                    if sum(ingredients[j][4] * counts[j] for j in range(len(counts))) != 500:
                        continue
                s = score(counts)
                max_score = max(s, max_score)
    print(max_score)



if __name__ == '__main__':
    solve(True)
    solve(False)
