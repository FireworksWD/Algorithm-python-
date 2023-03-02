s = input()
f = True
for j in range(2 ** 64):
    vis = [1] * len(s)
    ts = ''
    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1] and s[i] != s[i + 1]:
            vis[i] = 0
            vis[i + 1] = 0
        if s[i] != s[i - 1] and s[i] == s[i + 1]:
            vis[i] = 0
            vis[i - 1] = 0
    for k in range(len(s)):
        if vis[k] == 1:
            ts += s[k]
    if len(ts) == len(s):
        print(ts)
        f = False
        break
    else:
        s = ts
if f:
    if s == '':
        print('EMPTY')
    else:
        print(s)
