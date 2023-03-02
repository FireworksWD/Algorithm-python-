n, c = map(int, input('物品个数和背包容量空格分开：').split())
value = list(map(int, input('物品价值空格分开：').split()))
weight = list(map(int, input('物品重量空格分开：').split()))
bestvalue, curvalue, curweight = 0, 0, 0
vis = [False] * n
res = [] * n
def backtrack(t):
    global bestvalue, curvalue, curweight, res
    if t >= n:
        if curvalue > bestvalue:
            bestvalue = curvalue
            res = vis[:]
    else:
        if curweight + weight[t] < c:
            vis[t] = True
            curvalue += value[t]
            curweight += weight[t]
            backtrack(t + 1)
            curvalue -= value[t]
            curweight -= weight[t]
        vis[t] = False
        backtrack(t + 1)
backtrack(0)
print(bestvalue)
print(res)
