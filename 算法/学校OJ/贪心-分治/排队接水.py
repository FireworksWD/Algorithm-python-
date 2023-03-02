n,m=map(int,input().split())
time=0
i=0
w=[0]*10000
tap=[0]*100
a=list(map(int,input().split()))
for i in range(n):
    w[i]=a[i]
for i in range(m):
    tap[i]=w[i]
while i<n:
    su=tap[0]
    for j in range(m):
        su=min(su,tap[j])
    time+=su
    for j in range(m):
        tap[j]-=su
        if tap[j]==0:
            tap[j]=w[i+1]
left=0
for i in range(m):
    left=max(left,tap[i])
print(time+left)