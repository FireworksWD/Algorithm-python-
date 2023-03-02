n = int(input())
a = list(map(int,input().split()))
k = []
for i in range(len(a)):
    c=0
    for j in range(i):
        if a[j]<a[i]:
            c+=1
    k.append(c)
for z in range(len(k)):
    print(k[z], end=' ')