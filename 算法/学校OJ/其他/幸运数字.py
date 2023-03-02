a=[0,5,9]
ans=[float('inf')]*65
k=int(input())
while k:
    len=0
    while k:
        t=k%2
        if t==0:t=2
        len+=1
        ans[len]=a[t]
        k=(k-t)//2
    for i in range(len,0,-1):
        print(ans[i],end='')