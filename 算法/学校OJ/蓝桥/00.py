a, b = map(int, input().split())
c=0
s=(bin(a)[2:])
k=(bin(b)[2:])
for i in range(len(s)):
    for j in range(len(k)):
        if s[i] == k[j]:
            c += 1
print(c)