def solve(part1: bool):
    my_sue = dict()
    for line in open("sue.txt"):
        k, v = line.strip().split(": ")
        my_sue[k] = v


    max_match = 0
    best_num = -1
    for line in open("input.txt"):
        s = line.strip().split()
        num = int(s[1][:-1])
        d = {}
        for i in range(2, len(s), 2):
            k = s[i][:-1]
            v = s[i + 1].replace(",", "")
            d[k] = v
        score = 0
        for k in my_sue:
            if part1:
                if k in d and d[k] == my_sue[k]:
                    score += 1
            else:
                if k in d:
                    if k in ["cats", "trees"]:
                        if my_sue[k] < d[k]:
                            score += 1
                    elif k in ["pomeranians", "goldfish"]:
                        if my_sue[k] > d[k]:
                            score += 1
                    elif d[k] == my_sue[k]:
                        score += 1
        if score > max_match:
            max_match = score
            best_num = num
    print(best_num)


if __name__ == '__main__':
    solve(True)
    solve(False)
