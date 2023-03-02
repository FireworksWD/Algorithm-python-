'''l,n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(int(input()))
def check(x):
    la=0
    s=0
    for i in range(n):
        if a[i]-la>=x:
            la=a[i]
        else:
            s+=1
    if l-la<x:
        s+=1
    if s<=m:
        return s
y = 1
r=l
while r>y:
    mid = (1+r+y)//2
    if check(mid):
        y=mid
    else:
        r=mid-1
print(y)'''
import math
L,N,M=map(int,input().split())
D = []*50001
for i in range(N):
    D.append(int(input()))
high = L
low = D[0]
DL = []
DL.append(0)
DL.append(D[0])
for i in range(1, N):
    DL.append(D[i])
    d = D[i] - D[i - 1]
    if d < low:
        low = d
DL.append(L)
while low < high:
    mid = math.floor((high + low) / 2)
    pre_stone = 0
    temp_m = 0
    distance = []
    for j in range(1, len(DL)):
        if j == (len(DL) - 1):
            distance.append(DL[j] - pre_stone)
            break
        if (DL[j] - pre_stone) < mid:
            temp_m = temp_m + 1
        else:
            distance.append(DL[j] - pre_stone)
            pre_stone = DL[j]
        if temp_m > M:
            high = mid - 1
            break
    if temp_m == M:
        break
    elif temp_m < M:
        low = mid + 1
print(min(distance))