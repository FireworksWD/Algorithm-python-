a = list(map(int, input().split()))
a.sort()
s = (a[2]*2-a[1]-a[0]+1)//2
while (a[0]+a[1]+a[2]+s*2)%3 != 0:
    s+=1
print(s)