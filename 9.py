import copy

def solve(part1: bool):

    foo = min if part1 else max

    g = {}
    for line in open("input.txt"):
        s = line.split()
        src, dst, d = s[0], s[2], int(s[4])
        if src not in g:
            g[src] = {dst: d}
        else:
            g[src][dst] = d
        if dst not in g:
            g[dst] = {src: d}
        else:
            g[dst][src] = d
    
    def min_ham_path(u, visited, cost):
        if len(visited) == len(g):
            return cost
        children = []
        for v in g[u].keys():
            if v in visited:
                continue
            new_visited = copy.copy(visited)
            new_visited.add(v)
            children.append((v, new_visited, cost + g[u][v]))
        return foo([min_ham_path(*child) for child in children])

    result = foo(min_ham_path(start, {start}, 0) for start in g) 
    print(result)




if __name__ == '__main__':
    solve(True)
    solve(False)
