n = int(input())
a,b,c=map(int,str(n))
q=0
for i in range(100,1000):
    x,y,z=map(int, str(i))
    if z+c>=10 or y+b>=10 or x+a>=10:
        q+=1
print(q)