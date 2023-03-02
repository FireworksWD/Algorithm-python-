dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
ans = 0
map = [[0 for i in range(7)] for _ in range(7)]


def DFS(x, y):
    if x == 0 or x == 6 or y == 0 or y == 6:
        global ans
        ans += 1
        return
    for i in range(4):
        newx = x + dx[i]
        newy = y + dy[i]
        # print(newx,newy)
        if map[newx][newy] == 0:
            map[newx][newy] = 1  # 标记走过
            map[6 - newx][6 - newy] = 1
            DFS(newx, newy)
            map[newx][newy] = 0  # 搜索完后没走过
            map[6 - newx][6 - newy] = 0


def main():
    map[3][3] = 1  # 从中心位置3,3开始
    DFS(3, 3)  # 深度搜索
    print(ans // 4)


if __name__ == '__main__':
    main()
