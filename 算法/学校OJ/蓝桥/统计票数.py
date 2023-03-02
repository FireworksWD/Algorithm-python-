a = list(map(int,input().split()))
b = []
for i in range(1,11):
    b.append(a.count(i))
    print(i,end=' ')
print()
for j in range(10):
    print(b[j],end=' ')