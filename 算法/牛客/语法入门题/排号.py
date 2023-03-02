n = int(input())
s = []
for i in range(n):
    s1 = input()
    if s1 not in s:
        s.append(s1)
print(s.index('younik') + 1)
