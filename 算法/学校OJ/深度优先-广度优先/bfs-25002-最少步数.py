x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
dir = [[2, -1], [1, -2], [2, -2], [-2, -1], [-2, -2], [-1, -2], [-2, 1], [-2, 2], [-1, 2], [1, 2], [2, 1], [2, 2]]


def bfs(x, y):
    distance = [[0] * 101 for i in range(101)]
    vis = [[False] * 101 for _ in range(101)]
    vis[x1][y1] = True
    vis[x2][y2] = True
    queue = []
    queue.append([x, y])
    while len(queue) > 0:
        t1, t2 = queue.pop(0)
        for i, j in dir:
            tx = t1 + i
            ty = t2 + j
            if tx < 101 and tx > 0 and ty < 101 and ty > 0 and not vis[tx][ty]:
                queue.append([tx, ty])
                vis[tx][ty] = True
                distance[tx][ty] = distance[t1][t2] + 1
                if tx == 1 and ty == 1:
                    return distance[1][1]
        queue.pop(0)


print(bfs(x1, y1))
print(bfs(x2, y2))
