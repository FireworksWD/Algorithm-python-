n,c=map(int,input().split())
a=[]
ans = 0
for i in range(n):
    a.append(list(map(int,input().split())))
for j in range(n):
    x = a[j][1]// a[j][0]
    a[j].append(x)
a.sort(key=lambda i:i[2],reverse=True)
for i in a:
    if i[0]<=c:
        ans+=i[1]
        c-=i[0]
    else:
        ans+=i[2]*c
        break
print(ans)