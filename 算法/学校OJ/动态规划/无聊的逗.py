n=int(input())
list_1=list(map(int,input().split()))
def subset(n):
    res=[[]]
    for i in n:
        res=res+[[i]+ x for x in res]
    return res
def dhset(n):
    total=sum(n)
    tar=sum(n)//2
    if total%2:
        return False,tar
    dp=[True]+[False]*tar
    for i in n:
        for j in range(tar,i-1,-1):
            dp[j]=dp[j] or dp[j-i]
    return dp[-1],tar
max_res=0
nums=subset(list_1)
for i in nums:
    if not nums:
        continue
    flag,tar=dhset(i)
    if flag and tar>max_res:
        max_res=tar
print(max_res)
