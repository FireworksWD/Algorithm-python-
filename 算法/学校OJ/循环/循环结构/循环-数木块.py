n = int(input())
a=[]
x=1
for i in range(n):
    x=x+i
    a.append(x+i)
print(sum(a))