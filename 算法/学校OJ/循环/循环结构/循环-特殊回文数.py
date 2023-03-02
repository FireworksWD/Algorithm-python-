n = int(input())
for i in range(10000,100000):
    a,b,c,d,e=map(int, str(i))
    if a+b+c+d+e == n and str(i) == str(i)[::-1]:
        print(i)
for j in range(100000,1000000):
    a,b,c,d,e,f=map(int,str(j))
    if a+b+c+d+e+f == n and str(j) == str(j)[::-1]:
        print(j)