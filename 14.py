from dataclasses import dataclass

@dataclass
class Deer:
    name: str
    speed: int
    move_time: int
    rest_time: int

def simulate(deer: Deer, T: int):
    d = 0
    t = 0
    while t <= T:
        delta_d = deer.speed * min(deer.move_time, T - t)
        d += delta_d
        t += deer.move_time + deer.rest_time
    return d

def simulate_part_2(deer: Deer, T: int):
    moving = True
    d = [0] * (T)
    t = 0
    while t < T:
        for _ in range(deer.move_time):
            if t >= T:
                break
            d[t] = d[t - 1] + deer.speed
            t += 1
        for _ in range(deer.rest_time):
            if t >= T:
                break
            d[t] = d[t - 1]
            t += 1
    return d

def solve(part1: bool):
    deer = []
    for line in open("input.txt"):
        s = line.strip().split()
        deer.append(Deer(s[0], int(s[3]), int(s[6]), int(s[-2])))

    T = 2503

    if part1:
        print(max(simulate(d, T) for d in deer)) 
    else:
        deer_results = [simulate_part_2(d, T) for d in deer]
        points = [0] * len(deer)
        for t in range(T):
            max_dist = max(d[t] for d in deer_results)
            for i in range(len(deer)):
                if deer_results[i][t] == max_dist:
                    points[i] += 1
        print(max(points))

if __name__ == '__main__':
    solve(True)
    solve(False)
