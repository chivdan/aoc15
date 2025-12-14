def solve(part1: bool):
    result = 0
    for line in open("input.txt"):
        l, w, h = [int(v) for v in line.strip().split("x")]
        if part1:
            areas = [l*w, w*h, h*l]
            result += 2*sum(areas) + min(areas)
        else:
            perimeters = [2 * (l + w), 2 * (w + h), 2 * (h + l)]
            result += min(perimeters) + l*w*h
    print(result)

if __name__ == '__main__':
    solve(True)
    solve(False)
