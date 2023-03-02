n=int(input())
bag=[list(map(int,input().split())) for _ in range(n)]
res=[[0]*n for i in range(n)]
res[0][0]=bag[0][0]
for i in range(1,n):
    res[i][0]=res[i-1][0]+bag[i][0]
for j in range(1,n):
    res[0][j]=res[0][j-1]+bag[0][j]
for i in range(1,n):
    for j in range(1,n):
        res[i][j]=max(res[i-1][j]+bag[i][j],res[i][j-1]+bag[i][j])
print(res[-1][-1])
