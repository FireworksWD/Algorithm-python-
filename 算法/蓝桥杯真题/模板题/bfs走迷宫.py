n, m = map(int, input().split())
gra = [list(map(int, input().split())) for i in range(n)]
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
x1, y1, x2, y2 = map(int, input().split())
q = [[x1 - 1, y1 - 1, 0]]
f = True
while q:
    x, y, dis = q.pop(0)
    if x == x2 - 1 and y == y2 - 1:
        f = False
        print(dis)
        break
    for xx, yy in dirs:
        tx, ty = xx + x, yy + y
        if tx >= 0 and tx < n and ty >= 0 and ty < m and gra[tx][ty] == 1:
            gra[tx][ty] = 0
            q.append([tx, ty, dis+1])
if f: print(-1)
