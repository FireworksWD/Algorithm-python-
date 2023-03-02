n = int(input())
a = [int(i) for i in str(n)]
a = a[::-1]
for i in a:
    print(i,end=' ')
print(sum(a))