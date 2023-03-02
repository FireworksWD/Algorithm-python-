def yh(n):
    if n==1:
        res=[1]
    else:
        res=[[0]*n for i in range(n)]
        for i in range(n):
            for j in range(i+1):
                if i==0:
                    res[i][j]=1
                elif j==i:
                    res[i][j]=1
                else:res[i][j]=res[i-1][j]+res[i-1][j-1]
    return res[-1]
n,sum=map(int,input().split())
vis=[0]*n
yh=yh(n)
resut=[]
def dfs(step,s):
    if s>sum:
        return False
    if step==n:
        if s==sum:
            print(' '.join(str(i) for i in resut))
            return True
        else:
            return False
    for i in range(1,n+1):
        if vis[i-1]==0:
            vis[i-1]=1
            resut.append(i)
            if dfs(step+1,s+yh[step]*i):
                return True
            vis[i-1]=0
            resut.pop()
    return False
if n==1:
    print(sum)
else:
    dfs(0,0)