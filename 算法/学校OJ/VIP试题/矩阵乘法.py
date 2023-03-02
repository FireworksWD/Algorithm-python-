n,m = map(int,input().split())
s = []
c = [[0]*n for i in range(n)]
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
s=a
for m in range(m-1,0,-1):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j]+=s[i][k]*a[k][j]
    for i in range(n):
        for j in range(n):
            s[i][j]=c[i][j]
            c[i][j]=0
for i in range(n):
    for j in range(n):
        print(s[i][j],end=' ')
    print()