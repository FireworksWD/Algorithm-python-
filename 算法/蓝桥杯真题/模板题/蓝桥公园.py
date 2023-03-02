n, m, q = map(int, input().split())
distance = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    x, y, z = map(int, input().split())
    distance[x][y] = z
for i in range(1, n + 1):
    distance[i][i] = 0


def floyd():
    global n
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])


floyd()
res = []
for _b in range(q):
    a, b = map(int, input().split())
    if distance[a][b] == float('inf'):
        res.append(-1)
    else:
        res.append(distance[a][b])
for i in res:
    print(i)
