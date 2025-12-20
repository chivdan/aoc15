import copy
import itertools
import numpy as np

def extract_W(objects, W):
    for n in range(1, len(objects)):
        for i in itertools.combinations(objects, n):
            if sum(i) == W:
                pass

def solve(part1: bool):
    packages = [int(line.strip()) for line in open("input.txt")]
    
    W = sum(packages)
    if part1:
        W /= 3
    else:
        W /= 4

    for N in range(1, len(packages)): 
        groups1 = []
        for i in itertools.combinations(packages, N):
            if sum(i) == W:
                groups1.append(i)
        groups1 = sorted(groups1, key=lambda g: np.prod(g))
        
        for g1 in groups1:
            remaining = set(copy.copy(packages))
            remaining = list(remaining.difference(g1))
            for N2 in range(1, len(remaining)):
                for j in itertools.combinations(remaining, N2):
                    if sum(j) == W:
                        if part1:
                            return np.prod(g1)
                        else:
                            remaining_2 = set(copy.copy(remaining))
                            remaining_2 = list(remaining_2.difference(j))
                            for N3 in range(1, len(remaining_2)):
                                for k in itertools.combinations(remaining_2, N3):
                                    if sum(k) == W:
                                        return np.prod(g1)
    
        

if __name__ == '__main__':
    print(solve(True))
    print(solve(False))
