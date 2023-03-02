n=int(input())
f=[[0]*2 for i in range(n+1)]
f[1][0]=9
f[1][1]=1
for i in range(2,n+1):
    x=9
    if i==n:x-=1
    f[i][0]=(f[i-1][0]*x+f[i-1][1])%12345
    f[i][1]=(f[i-1][1]*x+f[i-1][0])%12345
print(f[n][0])