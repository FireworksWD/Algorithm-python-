n = int(input())


def solve(x):
    for i in range(int((x // 4) ** 0.5) + 1):
        for j in range(int((x // 2) ** 0.5) + 1):
            for k in range(int((x * 3 // 4) ** 0.5) + 1):
                l = x - i ** 2 - j ** 2 - k ** 2
                if l < 0: continue
                if l == int(l ** 0.5) ** 2:
                    print(i, j, k, int(l ** 0.5))
                    return


solve(n)

import math
import sys

x = int(input())
t = [0] * 4


def dfs(nw, x, las):
    ysn = int(math.sqrt(x))
    if nw > 2:
        if ysn >= las and ysn * ysn == x:
            print(t[0], t[1], t[2], ysn)
            sys.exit(0)
        return
    for i in range(las, ysn + 1):
        t[nw] = i
        dfs(nw + 1, x - i * i, i)


dfs(0, x, 0)
