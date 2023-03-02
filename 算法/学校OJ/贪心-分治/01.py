'''01背包：
m,n=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a.insert(0,[0,0])
bag=[[0 for i in range(m+1)]for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i][0]<=j:
            bag[i][j]=max(bag[i-1][j],bag[i-1][j-a[i][0]]+a[i][1])
        else:
            bag[i][j]=bag[i-1][j]
print(bag[-1][-1])'''
'''V,N = map(int, input().split())  # 物品数， 背包容量

v = [0] * (N + 1)  # 体积 索引从1开始到n
w = [0] * (N + 1)  # 价值 索引从1开始到n

for i in range(1, N + 1):
    v[i], w[i] = map(int, input().split())

f = [[0 for _ in range(V+1)] for i in range(N+1)]  # 初始化全0

for i in range(1, N + 1):
    for j in range(V + 1):
        f[i][j] = f[i - 1][j]

        if j >= v[i]:
            f[i][j] = max(f[i][j], f[i - 1][j - v[i]] + w[i])


print(f[N][V])'''
V,N = map(int, input().split())

v = [0] * (N + 1)
w = [0] * (N + 1)

for i in range(1, N + 1):
    v[i], w[i] = map(int, input().split())

f = [0 for i in range(V+1)]  # 初始化全0

for i in range(1, N + 1):
    for j in range(V, v[i]-1, -1):
        for k in range(0, j // v[i] + 1):
            f[j] = max(f[j], f[j - k * v[i]] + k * w[i])

print(f[V])
