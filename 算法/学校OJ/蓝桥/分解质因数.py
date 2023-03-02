n = int(input())
a=[]
for i in range(n):
    a.append(int(input()))
def fun(x):
    s=0
    for i in range(2,int(x**0.5)+1):
        while x%i==0:
            x//=i
            s+=1
        print(i,end=' ')
        print(s)
    if x>1:
        print(x,end=' ')
        print(1)
    print()
for i in range(n):
    fun(a[i])