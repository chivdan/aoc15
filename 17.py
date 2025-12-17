import itertools

def solve(part1: bool):
    containers = [int(line.strip()) for line in open("input.txt")]

    result = 0
    min_containers = 1e10
    D = dict()
    for i in itertools.product([True, False], repeat=len(containers)):
        if sum(int(coef) * cap for coef, cap in zip(i, containers)) == 150:
            result += 1
            if sum(i) <= min_containers:
                min_containers = sum(i)
                the_containers = [containers[j] for j in range(len(containers)) if i[j]]
                the_containers = "_".join([str(v) for v in the_containers])
                if min_containers not in D:
                    D[min_containers] = {the_containers}
                else:
                    D[min_containers].add(the_containers)

    if part1:
        print(result)
    else:
        print(len(D[min_containers]))


if __name__ == '__main__':
    solve(True)
    solve(False)
