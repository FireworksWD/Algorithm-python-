import math
a=[]
for i in str(math.factorial(100)):
    a.append(int(i))

a=a[::-1]
n=a[24]
c=0
for j in a:
    if j==0:
        c+=1
    else:
        break
print(c,end=' ')
print(n)