n = int(input())
a = list(map(int, input().split()))
s = set(a)
s = list(s)
s.sort()
for i in s:
    print(i, end=' ')