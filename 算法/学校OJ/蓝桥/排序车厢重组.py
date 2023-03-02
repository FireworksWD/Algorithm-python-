n = int(input())
a = list(map(int, input().split()))
c=0
for i in range(len(a)):
    for j in range(i):
        if a[j] > a[i]:
            c+=1
print(c)