a,b,n,k=map(int,input().split())
y=(n*a-n*k)//(k*a-k*b)
x=(n-y*b)//a
print(f'{x} {y}')