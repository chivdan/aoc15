import hashlib

def solve(part1: bool):
    key = open("input.txt").read().strip()

    prefix = "00000" if part1 else "000000"

    i = 1
    while True:
        hex_str = hashlib.md5((f"{key}{i}").encode()).hexdigest()
        if hex_str.startswith(prefix):
            print(i)
            break
        i += 1

if __name__ == '__main__':
    solve(True)
    solve(False)
