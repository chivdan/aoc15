import re

def solve(part1: bool):
    s = open("input.txt").read()
    if part1:
        print(sum(int(v) for v in re.findall("\-?[0-9]+", s)))
    else:
        stack = [[False, 0]]
        cur_num = ""
        for i, c in enumerate(s):
            if cur_num and not c.isdigit():
                stack[0][1] += int(cur_num)
                cur_num = ""

            if c == "{":
                stack.insert(0, [False, 0])
            elif c == "}":
                (r, n) = stack[0]
                stack.pop(0)
                if not r:
                    stack[0][1] += n
            elif c == "[":
                stack.insert(0, [False, 0])
            elif c == "]":
                (r, n) = stack[0]
                stack.pop(0)
                stack[0][1] += n
            elif s[i:i+5] == '"red"':
                stack[0][0] = True
            elif c.isdigit():
                cur_num += c
            elif c == "-" and not cur_num:
                cur_num = "-"

        result = 0
        if not stack[0][0]:
            result = stack[0][1]
        print(result)

if __name__ == '__main__':
    solve(True)
    solve(False)
