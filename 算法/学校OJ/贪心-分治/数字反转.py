n=int(input())
s=0
if n<0:
    print('-',end='')
    n=n*(-1)
while n>0:
    s=s*10+n%10
    n=n//10
print(s)