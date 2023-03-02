stx, sty = 0, 0
x, y = 0, 0
T = int(input())
res = []


def check(x, y, nn):
    if x >= 0 and x < nn and y >= 0 and y < nn:
        return True
    return False


for i in range(T):
    n = int(input())
    gra = [list(input()) for _ in range(n)]
    for k in range(n):
        for j in range(n):
            if gra[k][j] == 'S':
                x, y = k, j
                break
    q = int(input())
    questions = [list(input()) for _b in range(q)]
    # dirt = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
    for lis in questions:
        stx, sty = x, y
        f = False
        for j in lis:
            if j == 'L': sty -= 1
            if not check(stx, sty, n):
                f = True
                res.append('I am out!')
                break
            if check(stx, sty, n) and gra[stx][sty] == 'T':
                f = True
                res.append('I get there!')
                break
            if check(stx, sty, n) and gra[stx][sty] == '#':
                f = True
                res.append('I am dizzy!')
                break
            if j == 'R': sty += 1
            if not check(stx, sty, n):
                f = True
                res.append('I am out!')
                break
            if check(stx, sty, n) and gra[stx][sty] == 'T':
                f = True
                res.append('I get there!')
                break
            if check(stx, sty, n) and gra[stx][sty] == '#':
                f = True
                res.append('I am dizzy!')
                break
            if j == 'U': stx -= 1
            if not check(stx, sty, n):
                f = True
                res.append('I am out!')
                break
            if check(stx, sty, n) and gra[stx][sty] == 'T':
                f = True
                res.append('I get there!')
                break
            if check(stx, sty, n) and gra[stx][sty] == '#':
                f = True
                res.append('I am dizzy!')
                break
            if j == 'D': stx += 1
            if not check(stx, sty, n):
                f = True
                res.append('I am out!')
                break
            if check(stx, sty, n) and gra[stx][sty] == 'T':
                f = True
                res.append('I get there!')
                break
            if check(stx, sty, n) and gra[stx][sty] == '#':
                f = True
                res.append('I am dizzy!')
                break
        if not f:
            res.append('I have no idea!')
for i in res:
    print(i)
