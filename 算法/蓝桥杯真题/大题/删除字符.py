s = list(input())
t = int(input())
for i in range(t):
    s.remove(max(s[0], s[1]))
print(''.join(s))
