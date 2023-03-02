N, M, K, T = [int(x) for x in input().split()]
# 培育时间gT：growTime，初始种子seeds
gT = [int(x) for x in input().split()]
gT.insert(0, 0)
seeds = [int(x) for x in input().split()]
# 存杂交方案,hibrid[i] 为产生i作物的方案
hibrid = [[] for i in range(N+1)]
for i in range(1, K+1):
    A, B, C = [int(x) for x in input().split()]
    hibrid[C].append([A, B])

res = float("inf")
# 记录得到到该结点的距离，因为不记录的话搜索也可能出现回路，且会重复计算
dis = [float("inf") for _ in range(N+1)]
for x in seeds:
    dis[x] = 0


# 更新产生当前结点的最短时间，返回当前种子到已有种子的最短时间
def dfs(cur):
    global res, seeds
    if dis[cur] != float("inf"):
        return dis[cur]
    # 遍历杂交方案
    for hi in hibrid[cur]:
        growTime = max(gT[hi[0]], gT[hi[1]])
        dis[cur] = min(dis[cur], max(dfs(hi[0]), dfs(hi[1]))+growTime)
    # 更新
    return dis[cur]

dfs(T)
print(int(dis[T]))

