n = int(input())
s=0
a=[]
for i in range(1,43):
    s += int('1'*i)
    a.append(s%7)
x = n%42
if x==0:
    print(0)
else:
    print(a[x-1])