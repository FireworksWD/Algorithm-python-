n = int(input())
a = list(map(int,input().split()))
m = max(a)
s = min(a)
for j in range(len(a)):
    if m==a[j]:
        print(j,end=' ')
        break
for i in range(len(a)):
    if s==a[i]:
        print(i,end=' ')
        break
