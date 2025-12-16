import itertools

def solve(part1: bool):

    def pref(arr):
        result = 0
        for u, v in itertools.pairwise(arr):
            if u in data and v in data[u]:
                result += data[u][v]
            if v in data and u in data[v]:
                result += data[v][u]

        if arr[0] in data and arr[-1] in data[arr[0]]:
            result += data[arr[0]][arr[-1]]
        if arr[-1] in data and arr[0] in data[arr[-1]]:
             result += data[arr[-1]][arr[0]]
        
        return result


    data = {}

    actors = set()
    for line in open("input.txt"):
        s = line.strip()[:-1].split()
        src, dst, sign, cost = s[0], s[-1], -1 if s[2] == "lose" else 1, int(s[3])
        if src not in data:
            data[src] = {dst: sign * cost}
        else:
            data[src][dst] = sign * cost

        actors.add(src)
        actors.add(dst)

    if not part1:
        data["me"] = {}
        for other in data:
            data["me"][other] = 0
            data[other]["me"] = 0
        actors.add("me")
    
    result = max(pref(i) for i in itertools.permutations(actors, r=len(actors)))
    print(result)


if __name__ == '__main__':
    solve(True)
    solve(False)
