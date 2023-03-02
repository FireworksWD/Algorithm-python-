n, m = map(int, input('输入顶点数和几种颜色：').split())
cnt, color = 0, [-1] * 100  # cnt记录方案数，color记录每个顶点的颜色
c = [list(map(int,input().split())) for _ in range(n)]  # 输入邻接矩阵
def check(k):
    for i in range(n):
        if c[k][i] == 1 and color[k] == color[i]:  # k与i相连并且k的颜色与i的颜色相同
            return False
    return True
def GraphColor(step):
    global cnt
    if step == n:  # 所有顶点颜色搜索完
        cnt += 1  # 方案加一
        print(f'第{cnt}种方案的颜色：')
        for i in range(n):
            print(color[i], end=' ')  # 输出每个顶点的颜色
        print()
        return
    else:
        for i in range(m):
            color[step] = i  # 将顶点颜色换为颜色i
            if check(step):  # 是否符合条件
                GraphColor(step + 1)  # 下一步
            color[step] = -1  # 回溯置为-1
GraphColor(0)
print(cnt)
'''5 4
0 1 1 1 0
1 0 1 1 1
1 1 0 1 0
1 1 1 0 1
0 1 0 1 0


48
'''