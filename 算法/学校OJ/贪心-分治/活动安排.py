n = int(input())
a = []
c=1
j=1
for i in range(n):
    a.append(list(map(int,input().split())))
a.sort(key=lambda i:i[1],reverse=False)
print(a)
i=0
while i<n-1:
    if a[i][1]<=a[j][0]:
        i=j
        j+=1
        c+=1
    else:
        j+=1
print(c)