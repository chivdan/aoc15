def solve():
    code = 20151125
    i, j = 1, 1
    max_i = 1
    while True:
        if i == 1:
            max_i += 1
            i = max_i
            j = 1
        else:
            i -= 1
            j += 1
        max_i = max(i, max_i)

        code = (code * 252533) % 33554393

        if i == 2981 and j == 3075:
            print(code)
            break


if __name__ == '__main__':
    solve()
