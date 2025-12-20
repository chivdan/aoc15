import re

def solve(current):
    start = ord('a')
    next_char = {chr(i): chr(i + 1) for i in range(ord('a'), ord('a') + 26)}
    next_char['z'] = 'a'

    pwd = current 
    while True:
        i = len(pwd) - 1
        carry = False
        while True:
            if i == -1 and carry:
                pwd = "a" + pwd
                break
            carry = pwd[i] == 'z'
            pwd = pwd[:i] + next_char[pwd[i]] + pwd[i+1:]
            i -= 1
            if not carry:
                break

        # check rules
        if any(c in pwd for c in ["i", "o", "l"]):
            continue
        if not any(f"{chr(j)}{chr(j+1)}{chr(j+2)}" in pwd for j in range(start, start + 24)):
            continue
        m = re.match(".*([a-z])\\1.*([a-z])\\2.*", pwd)
        if m and m.group(1) != m.group(2):
            return pwd
        



if __name__ == '__main__':
    part1 = solve("hepxcrrq")
    print(part1)
    print(solve(part1))

