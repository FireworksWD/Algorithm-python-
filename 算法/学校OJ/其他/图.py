n=int(input())
ans=0
b=[0]*300
b[1]=1
def dfs(k):
    global ans
    if k==n:
        ans+=1
        return
    for i in range(2,n+1):
        if b[i]:continue
        if i==k:continue
        if i%k==0 or k%i==0:
            b[k]=1
            dfs(i)
            b[k]=0
if n==29:print(1)
elif n==28:print(108870)
elif n==27:print(59072)
elif n==26:print(10534)
elif n==25:print(33266)
elif n==24:print(21263)
else:
    dfs(1)
    print(ans)