def solve(part1: bool):
    result = 0
    for line in open("input.txt"):
        line = line.strip()
        code_len = len(line)

        if part1:
            mem_len = 0
            i = 1
            while i < len(line) - 1:
                if line[i] == "\\":
                    if line[i + 1] == "x":
                        mem_len += 1
                        i += 4
                    elif line[i + 1] == '"' or line[i + 1] == '\\':
                        mem_len += 1
                        i += 2
                else:
                    mem_len += 1
                    i += 1

            result += code_len - mem_len
        else:
            enc_len = 2
            for i in range(code_len):
                if line[i] == '"' or line[i] == '\\':
                    enc_len += 2
                else:
                    enc_len += 1
            result += enc_len - code_len


    print(result)


if __name__ == '__main__':
    solve(True)
    solve(False)
